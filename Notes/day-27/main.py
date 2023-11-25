from tkinter import *

#Create a window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

 
#Label
my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

#Change if needed
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_2 = Button(text="Click Me", command=button_clicked)
# button.pack()
button_2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
print(input.get())

#Keep window open
window.mainloop()