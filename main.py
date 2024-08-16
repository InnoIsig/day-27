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
window.config(padx=100, pady=200)

#label
my_label = Label(text="I am label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)





my_button = Button(text="Click me", command=click_button)
my_button.grid(column=1, row=1)
new_button = Button(text="New buttom")
new_button.grid(column=2, row=0)


#Entry
my_Entry_input = Entry(width=10)
my_Entry_input.grid(column=3, row=2)
print(my_Entry_input.get())




window.mainloop()