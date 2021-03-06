#include<bits/stdc++.h>
#include <boost/filesystem.hpp>
#include<fstream>
#include<curses.h>
#include "book.h"

using namespace std;

class Library
{
    boost::filesystem::path base_dir;
    vector<Book> books;
    public:

        Library()
        {
            cout<<"TO CREATE THE LIBRARY YOU NEED TO PROVIDE A DIRECTORY CONTAINING THE BOOKS..."<<endl;
            cout<<">> ENTER NAME OF THE DIRECTORY CONTAINING THE BOOKS: ";
            cin>>base_dir;
        }

        void welcome_message()
        {
            cout<<endl;
            cout<<"LMS PROVIDES YOU THE FOLLOWING FEATURES"<<endl;
            cout<<"ENTER 1 TO SEE LIST OF ALL BOOKS"<<endl;
            cout<<"ENTER 2 TO SEARCH FOR SOME BOOK"<<endl;
            cout<<"ENTER 3 TO READ A BOOK"<<endl;
            cout<<"ENTER 4 FOR PERFORMING ANALYTICS"<<endl;
            cout<<"ENTER -1 TO EXIT THIS LIBRARY"<<endl;
        }

        void update_library()
        {
            ifstream fin;
            ofstream fout;
           
            fin.open("index.txt");

            int base_dir_len = base_dir.string().length(); 

            set<string> previous_books,current_books;
            vector<Book> old_books;
            while(!fin.eof())
            {
                Book b;
                fin>>b;
                previous_books.insert(b.get_filename());
                old_books.push_back(b);
            }

            fin.close();

            vector<boost::filesystem::directory_entry> files;

            if(boost::filesystem::is_directory(base_dir))
            {
                copy(boost::filesystem::directory_iterator(base_dir),boost::filesystem::directory_iterator(),back_inserter(files));

                for (vector<boost::filesystem::directory_entry>::const_iterator it = files.begin(); it != files.end();  ++it )
                {
                    string book_address = (*it).path().string();
                    int base_len = base_dir.string().length();
                    string book_name = string(book_address.begin()+base_len+1,book_address.end());
                    current_books.insert(book_name);
                }  
            }

            fout.open("index.txt");


            for(set<string>::iterator it = current_books.begin();it!=current_books.end();it++)
            {
                string book_name = *it;
                if(previous_books.find(book_name) == previous_books.end())
                {
                    cout<<"FOUND A NEW BOOK NAMED: "<< book_name <<endl;
                    Book new_book;
                    cout<<">> ENTER TYPE OF THE BOOK :"; 
                    string book_type;
                    cin>>book_type;
                    new_book.set_type(book_type);
                    new_book.set_filename(book_name);
                    new_book.update_book_from_path(base_dir_len,base_dir.string()+"/"+book_name);
                    books.push_back(new_book);
                    
                    fout<< new_book;
                }
                else
                {
                    Book b;
                    for(int i=0;i<old_books.size();i++)
                    {
                        if(old_books[i].get_filename()==book_name)
                        {
                            b = old_books[i];
                            break;
                        }
                    }
                    books.push_back(b);
                    fout<< b;
                }
            }

            fout.close();

            cout<<"SUCCESSFULLY CREATED AND UPDATED THE LIBRARY...\n"<<endl;
        }

        void enumerate_book(Book current,int i)
        {
            cout<<"Book Number: "<<i+1<<endl;
            cout<<"Filename : "<<current.get_filename()<<endl;
            cout<<"Title : "<<current.get_title()<<endl;
            cout<<"Author : "<<current.get_author()<<endl;
            cout<<endl;
        }

        void list_all_books()
        {
            cout<<"DISPLAYING ALL BOOKS IN THE LIBRARY..."<<endl;
            if(books.size()==0)
            {
                cout<<"NO BOOKS AVAILABLE!"<<endl;
                return;
            }
            for(int i=0;i<books.size();i++)
            {
                Book current = books[i];
                enumerate_book(current,i);
            }
        }

        void search_books()
        {
            cout<<"YOU CAN SEARCH BY TITLE OR AUTHOR'S NAME."<<endl;
            cout<<"PRESS 1 TO SEARCH BY TITLE \nPRESS 2 TO SEARCH BY AUTHOR'S NAME"<<endl;
            cout<<">> ";
            int input;
            cin>>input;
            vector<pair<Book,int>> queryset;
            if(input==1)
            {
                cout<<">> ENTER TITLE: ";
                string book_title;
                cin>>book_title;
                regex r(book_title,regex::icase);
                for(int i=0;i<books.size();i++)
                {
                    if( regex_search(books[i].get_title(),r ))
                    {
                        queryset.push_back({books[i],i});
                    }
                }
            }
            else if(input==2)
            {
                cout<<">> ENTER AUTHOR'S NAME: ";
                string book_author;
                cin>>book_author;

                regex r(book_author,regex::icase);
                for(int i=0;i<books.size();i++)
                {
                    if( regex_search(books[i].get_author(),r ))
                    {
                        queryset.push_back({books[i],i});
                    }
                }
            }
            else
            {
                return;
            }

            cout<<"DISPLAYING RESULTS BASED ON YOUR SEARCH..."<<endl;
            if(queryset.size()>0)
            {
                for(int i=0;i<queryset.size();i++)
                {
                    enumerate_book(queryset[i].first,queryset[i].second);
                }
            }
            else
            {
                cout<<"NO RESULTS FOUND BASED ON YOUR SEARCH"<<endl;
                return;
            }

            input = 100;

            while(input!=-1)
            {
                cout<<"DO YOU WANT TO READ OR ANALYSE ANY OF THE BOOKS FOUND IN YOUR SEARCH?"<<endl;
                cout<<"ENTER 1 TO READ A BOOK"<<endl;
                cout<<"ENTER 2 TO ANALYSE A BOOK"<<endl;
                cout<<"ENTER -1 TO EXIT FROM HERE"<<endl;

                cout<<">> ";
                cin>>input;

                if(input == -1)
                    break;

                cout<<"HERE ARE THE BOOKS"<<endl;
                for(int i=0;i<queryset.size();i++)
                {
                    enumerate_book(queryset[i].first,queryset[i].second);
                }
                cout<<">> ENTER BOOK NUMBER ";
                if(input ==1)
                    cout<<"TO READ IT: ";
                else
                    cout<<"TO PERFORM ANALYTICS: ";
                int book_num;
                cin>>book_num;
                
                if(input == 1)
                {
                    display_book(book_num);
                }
                else if(input == 2)
                {
                    analytics(book_num);   
                }
            }
        }

        void display_book(int id)
        {
            if(books.size()==0)
            {
                cout<<"NO BOOKS AVAILABLE!"<<endl;
                return;
            }
            if(id<0)
                return;

            Book b = books[id-1];
            ifstream fin;
            fin.open(b.get_path().c_str());

            vector<string> pages;

            while(!fin.eof())
            {
                string thispage="";
                for(int i=0;i<30 && fin.eof()==false;i++)
                {
                    string s;
                    getline(fin,s);
                    thispage += "\n"+ s;
                }
                pages.push_back(thispage);
            }

            string inp="XXX";
            
            int pagenum=0;
            system("clear");
            cout<<pages[pagenum]<<endl<<endl;
            while(inp!="Q" || inp!="q")
            {
                cout<<"PRESS Q TO QUIT READING"<<endl;
                if(pagenum>0)
                    cout<<"PRESS B TO GO TO PREVIOUS PAGE"<<endl;
                if(pagenum!=pages.size()-1)
                    cout<<"ENTER N TO CONTINUE TO NEXT PAGE"<<endl;
                cout<<">> ";
                cin>>inp;

                if(inp=="B" || inp=="b")
                    pagenum--;
                else if(inp=="N" || inp=="n")
                    pagenum++;
                else
                    break;

                system("clear");

                cout<<pages[pagenum]<<endl<<endl;
            }
        }

        void analytics(int id)
        {
            if(id<=0)
                return;

            Book b = books[id-1];

            string type = b.get_type();
            ifstream fin;
            fin.open(b.get_path().c_str());

            if(type[0] == 'n' || type[0] == 'N')
            {
                Novel curr = Novel(b);
                cout<<">> ENTER A WORD TO ANALYSE: ";
                string word;
                cin>>word;
                regex r(word,regex::icase);
                int k;
                cout<<">> ENTER VALUE OF K for TOP-K ANALYTICS: ";
                cin>>k;

                set<pair<int,int>> query_chap;
                set<pair<int,pair<int,int>>> query_para;
                
                int tot_count = 0;

                for(int i=0;i<curr.chapters.size();i++)
                {
                    for(int j=0;j<curr.chapters[i].chap.size();j++)
                    {
                        string str = curr.chapters[i].chap[j].para;
                        int word_count = 0;
                        istringstream iss(str);
                        do
                        {
                            string subs;
                            iss >> subs;
                            if(regex_search(subs,r))
                            {
                                word_count++;
                            }
                        } while (iss);

                        query_para.insert({word_count,{i,j}});

                        if(query_para.size()>k)
                        {
                            query_para.erase(query_para.begin());
                        }
                        
                        tot_count += word_count;

                    }

                    query_chap.insert({tot_count,i});
                    if(query_chap.size()>k)
                    {
                        query_chap.erase(query_chap.begin());
                    }
               		
               		tot_count = 0;

                }

               
                int input = 0;
                

                while(input!=-1)
                {       
                    cout<<"ENTER 1 TO SEE TOP "<<k<<" CHAPTERS CONTAINING THE WORD: \""<<word<<"\""<<endl;
                    cout<<"ENTER 2 TO SEE TOP "<<k<<" PARAGRAPHS CONTAINING THE WORD: \""<<word<<"\""<<endl;
                    cout<<"ENTER -1 TO EXIT"<<endl;
                    cout<<">> ";
                    cin>>input;         
                    if(input == 1)
                    {
                        cout<<"TOP "<<k<<" CHAPTERS BASED ON YOUR WORD: "<<endl<<endl;
                        for(set<pair<int,int>>::reverse_iterator it=query_chap.rbegin();it!=query_chap.rend(); ++it)
                        {
                            int id = it->second;
                            cout<<"   "<<curr.chapters[id].name<<" "<<" : \""<<word<<"\" APPEARED "<<it->first<<" TIMES "<<"\n";
                        }
                        cout<<endl;
                    }
                    else if(input == 2)
                    {
                        cout<<"TOP "<<k<<" PARAGRAPHS BASED ON YOUR WORD: "<<endl<<endl;

                        for(set<pair<int,pair<int,int>>>::reverse_iterator it=query_para.rbegin();it!=query_para.rend(); ++it)
                        {
                            int i= (it->second).first,j = (it->second).second;
                            cout<<"**************************************************************"<<endl;
                            cout<<"PARAGRAPH "<<j<<" FROM CHAPTER "<<i<<" : \""<<word<<"\" APPEARED "<<it->first<<" TIMES "<<"\n";
                            cout<<"**************************************************************"<<endl;
                            cout<<curr.chapters[i].chap[j].para<<endl<<endl;
                        }
                    }
                }

            }
            else if(type[0] == 'p' || type[0] == 'P')
            {
                Play curr = Play(b);
                string character;
                cout<<">> ENTER NAME OF A CHARACTER: ";
                cin>>character;
                
                for(int i=0;i<character.length();i++)
                {
                    character[i] = toupper(character[i]);
                }

                set<string> query;
                string line ="";

                for(int i=0;i<curr.acts.size();i++)
                {
                    for(int j=0;j<curr.acts[i].act.size();j++)
                    {
                        string str = curr.acts[i].act[j].scene;
                        istringstream iss(str);
                        set<string> st;
                        do{
                            getline(iss,line);
                            if(line.size()>1 && line[0]>='A' && line[0]<='Z' && line[1]>='A' && line[1]<='Z')
                            {
                                st.insert(string(line.begin(),line.end()-1));
                            }
                            
                        }while(iss);

                        if(st.find(character)!=st.end())
                        {
                            st.erase(character);
                            for(set<string>::iterator it =st.begin();it!=st.end();it++)
                            {
                                query.insert(*it);
                            }
                        }
                    }
                }

                if(query.size()==0)
                {
                    cout<<"NO CHARACTED NAMED \""<<character<<"\" FOUND IN THIS BOOK ! "<<endl;
                    return;
                }

                cout<<"A LIST OF ALL OTHER CHARACTERS WHO APPEAR IN AT LEAST ONE SCENE WITH : "<<character<<endl; 
                int count = 0;
                for(set<string>::iterator it =query.begin();it!=query.end();it++)
                {
                    cout<<"   "<<(++count)<<". "<<*it<<endl;
                }

            }

            fin.close();
        }

        ~Library()
        {
            for(int i=0;i<books.size();i++)
            {
                books.pop_back();
            }
        }
};



int main()
{
    Library lib;
    lib.update_library();

    cout<<"WELCOME TO DEBANJAN'S LIBRARY..."<<endl;
    int input = 1;
    while(input != -1)
    {
        lib.welcome_message();
        cout<<">> ";
        cin>>input;
        if(input == 1)
        {
            lib.list_all_books();
        }
        else if(input == 2)
        {
            lib.search_books();
        }
        else if(input == 3)
        {
            lib.list_all_books();
            cout<<">> ENTER THE BOOK NUMBER WHICH YOU WANT TO READ :";
            int book_num;
            cin>>book_num;
            lib.display_book(book_num);
        }
        else if(input == 4)
        {
             lib.list_all_books();
            cout<<">> ENTER THE BOOK NUMBER OF THE BOOK FOR PERFORMING ANALYTICS: ";
            int book_num;
            cin>>book_num;
            lib.analytics(book_num);
        }
    }

    cout<<"HAVE A GOOD DAY...BYE"<<endl;
    return 0;
}


