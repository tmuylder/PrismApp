from tkinter import *

# First the root widget which is basically the box
root = Tk()


def myClick():
    Success = Label(root, text="Data transformed, check the new excel file")
    Success.pack()

# First define a new widget 
myTitle = Label(root, text = "Prism Reformatter")
# Secondly pack the widget and put it in the root widget
myLabel.pack()



# Convert button
myButton = Button(root, text = "Convert", padx=50, command=myClick)

root.mainloop()