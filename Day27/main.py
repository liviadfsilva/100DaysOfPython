from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Miles to Kilometers Converter")

window.config(padx=20, pady=20)

#TODO: entry.
user_input = Entry(width=5)
user_input.grid(column=1, row=0)

#TODO: labels
label_1 = Label(text="Mile(s)", font=("Courier", 15, "normal"))
label_1.grid(column=2, row=0)
label_1.config(padx=5, pady=5)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)
label_2.config(padx=5, pady=5)


label_3 = Label(text="0")
label_3.grid(column=1, row=1)
label_3.config(padx=5, pady=5)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)
label_3.config(padx=5, pady=5)

def calculate():
    miles = user_input.get()
    convertion = float(miles) * 1.609
    label_3["text"] = round(convertion)

#TODO: button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)

window.mainloop()