from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:/Programming - Python/VS Code/COM404/2-guis/4-images/images/ambulance.gif")
        self.bike_image = PhotoImage(file="U:/Programming - Python/VS Code/COM404/2-guis/4-images/images/bike.gif")
        self.plane_image = PhotoImage(file="U:/Programming - Python/VS Code/COM404/2-guis/4-images/images/plane.gif")
        
        # set window attributes
        self.title("Transport")
        
        # add components
        self.add_main_frame()
        self.add_heading_label()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()

    
    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.grid(row=0, column=0)

    def add_heading_label(self):
        self.heading_label = Label(self.main_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(font="Arial 15",
                                 text="Transport")
        
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label(self.main_frame)
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def add_bike_image_label(self):
        self.bike_image_label = Label(self.main_frame)
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image,
                                             height=60,
                                             width=60)
 
    def add_plane_image_label(self):
        self.plane_image_label = Label(self.main_frame)
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image,
                                             height=60,
                                             width=60)
