from tkinter import *

window  = Tk()
window.title("KM to Miles")
window.minsize(width=350, height=300)
window.config(padx=50,pady=50)

def cal():
    val=entry1.get()
    label_3.config(text=int(val)*1.609)
entry1 = Entry(width=5)
entry1.grid(row=0, column=1)
label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)
label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)
label_3 = Label(text="0")
label_3.grid(row=1, column=1)
label_4= Label(text="Km")
label_4.grid(row=1, column=2)
button = Button(text="Calculate", command=cal)
button.grid(row=2, column=1)









window.mainloop()
