from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 20",
                                 text="Entrance Ticket")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(font = "Arial 15", text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0)
                
    def __add_buy_button(self):
        #create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)
        #style
        self.buy_button.configure(text="Submit")
        #events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        no_of_tickets = int(self.tickets_entry.get())
        
        if no_of_tickets==1:
            messagebox.showinfo("Purchased!","You have purchased 1 ticket")
        elif no_of_tickets>1:
            messagebox.showinfo("Purchased!","You have purchased " + str(no_of_tickets) +" tickets")
        else: 
            messagebox.showinfo("Invalid","You have entered an invalid number of tickets!")
        