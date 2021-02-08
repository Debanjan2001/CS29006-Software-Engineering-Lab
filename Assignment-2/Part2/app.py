from tkinter import *   
from PIL import ImageTk,Image
from tkinter import filedialog,messagebox


root = Tk()
app_font = ("Fixedsys",13)
heading_font = ("Fixedsys",20,'bold')

def read_file():

    file = open("social_network.txt",'r')
    # print("File name: "+file.name)
    hash_cnt = 0
    user_dict= {}
    group_dict = {}
    messages_dict = {}
    posts_dict = {}
    user_groups = {}

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
                messages_dict[userid] = []
                posts_dict[userid] = []
                user_groups[userid] = []

            else:
                line[1] = line[1].split(',')
                groupid = line[0]
                member_list = []
                for member in line[1]:
                    member_list.append(member)
                    user_groups[member].append(groupid)

                group_dict[groupid]=member_list
            
    file.close()

    #Messages
    file = open("messages.txt",'r')
    for msg_to in file:
        msg_from = file.readline().strip('\n')
        msg = file.readline().strip('\n')
        photofile = file.readline().strip('\n')
        msg_to = msg_to.strip('\n')
        print([msg_from,msg,photofile])
        messages_dict[msg_to].append([msg_from,msg,photofile])

    file.close()

    return [user_dict,group_dict,messages_dict,user_groups]


def update_message():
    file = open("messages.txt",'w')
    for user in data[2]:
        for obj in data[2][user]:
            if len(obj)==0:
                break
            file.write(user+"\n")
            file.write(obj[0]+"\n")
            file.write(obj[1]+"\n")
            file.write(obj[2]+"\n")
    file.close()



data = read_file()

class Welcome(Frame):
     def __init__(self,master=None):
        super().__init__(master,background="thistle4")
        self.master = master
        self.grid(row=0,column=0,sticky="nsew")
        self.label = Label(self,bg="thistle4",text= "WELCOME TO PYTHON SOCIAL NETWORKING APP",font=heading_font)
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)


class UserMenu(Frame):
    def __init__(self,master=None,display = None):
        super().__init__(master,bg="coral")
        self.master = master
        self.display = display
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
        self.display.clear_display()
        self.msg = Label(self.display,text="Hello {}!! You can check messages or,\nCheck your contacts and groups or,\nPost something".format(s),font=heading_font)
        self.msg.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.display.userid = s

class Features(Frame):
    def __init__(self,master=None,commands=None):
        super().__init__(master,bg="palegreen4")
        self.master = master
        self.commands = commands
        self.grid(row=2,sticky="nsew",pady=(0,0))

        button_config = {'font':app_font,'bg':"black",'fg':"white"}
        grid_config_dict = {'row':0,'padx':0,'pady':(0,0),'sticky':"ew"}
        self.button1 = Button(self,button_config,text="Incoming Messages",command=self.commands['messages'])
        self.button1.grid(grid_config_dict,column=0)
        self.button2 = Button(self,button_config,text="Your Contacts",command=self.commands['contacts'])
        self.button2.grid(grid_config_dict,column=1)
        self.button3 = Button(self,button_config,text="Your Groups",command=self.commands['groups'])
        self.button3.grid(grid_config_dict,column=2)
        self.button4 = Button(self,button_config,text="Post Something",command=self.commands['post'])
        self.button4.grid(grid_config_dict,column=3)

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)

class Display(Frame):
    def __init__(self,master=None):
        super().__init__(master,bg="chocolate1")
        self.master = master
        self.grid(row=3,column=0,sticky="nsew")
        self.userid = ""
        
      
    def clear_display(self):
        for widget in self.winfo_children():
            widget.destroy()

        
    def get_messages(self):
        self.clear_display()
        
        userid = self.userid

        self.grid_columnconfigure(0,weight=2)
        
        msg_frame = Frame(self,bg="white")
        msg_frame.grid(row=0,column=0,sticky="nsew",padx=100,pady=20)
        msg_frame.grid_columnconfigure(0,weight=1)
        msg_frame.grid_columnconfigure(1,weight=4)
        msg_frame.grid_columnconfigure(1,weight=4)


        messages = data[2][userid]
        
        for cnt,msg in enumerate(reversed(messages)):
            msg_from = msg[0]
            msg_txt = msg[1]
            imgfile = msg[2]
            img = None
            serial = Label(msg_frame,text=str(cnt+1),font=app_font)
            serial.grid(row=cnt,column=0,padx=5,pady=5,sticky="nsew")
            
            showtxt = Label(msg_frame,text="Sent by:"+msg_from+"\n"+"Message: "+msg_txt+" ",font=app_font)
            showtxt.grid(row=cnt,column=1,padx=5,pady=5,sticky="nsew")

            if imgfile != "NULL":
                img = Image.open(imgfile)
                img = img.resize((200, 125), Image.ANTIALIAS) 
                img = ImageTk.PhotoImage(img) 

            if img is not None:
                panel = Label(msg_frame, image = img,pady=5) 
                panel.image = img 
                panel.grid(row = cnt,column=2,padx=10,pady=5,sticky="wnse")
            else:
                panel = Label(msg_frame,text="NO IMAGE",font=app_font) 
                panel.grid(row = cnt,column=2,padx=10,pady=5,sticky="wens")


        if len(messages) == 0:
            panel = Label(msg_frame,text="NO MESSAGES",font=app_font) 
            panel.grid(row = 0,column=0,columnspan=3,padx=10,pady=5,sticky="we")
        

    def get_contacts(self):
        self.clear_display()
        self.grid_columnconfigure(0,weight=1)


        userid = self.userid

        msg_frame = Frame(self,bg="white")
        msg_frame.grid(row=0,column=0,sticky="nsew",padx=100,pady=20)
        msg_frame.grid_columnconfigure(0,weight=1,uniform="col_uniform")
        msg_frame.grid_columnconfigure(1,weight=4,uniform="col_uniform")


        friends = data[0][userid]
        for cnt,fr in enumerate(friends):
            serial = Label(msg_frame,text=str(cnt+1),font=app_font)
            serial.grid(row=cnt,column=0,padx=5,pady=5,sticky="nsew")
            
            showtxt = Label(msg_frame,text=fr,bg="white",font=app_font)
            showtxt.grid(row=cnt,column=1,padx=5,pady=5,sticky="nsw")



    def get_groups(self):
        self.clear_display()
        self.grid_columnconfigure(0,weight=1)
        

        userid = self.userid

        msg_frame = Frame(self,bg="white")
        msg_frame.grid(row=0,column=0,sticky="nsew",padx=100,pady=20)
        msg_frame.grid_columnconfigure(0,weight=1,uniform="col_uniform")
        msg_frame.grid_columnconfigure(1,weight=4,uniform="col_uniform")


        groups = data[3][userid]
        for cnt,g in enumerate(groups):
            serial = Label(msg_frame,text=str(cnt+1),font=app_font)
            serial.grid(row=cnt,column=0,padx=5,pady=5,sticky="nsew")
            
            showtxt = Label(msg_frame,text=g,bg="white",font=app_font)
            showtxt.grid(row=cnt,column=1,padx=5,pady=5,sticky="nsw")



    def create_post(self):
        self.clear_display()
        userid = self.userid

        self.option_frame = Frame(self,bg="cadet blue")
        self.option_frame.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
        self.message_frame = Frame(self,bg="cadet blue")
        self.message_frame.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)

        self.option_frame.grid_columnconfigure(0,weight=2,uniform = "col_uniform")
        self.option_frame.grid_columnconfigure(1,weight=1,uniform="col_uniform")

        self.message_frame.grid_columnconfigure(0,weight=1,uniform = "col_uniform")
        self.message_frame.grid_columnconfigure(1,weight=1,uniform="col_uniform")


        self.grid_rowconfigure(0,weight = 2)
        self.grid_rowconfigure(1,weight = 8)
        self.grid_columnconfigure(0,weight = 1)

        label1 = Label(self.option_frame,text="Okay {},Select a friend/group to post:".format(userid),font=app_font)
        label1.grid(row=0,column=0,pady=10,padx=10,sticky="nsew")

        self.options =[]
        self.clicked = StringVar() 
        self.clicked.set("None Selected")
        
        for contact in data[0][userid]:
            self.options.append(contact)
        
        for group in data[3][userid]:
            self.options.append(group)

        self.post_to = ""
        def id_post(event): 
            s = self.clicked.get()
            self.post_to = s
            print(s)
            return s

        drop = OptionMenu(self.option_frame, self.clicked ,*self.options ,command=id_post) 
        drop.config(font = app_font)
        drop.grid(row=0,column=1,padx=5,pady=10)

        msglabel = Label(self.message_frame,text="Enter your message to post :",font=app_font)
        msglabel.grid(row=0,column=0,padx=10,pady=20)
        message = Text(self.message_frame,font=app_font,height = 5,width = 30)
        message.grid(row=1,column=0,padx=30,pady=20)

        self.msg = "NULL"
        self.photofile = "NULL"

        def openfilename(): 
            # open file dialog box to select image 
            # The dialogue box has a title "Open" 
            filename = filedialog.askopenfilename(title ='Open') 
            print(filename)
            self.photofile = filename
            return filename 
        
        def open_img(): 
            file = openfilename() 
            img = Image.open(file) 
            # resize the image and apply a high-quality down sampling filter 
            img = img.resize((350, 200), Image.ANTIALIAS) 
            # PhotoImage class is used to add image to widgets, icons etc 
            img = ImageTk.PhotoImage(img) 
            # create a label 
            panel = Label(self.message_frame, image = img) 
            panel.image = img 
            panel.grid(row = 2,column=1,columnspan=3,padx=10,pady=5)

        imglabel = Label(self.message_frame,text="Select an image to post(Optional) :",font=app_font)
        imglabel.grid(row=0,column=1,padx=10,pady=20)
        image = Button(self.message_frame, text ='Upload image', command = open_img,font=app_font)
        image.grid(row = 1, column = 1,padx=10,pady=5)


        def post():
            self.msg = message.get(1.0,END).strip('\n')
            self.photofile = self.photofile.strip('\n')
            if self.post_to != "" and self.msg != "":
                if self.post_to in data[0]:
                    data[2][self.post_to].append([self.userid,self.msg,self.photofile])
                elif self.post_to in data[1]:
                    for user in data[1][self.post_to]:
                        if user!=self.userid:
                            data[2][user].append([self.userid + " in "+self.post_to+ " group",self.msg,self.photofile])

                print("posted")
                messagebox.showinfo("Message", "Successfully Posted") 
                self.create_post()
            else:
                messagebox.showinfo("Message", "Error!Empty Message or No user Selected!") 
           
        submit = Button(self.message_frame,text="Post",command=post,font=app_font)
        submit.grid(row=2,column=0,padx=10,pady=5)



    def get_commands(self):
        commands = {'contacts':self.get_contacts,'messages':self.get_messages,
        'groups':self.get_groups,'post':self.create_post} 
        
        return commands
 

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
        
        self.display = Display(self.master)
        self.welcome = Welcome(self.master)
        self.usermenu = UserMenu(self.master,self.display)
        commands = self.display.get_commands()
        self.features = Features(self.master,commands)


app = App(root)

root.mainloop()

update_message()
        