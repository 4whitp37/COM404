from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Song Maker")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyrics_frame()
        self.__add_lyrics_entry()
        self.__add_lyrics_button()

        self.__add_lyrics_output_label()
        self.__add_lyrics_output()

        
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 20",
                                 text="Song Maker")
        
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(font = "Arial 10", text="Lyrics to add:")
       
    def __add_lyrics_frame(self):
        self.lyrics_frame = Frame()
        self.lyrics_frame.grid(row=2, column=0)
               
    def __add_lyrics_entry(self):
        self.lyrics_entry = Entry(self.lyrics_frame)
        self.lyrics_entry.pack(side=LEFT)
        #self.lyrics_entry.configure(width=45)

    def __add_lyrics_button(self):
        #create
        self.lyrics_button = Button(self.lyrics_frame)
        self.lyrics_button.pack(side=RIGHT)
        #style
        self.lyrics_button.configure(text="Add")
        #events
        self.lyrics_button.bind("<ButtonRelease-1>", self.__lyrics_button_clicked)


    def __add_lyrics_output_label(self):
        self.lyrics_output_label = Label()
        self.lyrics_output_label.grid(row=3, column=0)
        self.lyrics_output_label.configure(font = "Arial 10", text="Lyrics:")

    def __add_lyrics_output(self):
        self.lyrics_output = Entry()
        self.lyrics_output.grid(row=4, column=0)
        #self.lyrics_output.configure






    def __lyrics_button_clicked(self, event):
        pass
        #no_of_tickets = int(self.tickets_entry.get())
        
        #if no_of_tickets==1:
        #    messagebox.showinfo("Purchased!","You have purchased 1 ticket")
        #elif no_of_tickets>1:
        #    messagebox.showinfo("Purchased!","You have purchased " + str(no_of_tickets) +" tickets")
        #else: 
        #    messagebox.showinfo("Invalid","You have entered an invalid number of tickets!")
        