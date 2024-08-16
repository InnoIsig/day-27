from tkinter import *

def mils_to_km():
    miles = float(miles_Entry.get())
    km = round(miles * 1.609)
    kilometer_result_label.configgit(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_Entry = Entry(width=7)
miles_Entry.grid(column=1, row=0)

mille_label = Label(text="Miles")
mille_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=mils_to_km)
calculate_button.grid(column=1, row=2)



window.mainloop()