from tkinter import *
from  tkinter import filedialog
from functions import *

# First the root widget which is basically the box
root = Tk()
root.configure(background='white')

# Set app width and height
canvas = Canvas(root, height=500, width=550)
canvas.grid()

# First define a new widget 
myTitle = Label(root, text = "Prism Reformatter", font=("Open Sans", 18), bg='white')
# Secondly pack the widget and put it in the root widget
myTitle.grid(row=0)

#################################
# Three inputs for the function #
#################################

# Find Excel file
def open_excel_file():
    root.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("excel file","*.xlsx"),("all files","*.*")))
    fileButtonText = Label(root, text=(root.filename))
    fileButtonText.grid(row=1, column=1)

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


#####################
# Call the function #
#####################

def myClick():
    myInputSheet = root.filename
    myVariable = v.get()
    myOutputName = o.get()

    plant_data_prism(myInputSheet, myVariable, myOutputName)

    Success = Label(root, text="Transformed Excel sheet: " + root.filename + ".\nExtracted the variable: " + myVariable + ".\nNew format in: " + myOutputName + ".xlsx\n Done...")
    Success.grid(row=5)

# Convert button
myButton = Button(root, text = "Convert", padx=50, command=myClick)
myButton.grid(row=4)

root.mainloop()