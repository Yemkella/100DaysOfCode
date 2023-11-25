from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.get()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    output_label.config(text=km)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()