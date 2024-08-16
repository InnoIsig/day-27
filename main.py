from tkinter import *


#Button
def click_button():
    print("I got click something")
    new_text = my_Entry_input.get()
    my_label.config(text=new_text)

    
#Tk
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#label
my_label = Label(text="I am label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New text"
my_label.config(text="New text")




my_button = Button(text="Click me", command=click_button)
my_button.pack()

#Entry
my_Entry_input = Entry(width=10)
my_Entry_input.pack()
print(my_Entry_input.get())












window.mainloop()