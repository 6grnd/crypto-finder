from tkinter import * 
#from main import * 
window = Tk() 
color = "yellow"
# appears at the top of the screen. 
window.title("Cryto Scraper | PonyKillerMX")
window.configure(bg=color)
# size of window when it is first shown. 
window.geometry("300x100") 

main_label = Label(window, text="Choose Crypto:", font=("Arial Bold", 20), bg=color)
main_label.place(x=75, y=0)

#entry where user inputs name of crypto  
main_entry = Entry(window, width=32, highlightthickness=4)
main_entry.place(x=0, y=30)
main_entry.focus()

main_button = Button(window, text="Enter") # missing a command = x 
main_button.place(x=130, y=70)


window.mainloop()