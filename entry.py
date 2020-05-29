from tkinter import *
from  tkinter import filedialog

# First the root widget which is basically the box
root = Tk()
root.configure(background='pink')


# First define a new widget 
myTitle = Label(root, text = "Prism Reformatter", font=("Open Sans", 18))
# Secondly pack the widget and put it in the root widget
myTitle.grid(row=0, column=0)

#################################
# Three inputs for the function #
#################################

# Find Excel file
def open_excel_file():
    root.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("excel file","*.xlsx"),("all files","*.*")))

# Display the button to select a file    
fileButton = Button(root, text="Select a file", command=open_excel_file)
fileButton.grid(row=1, column=0)

# Box for the variable
variableText = Label(root, text="Type the name of the variable: ")
variableText.grid(row=2, column=0)
v = Entry(root, width=50, borderwidth=3)
v.grid(row=2, column=1)

# Box for the name of the excel file
NameOutputText = Label(root, text="Type the name of the output file: ")
NameOutputText.grid(row=3, column=0)
o = Entry(root, width=50, borderwidth=3)
o.grid(row=3, column=1)


def myClick():
    #myInputSheet = i.get()   # Uncomment if you're using an Entry for the inputsheet
    myVariable = v.get()
    myOutputName = o.get()
    Success = Label(root, text="Transformed Excel sheet: " + root.filename + ".\nExtracted the variable: " + myVariable + ".\nNew format in: " + myOutputName + ".xlsx")
    Success.grid(row=5, column=0)

# Convert button
myButton = Button(root, text = "Convert", padx=50, command=myClick)
myButton.grid(row=4, column=0)

root.mainloop()