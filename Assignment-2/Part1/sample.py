from tkinter import *
from ast import literal_eval
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 

heading_font = ("Arial",16)
app_font = ("Helvetica",13) 

root = Tk()
root.configure(background='thistle4')


class LeftFrame(Frame):
    def __init__(self,master=None,drawing_frame = None):
        super().__init__(master,bg="salmon")
        self.master=master
        self.grid(row=0,column=0,sticky="nsew",padx=50,pady=75)
        self.drawing_frame = drawing_frame

        self.header = Label(self,text="PLOT YOUR FUNCTION",font=heading_font,highlightcolor="black",highlightthickness=4,highlightbackground="black",padx=5,pady=5)
        self.header.grid(row=0,column=0,columnspan=2,pady=50)

        self.expr = Label(self,text = "Enter an expression of variable x:",font=app_font) 
        self.expr.grid(row=1,column=0,padx = 5,pady = 10)
        self.expression = Text(self,height=2,width=20,font=app_font)
        self.expression.grid(row=1,column=1,padx = 5,pady = 20)

        self.lb = Label(self,text = "Enter Lower Bound of Iteration : ",font=app_font)
        self.lb.grid(row=2,column=0,padx=5,pady=10)
        self.lbound = Text(self,height=2,width=20,font=app_font)
        self.lbound.grid(row=2,column=1,padx = 5,pady = 20)

        self.ub = Label(self,text = "Enter Upper Bound of Iteration : ",font=app_font)
        self.ub.grid(row=3,column=0,padx=5,pady=10)
        self.ubound = Text(self,height=2,width=20,font=app_font)
        self.ubound.grid(row=3,column=1,padx = 5,pady = 20)

        self.button = Button(self,text = "Create Plot",command=self.draw_plot,font=app_font,fg="white",bg="black",highlightcolor="white",highlightthickness=4,highlightbackground="purple1",padx=5,pady=5)
        self.button.grid(row=4,column=0,padx=15,pady=20,columnspan=2)  


    def draw_plot(self):
        formula = self.expression.get(1.0,END)
        formula = formula.strip('\n')
        a = literal_eval(self.lbound.get(1.0,END))
        b = literal_eval(self.ubound.get(1.0,END))

        x = np.linspace(a,b,20)
        mydict = {'x':x}
        y = eval(formula,mydict)

        
        fig = plt.figure(num=1)
        fig.clf()
        plt.plot(x,y,'o-')
        plt.xlabel('Value of x')
        plt.ylabel('Value of y')
        title = "Plot of y = "+formula+" in the range ["+str(a)+","+str(b)+"]"
        plt.title(title)

        canvas = FigureCanvasTkAgg(fig, master=self.drawing_frame)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row = 0,column=0)
        

class RightFrame(Frame):
    def __init__(self,master=None):
        super().__init__(master,background='white')
        self.master=master
        self.grid(row=0,column=1,sticky="nsew",padx=50,pady=75)


class Window(Frame):
    def __init__(self,master=None):
        super().__init__(master)

        master.title('Matplotlib Plotter GUI')
        master.geometry('1400x800')

        master.grid_rowconfigure(0,weight=1)
        master.grid_columnconfigure(0,weight=1,uniform='group1')
        master.grid_columnconfigure(1,weight=1,uniform='group1')

        self.rframe = RightFrame(master)
        self.lframe = LeftFrame(master,self.rframe)

gui_window = Window(root)

root.mainloop()

