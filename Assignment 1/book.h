#ifndef BOOK_H
#define BOOK_H
#include<bits/stdc++.h>
#include<fstream>
using namespace std;

class Book
{
    protected:
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
        friend ostream& operator <<(ostream& fout,Book& b);
        friend istream& operator >>(istream& fin,Book& b);
};

class Paragraph
{
    public :
        string para; 
};

class Chapter
{
    public:
        string name;
        vector<Paragraph> chap; 
};

class Novel: public Book
{
    public :
        vector<Chapter> chapters;

        Novel();
        Novel(Book b);
};

class Scene
{
    public:
        string scene;
};

class Act
{
    public :
        vector<Scene> act;
};

class Play: public Book
{
    public:
        vector<Act> acts;
        Play();
        Play(Book b);

};

#endif