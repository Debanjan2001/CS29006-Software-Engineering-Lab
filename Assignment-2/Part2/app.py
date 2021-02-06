# class User():
#     def __init__(self,userid=None,contact_list = None):
#         self.userid = userid
#         self.contact_list = contact_list
#         self.messages = []

#     def get_userid(self):
#         return self.userid

#     def get_contact_list(self):
#         return self.contact_list
    
#     def add_message(self,post):
#         self.messages.append(post)


# class Group():
#     def __init__(self,groupid=None,member_list = None):
#         self.groupid = groupid
#         self.member_list = member_list
#         self.messages = []
    
#     def get_groupid(self):
#         return self.groupid

#     def get_member_list(self):
#         return self.member_list

#     def add_message(self,post):
#         self.messages.append(post)
        

def read_file():

    file = open("social_network.txt",'r')
    # print("File name: "+file.name)
    hash_cnt = 0
    user_dict= {}
    group_dict = {}

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

                user_dict[userid] = contact_list

            else:
                line[1] = line[1].split(',')
                groupid = line[0]
                member_list = []
                for member in line[1]:
                    member_list.append(member)

                group_dict[groupid]=member_list
            
    file.close()
    return (user_dict,group_dict)

    # for group in group_list:
    #     print( group.get_groupid())
    #     for y in group.get_member_list():
    #         print(y+", ",end='')
    #     print()
    
from tkinter import *

from matplotlib.pyplot import text 
root = Tk()
app_font = ("Helvetica",13)

data = read_file()


class Welcome(Frame):
     def __init__(self,master=None):
        super().__init__(master,background="thistle4")
        self.master = master
        self.grid(row=0,column=0,sticky="nsew")
        self.label = Label(self,bg="thistle4",text= "WELCOME TO PYTHON SOCIAL NETWORKING APP",font=("Helvetica",16))
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)


class UserMenu(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=1,column=0,sticky="nsew")
        self.userid = ""

        self.select_user_label = Label(self,text="Please select a user :",font = app_font)
        self.select_user_label.grid(row=0,column=0)

        self.options = [ userid for userid in data[0] ]
        self.clicked = StringVar() 
        self.clicked.set("None Selected")

        self.drop = OptionMenu( self, self.clicked ,*self.options ,command=self.show) 
        self.drop.config(font = app_font)
        self.drop.grid(row=0,column=1,padx=5,pady=10)

        self.choice = Label(self,text="Current Selected User: ",font=app_font)
        self.choice.grid(row=0,column=2)

        self.user = Label(self,text = "None",font = app_font)
        self.user.grid(row=0,column=3)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)

    def show(self,event): 
        s = self.clicked.get()
        self.user.config(text = s)
        self.userid = s

    def get_userid(self):
        return self.userid

class Features(Frame):
    def __init__(self,master=None,display = None):
        super().__init__(master)
        self.master = master
        self.display = display
        self.grid(row=2,sticky="ew",pady=(0,0))

        grid_config_dict = {'row':0,'padx':0,'pady':(0,0),'sticky':"nsew"}
        self.button1 = Button(self,text="Incoming Messages",font=app_font)
        self.button1.grid(grid_config_dict,column=0)
        self.button2 = Button(self,text="Your Contacts",font=app_font,command=self.display.get_contacts)
        self.button2.grid(grid_config_dict,column=1)
        self.button3 = Button(self,text="Your Groups",font=app_font)
        self.button3.grid(grid_config_dict,column=2)
        self.button4 = Button(self,text="Post Something",font=app_font)
        self.button4.grid(grid_config_dict,column=3)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)

class Display(Frame):
    def __init__(self,master=None,usermenu=None):
        super().__init__(master,background="cyan")
        self.master = master
        self.grid(row=3,column=0,sticky="nsew")
        self.usermenu = usermenu

        self.label = Label(self,text="")
        self.label.place(relx=0.5,rely=0.5,anchor=CENTER)

    def get_contacts(self):
        userid = self.usermenu.get_userid()
        s = ""   
        for contact in data[0][userid]:
            s += (contact + "\n")
        self.label.config(text=s)
        

    def get_commands(self):
        return [self.get_contacts]






class App(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('1000x800')
        self.master.title('Social Network')
        
        self.master.grid_rowconfigure(0,weight = 1,uniform = "row_unity")
        self.master.grid_rowconfigure(1,weight = 1,uniform = "row_unity")
        self.master.grid_rowconfigure(2,weight = 1,uniform = "row_unity")
        self.master.grid_rowconfigure(3,weight = 7,uniform = "row_unity")

        self.master.grid_columnconfigure(0,weight = 1)
        # self.master.grid_columnconfigure(1,weight = 1,uniform = "column_uniform")
        # self.master.grid_columnconfigure(2,weight = 1,uniform = "column_uniform")
        # self.master.grid_columnconfigure(3,weight = 1,uniform = "column_uniform")

        self.welcome = Welcome(self.master)
        self.usermenu = UserMenu(self.master)
        self.display = Display(self.master,self.usermenu)
        self.features = Features(self.master,self.display)

app = App(root)
# # root.config(menu=app.menubar.user_menubar)
# root.mainloop()

# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


root.mainloop()
    