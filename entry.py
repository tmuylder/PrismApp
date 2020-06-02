from tkinter import *
from  tkinter import filedialog
from functions import *

# First the root widget which is basically the box
root = Tk()
#root.configure(background='white')

# Set app width and height
canvas = Canvas(root, height=600, width=750)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

# First define a new widget 
myTitle = Label(frame, text = "Prism Reformatter", font=("Open Sans", 18), bg='white')
# Secondly pack the widget and put it in the root widget
myTitle.place(relx = 0.1, rely = 0.1, relheight=0.1, relwidth=0.8)

myInformationText="""
This program reformats an Excel file with experimental data in a format required for input in Prism.
Please read the manual here: https://github.com/tmuylder/PrismApp.  
"""
myInfo = Label(frame, text = myInformationText, justify=LEFT, font=('Open Sans', 10), bg='white')
myInfo.place(relx=0.1, rely=0.2, relheight=0.1)

#################################
# Three inputs for the function #
#################################

# Find Excel file
def open_excel_file():
    root.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("excel file","*.xlsx"),("all files","*.*")))
    fileButtonText = Label(frame, text="Selected file: {}".format((root.filename)), bg='white')
    fileButtonText.place(relx=0.4, rely=0.4)

# Display the button to select a file    
fileButton = Button(frame, text="Select a file", command=open_excel_file)
fileButton.place(relx=0.1, rely=0.4)


# Box for the variable
variableText = Label(frame, text="Type the name of the variable: ", bg='white')
variableText.place(relx = 0.1, rely = 0.5)
v = Entry(frame, width=50, borderwidth=3)
v.place(relx=0.4, rely=0.5)

# Box for the name of the excel file
NameOutputText = Label(frame, text="Type the name of the output file: ", bg='white')
NameOutputText.place(relx = 0.1, rely=0.6)
o = Entry(frame, width=50, borderwidth=3)
o.place(relx = 0.4, rely=0.6)


#####################
# Call the function #
#####################

def myClick():
    myInputSheet = root.filename
    myVariable = v.get()
    myOutputName = o.get()

    plant_data_prism(myInputSheet, myVariable, myOutputName)

    Success = Label(root, text="Transformed Excel sheet: " + root.filename + ".\nExtracted the variable: " + myVariable + ".\nNew format in: " + myOutputName + ".xlsx\n Done...", justify=LEFT, font=('Open Sans', 10), bg='white')
    Success.place(relx=0.1, rely= 0.85)

# Convert button
myButton = Button(frame, text = "Convert", padx = 100, command=myClick)
myButton.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()