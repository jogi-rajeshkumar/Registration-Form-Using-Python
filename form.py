from tkinter import *
root = Tk()
root.geometry("600x400")

def getvals():
    print("Accepted")


# Heading
Label(root, text="Registration Form", font="ar 30 bold").grid(row=0,column=6)

# Field Name
name = Label(root, text="Name", font="ar 15")
phone = Label(root, text="Phone", font="ar 15")
gender = Label(root, text="Gender", font="ar 15")
address = Label(root, text="Address", font="ar 15")
paymentmode = Label(root, text="Payment Mode", font="ar 15")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
address.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Variable for Storing Data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
addressvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

# Creating Entry Field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
addressentry = Entry(root, textvariable =addressvalue)
paymentmodeentry = Entry(root, textvariable =paymentmodevalue)

# packing Entry Field
nameentry.grid(row=1, column=6)
phoneentry.grid(row=2, column=6)
genderentry.grid(row=3, column=6)
addressentry.grid(row=4, column=6)
paymentmodeentry.grid(row=5, column=6)

# Create Checkbox
checkbtn = Checkbutton(text="Remember me?", variable = checkvalue, font="ar 10")
checkbtn.grid(row=6, column=6)

#Submit Button
Button(text="Submit", command=getvals).grid(row=7, column=6)

root.mainloop()