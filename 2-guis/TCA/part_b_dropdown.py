# gui.py

from tkinter import *
from tkinter import messagebox

class Gui(Tk):

        


    def __init__(self):
        super().__init__()


        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()
        self.__add_option_box_label()
        self.__add_option_box()
        self.__add_animation_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 14",
                                        text="RECEIVE OUR NEWSLETTER")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="Please enter your email below to receiver our newsletter")

    def __add_email_label(self):
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, sticky=E)
        self.email_label.configure( pady=20,
                                    text="Email:")
                                    
              

    def __add_email_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        self.email_entry.configure(width=40)
        
        
    def __add_option_box_label(self):
        self.option_box_label = Label(self.outer_frame)
        self.option_box_label.grid(row=3, column=0, sticky=E)
        self.option_box_label.configure( pady=20,
                                    text="Type")    
        
        
    def __add_option_box(self):
        global variable
        variable = StringVar()
        variable.set("Weekly")
        self.option_box = OptionMenu(self.outer_frame, variable, "Weekly", "Monthly", "Yearly")
        #self.option_box.pack
        self.option_box.grid(row=3, column=1, sticky=W)
        self.option_box.configure(width=30)
        #mainloop()
        #return variable.get()

    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=6, column=0, columnspan=2, sticky=N+E+S+W)
        self.subscribe_button.configure(bg="#fcc",
                                        text="Subscribe")
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_clicked)

    def __subscribe_clicked(self, event):
      
      email_entry = self.email_entry.get()
      #frequency = variable.get()
      
      if email_entry == '':
        messagebox.showinfo("Newsletter","Please enter your email!")
      if email_entry != '' and variable.get() == "Weekly":
        messagebox.showinfo("Newsletter","You have subscribed to the weekly newsletter! You will receive this every Monday.")
      if email_entry != '' and variable.get() == "Monthly":
        messagebox.showinfo("Newsletter","You have subscribed to the monthly newsletter! You will receive this on the first day of every month.")
      if email_entry != '' and variable.get() == "Yearly":
        messagebox.showinfo("Newsletter","You have subscribed to the yearly newsletter! You will receive this at the start of each year.")
          
    def __add_animation_button(self):
      
        global animation
        animation = StringVar()
        animation.set("Start")
        self.__animation_button = Button(self.outer_frame)
        self.__animation_button.grid(row=7, column=0, columnspan=2, sticky=N+E+S+W)
        self.__animation_button.configure(bg="#fcc",
                                        text="Start Animation")
        self.__animation_button.bind("<ButtonRelease-1>", self.__animation_clicked)
        

    def __animation_clicked(self, event):
      
      if animation.get()=="Start":
        self.__animation_button.configure(text="Stop Animation")
        global animation2
        animation2 = StringVar()
        animation2.set("Stop")
        self.__animation_button.bind("<ButtonRelease-1>", self.__animation_clicked2)
       
    def __animation_clicked2(self, event):
      if animation2.get()=="Stop":
        self.__animation_button.configure(text="Start Animation")
        animation.get()=="Start"
        self.__animation_button.bind("<ButtonRelease-1>", self.__animation_clicked)