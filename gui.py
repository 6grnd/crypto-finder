from tkinter import * 
# connect my crypto class to the tkinter interface. 
from connectToCurrencies import currencyScraper

class App(Tk):
    def __init__(self): 
        Tk.__init__(self) 
        self._frame = None
        self.switch_frame(mainGUI)
    
    def switch_frame(self, frame_class): 
        new_frame = frame_class(self) 
        if self._frame is not None: 
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()



class mainGUI(Frame, currencyScraper): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        self.cryptoSelection = Label(master, text="Choose Crypto: ", font=("Arial Bold", 20))
        self.cryptoSelection.grid()

        self.cryptoEntry = StringVar()
        self.cryptoEntry = Entry(textvariable=self.cryptoSelection)
        self.cryptoEntry.grid()

        def buttonClick(): 
            print("You pressed Submit!")
            print("You chose: " + self.cryptoEntry.get())
            # And then delete the past entry. 
            self.cryptoEntry.delete(0, "end")

        self.submitButton = Button(master, text="Submit", command=buttonClick)
        self.submitButton.grid()

class PageOne(Frame): 
    def __init__(self, master): 
        Frame.__init__(self, master) 
        Frame.configure(self, bg="yellow")
        Label(self, text="Page one", font=("Arial Bold", 20)).pack(side="top", fill="x", pady=5)
        #Button(text="Information", command=lambda: master.switch_frame(PageA)).pack())
        #Button(text="Information", command=lambda: master.switch_frame(PageB)).pack())
        #Button(text="Information", command=lambda: master.switch_frame(PageC)).pack())

class PageA(Frame): 
    pass

class PageB(Frame): 
    pass

class PageC(Frame): 
    pass



if __name__ == "__main__": 
    # TODO: program not printing anything when run. 
    app = App()
    app.mainloop()