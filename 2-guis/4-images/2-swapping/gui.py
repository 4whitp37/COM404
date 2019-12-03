from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.osprey_image = PhotoImage(file="U:/Programming - Python/VS Code/COM404/2-guis/4-images/images/osprey.gif")
        self.ospreyflip_image = PhotoImage(file="U:/Programming - Python/VS Code/COM404/2-guis/4-images/images/ospreyflip.gif")
        
        # set window attributes
        self.title("Osprey")
        
        # add components
        self.add_heading_label()
        self.add_osprey_image_label()
        self.add_flip_button()
        #self.add_flip_button_clicked()


    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 25",
                                 text="Osprey")
        
    def add_osprey_image_label(self):
        self.osprey_image_label = Label()
        self.osprey_image_label.grid(row=1, column=0)
        self.osprey_image_label.configure(image=self.osprey_image,
                                             height=400,
                                             width=400)

    def add_flip_button(self):
        #create
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        #style
        self.flip_button.configure(font="Arial 15",text="Flip",width=20)
        #events
        self.flip_button.bind("<ButtonRelease-3>", self.add_flip_button_click_left)
        self.flip_button.bind("<ButtonRelease-1>", self.add_flip_button_click_right)

    def add_flip_button_click_left(self, event):
        self.osprey_image_label.configure(image=self.ospreyflip_image)

    def add_flip_button_click_right(self, event):
        self.osprey_image_label.configure(image=self.osprey_image)
                                        
        

    