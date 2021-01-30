#ifndef BOOK_H
#define BOOK_H
#include<bits/stdc++.h>
#include<fstream>
using namespace std;

class Book
{
    string title;
    string author;
    string type;
    string path;
    string filename;

    public:
        Book();
        string get_type();
        string get_title();
        string get_author();
        string get_path();
        string get_filename();
        void set_type(string book_type);
        void set_author(string book_author);
        void set_title(string book_title);
        void set_path(string book_path);
        void set_filename(string book_name);
        void update_book_from_path(int base_len,string book_path);
        void copy_from_book(Book b);
};

ostream& operator <<(ostream& fout,Book& b);
istream& operator >>(istream& fin,Book &b);

class Novel: public Book
{
    vector<string> chapter;
    vector<vector<string>> paragraph;
    public:
        Novel();
        Novel(Book b);
        vector<string> get_chapters();
        vector<vector<string>> get_paragraphs();
};

class Play: public Book
{

};

#endif