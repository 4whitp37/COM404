from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="U:/Programming - Python/VS CODE/COM404/2-guis/5-animation/images/ball.gif")
        self.greenball_image = PhotoImage(file="U:/Programming - Python/VS CODE/COM404/2-guis/5-animation/images/greenball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 250
        self.ball_y_pos = 100
        self.ball_x_change = 3
        self.ball_y_change = 3

        self.greenball_x_pos = 150
        self.greenball_y_pos = 100
        self.greenball_x_change = -2
        self.greenball_y_change = 2

        
        # add components
        self.add_ball_image_label()
        self.add_greenball_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        #whiteball tick
        if self.ball_x_pos > 450:
            self.ball_x_change = -1
        if self.ball_y_pos > 450:
            self.ball_y_change = -1
        if self.ball_x_pos < 0:
            self.ball_x_change = 1
        if self.ball_y_pos < 0:
            self.ball_y_change = 1            
       
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change

        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        self.after(100, self.tick)

        #greenball tick

        if self.greenball_x_pos > 450:
            self.greenball_x_change = -1
        if self.greenball_y_pos > 450:
            self.greenball_y_change = -1
        if self.greenball_x_pos < 0:
            self.greenball_x_change = 1
        if self.greenball_y_pos < 0:
            self.greenball_y_change = 1            
       
        self.greenball_x_pos = self.greenball_x_pos + self.greenball_x_change

        self.greenball_y_pos = self.greenball_y_pos + self.greenball_y_change
        self.greenball_image_label.place(x=self.greenball_x_pos, 
                                    y=self.greenball_y_pos)
        self.after(100, self.tick)

    # the whiteball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)


    # the greenball image
    def add_greenball_image_label(self):
        self.greenball_image_label = Label()
        self.greenball_image_label.place(x=self.greenball_x_pos,
                                    y=self.greenball_y_pos)
        self.greenball_image_label.configure(image=self.greenball_image)
     
