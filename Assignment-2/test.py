from tkinter import *
from ast import literal_eval
import numpy as np

class LeftFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master,bg="green")
        self.master = master
        self.grid(row=0, column=0,sticky=S+N+E+W)
        master.grid_columnconfigure(0,weight=1)
        master.grid_rowconfigure(0,weight=1)
        self.textbox = Text(self,width=50,height=20,padx=10,pady=10,bd=5)
        self.textbox.insert(END,"enter your expression and value of variable")
        self.textbox.grid(row=0,column=0,sticky=S+N+E+W)

    def insert(self, ins_string):
        textbox.insert(END,ins_string)



class RightFrame(Frame):
    def __init__(self, master=None,lframe=None):
        Frame.__init__(self, master,bg="red")
        self.master = master
        self.lframe = lframe
        self.grid(row=0, column=1,sticky=S+N+E+W)
        master.grid_columnconfigure(1,weight=1)

        self.lab1 = Label(self,text="Expression (variable x): ")
        self.lab1.grid(row=0,column=0)

        self.exprtext = Text(self,width=40,height=2,padx=10,pady=20)
        self.exprtext.insert(END, "expr")
        self.exprtext.grid(row=0,column=1,columnspan=2)

        self.lab2 = Label(self, text="Variable Range (a,b): ")
        self.lab2.grid(row=1, column=0)

        self.variablevalue = Text(self,width=10,height=2,padx=2,pady=20)
        self.variablevalue.insert(END, "value")
        self.variablevalue.grid(row=1,column=1)


        self.evaluatebutton = Button(self,text="Evaluate !",command=self.evaluate,width=10,height=2,padx=2,pady=20)
        self.evaluatebutton.grid(row=2, column=1)

        self.exitbutton = Button(self, text="Exit", command=exit, width=5, height=2, padx=2, pady=20)
        self.exitbutton.grid(row=2, column=2)

    def evaluate(self):
        expr=self.exprtext.get(1.0,END)
        print(expr)
        varval=self.variablevalue.get(1.0,END)
        print(varval)
        a=literal_eval(varval)
        self.lframe.textbox.delete(1.0,END)
        print(a)
        for x in np.linspace(a[0],a[1],10):
            expr=expr.strip('\n')
            y=eval(expr)
            print(expr+' ( '+str(x)+' ) '+' = '+str(y))
            self.lframe.textbox.insert(END,expr+' ( '+str(x)+' ) '+' = '+str(y)+'\n')



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.geometry("1000x600")
        self.leftframe = LeftFrame(master)
        self.rightframe = RightFrame(master,self.leftframe)
        master.wm_title("expression calculator")
        self.grid(row=0,column=0,sticky="nsew")


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
#root.wm_title("Tkinter window")

# show window
root.mainloop()