from tkinter import *

class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Newletter")
    self.configure(bg="#4682B4",
                   height=250, 
                   width=400)

    self.add_heading_label()
    self.add_sub_heading_label()
    self.add_email_label()
    self.add_email_entry()
    self.add_button()

  def add_heading_label(self):
      # create
     self.heading_label = Label()
     #self.bg="#4682B4"
     self.heading_label.place(x=35, y=5)
      # ...setting the attributes of the component using the attribute
     self.heading_label.configure(bg="#4682B4",font="Arial 25",
                                 text="Receive our newsletter")

  def add_sub_heading_label(self):
    self.sub_heading_label = Label()
    self.sub_heading_label.place(x=40, y=50)
    self.sub_heading_label.configure(bg="#4682B4",font="Arial 8",
                                 text="Please enter your email address below to receive our newsletter")
    
  def add_email_label(self):
    self.email_label = Label()
    self.email_label.place(x=40, y=120)
    self.email_label.configure(bg="#4682B4",font="Arial 8",
                                 text="Email:")  
    
  def add_email_entry(self):
    self.email_entry = Entry()
    self.email_entry.place(x=80, y=120)
    self.email_entry.configure(width=45)

  def add_button(self):
    self.button = Button()
    self.button.place(x=160, y=180)
    self.button.configure(text="Subscribe")
  

  # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)