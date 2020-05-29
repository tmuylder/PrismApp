from tkinter import *

# First the root widget which is basically the box
root = Tk()

i = Entry(root, width=50, borderwidth=3)
i.pack()

v = Entry(root, width=50, borderwidth=3)
v.pack()

o = Entry(root, width=50, borderwidth=3)
o.pack()

def myClick():
    myInputSheet = i.get()
    myVariable = v.get()
    myOutputName = o.get()
    Success = Label(root, text="Transformed Excel sheet: " + myInputSheet + ".\nExtracted the variable: " + myVariable + ".\nNew format in: " + myOutputName + ".xlsx")
    Success.pack()



# First define a new widget 
myTitle = Label(root, text = "Prism Reformatter")
# Secondly pack the widget and put it in the root widget
myTitle.pack()



# Convert button
myButton = Button(root, text = "Convert", padx=50, command=myClick)
myButton.pack()

root.mainloop()