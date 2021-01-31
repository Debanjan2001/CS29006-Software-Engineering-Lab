#include<bits/stdc++.h>
#include "book.h"
#include<fstream>
using namespace std;

Book::Book()
{
    title = "";
    author = "";
    type = "";
    path = "";
    filename = "";
}


string Book::get_type()
{
    return type;
}
string Book::get_title()
{
    return title;
}
string Book::get_author()
{
    return author;
}
string Book::get_path()
{
    return path;
}
string Book::get_filename()
{
    return filename;
}

void Book::set_type(string book_type)
{
    type = book_type;
}

void Book::set_author(string book_author)
{
    author = book_author;
}

void Book::set_title(string book_title)
{
    title = book_title;
}

void Book::set_path(string book_path)
{
    path = book_path;
} 
void Book::set_filename(string book_name)
{
    filename = book_name;
} 

void Book::update_book_from_path(int base_len,string book_path)
{
    ifstream fin;
    fin.open(book_path.c_str());
    path = book_path;
    filename = string(book_path.begin()+base_len+1,book_path.end());

    string line="";
    regex end ("[***]");

    while ( regex_search(line,end) == 0)
    {
        getline(fin,line);
        regex book_title("Title");
        regex book_author("Author");

        if(regex_search(line,book_title) )
        {
            title = string(line.begin()+7,line.end());
        }
        if(regex_search(line,book_author))
        {
            author = string(line.begin()+8,line.end());
        }
    }
}

void Book::copy_from_book(Book b)
{
    path = b.get_path();
    author = b.get_author();
    title = b.get_title();
    type = b.get_type();
    filename = b.get_filename();
}

ostream& operator <<(ostream& fout,Book& b)
{
    fout<<b.get_title()<<endl;
    fout<<b.get_author()<<endl;
    fout<<b.get_type()<<endl;
    fout<<b.get_path()<<endl;
    fout<<b.get_filename()<<endl;
    return fout;
}

istream& operator >>(istream& fin,Book &b)
{
    string s;
    getline(fin,s);
    b.set_title(s);

    getline(fin,s);
    b.set_author(s);
    
    getline(fin,s);
    b.set_type(s);
    
    getline(fin,s);
    b.set_path(s);
    
    getline(fin,s);
    b.set_filename(s);
    
    return fin;
}

Novel::Novel(Book b)
{
    copy_from_book(b);
    ifstream fin;
    fin.open(get_path().c_str());

    regex chapter("CHAPTER");
    string line="";

    while(!fin.eof() && !regex_search(line,chapter))
        getline(fin,line);

    string chapter_name = line; 
    vector<Paragraph> ch;
    Paragraph p;
    p.para = "";


    while(!fin.eof())
    {   
        getline(fin,line);
        if(regex_search(line,chapter)==true && line[0]=='C')
        {
            Chapter newch;
            newch.name = chapter_name;
            newch.chap = ch; 
            chapters.push_back(newch);
            p.para = "";
            ch.clear();
            chapter_name = line;
        }
        else
            p.para += line;
        if(line.length() == 0)
        {
            if(p.para.length()>0)
                ch.push_back(p);
            p.para = "";
        }
    }

    Chapter newch;
    newch.name = chapter_name;
    newch.chap = ch; 
    chapters.push_back(newch);

    fin.close();
}




