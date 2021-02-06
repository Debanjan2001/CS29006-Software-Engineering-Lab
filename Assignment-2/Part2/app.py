# from tkinter import *
import os
# root = Tk()



       
        
# class App(Frame):
#     def __init__(self,master = None):
#         super().__init__(master)
#         self.master = master

#         self.menubar = Menu(self.master)
#         self.usermenu = Menu(self.menubar, tearoff=0)
#         self.usermenu.add_command(label="Select User")
#         self.menubar.add_cascade(label="Select User", menu=self.usermenu)
#         self.master.config(menu=self.menubar)


# app = App(root)
# # root.config(menu=app.menubar.user_menubar)
# root.mainloop()

class User():
    def __init__(self,userid=None,contact_list = None):
        self.userid = userid
        self.contact_list = contact_list
        self.messages = []

    def get_userid(self):
        return self.userid

    def get_contact_list(self):
        return self.contact_list
    
    def add_message(self,post):
        self.messages.append(post)


class Group():
    def __init__(self,groupid=None,member_list = None):
        self.groupid = groupid
        self.member_list = member_list
        self.messages = []
    
    def get_groupid(self):
        return self.groupid

    def get_member_list(self):
        return self.member_list

    def add_message(self,post):
        self.messages.append(post)
        

# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_file():

    file = open("social_network.txt",'r')
    # print("File name: "+file.name)
    hash_cnt = 0
    user_list= []
    group_list = []

    for line in file:
        # print(line)
        if line[0]=='#':
            hash_cnt += 1
        else:
            line = line.strip(' ')
            line = line.strip('\n')
            line = str(line[1:len(line)-1])
            line = line.split(':')

            # print(line)

            if hash_cnt == 1:
                userid = line[0]
                contact_list = []
                line[1] = line[1].split(',')
                for contact in line[1]:
                    contact_list.append(contact)

                user = User(userid=userid,contact_list=contact_list)
                user_list.append(user)

            else:
                line[1] = line[1].split(',')
                groupid = line[0]
                member_list = []
                for member in line[1]:
                    member_list.append(member)

                group = Group(groupid=groupid,member_list=member_list)
                group_list.append(group)
            
    file.close()

    # for group in group_list:
    #     print( group.get_groupid())
    #     for y in group.get_member_list():
    #         print(y+", ",end='')
    #     print()
        
if __name__== "__main__":
    # read_file()