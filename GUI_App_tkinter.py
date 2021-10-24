#______________________________Starter Code__________________________
# To import tkinter module :-
import tkinter as tk
from tkinter import Checkbutton, StringVar, ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title("GUI App")


#____________________________Create Labels___________________________
name_label = ttk.Label(win, text="Enter your name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="Enter your age : ")
age_label.grid(row=1, column=0, sticky=tk.W)
 
email_label = ttk.Label(win, text="Enter your email : ")
email_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text="Select your gender : ")
gender_label.grid(row=3, column=0, sticky=tk.W)

#___________________________Create EntryBox__________________________
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=20, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

age_var = tk.IntVar()
age_entrybox = ttk.Entry(win, width=20, textvariable=age_var)
age_entrybox.grid(row=1, column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=20, textvariable=email_var)
email_entrybox.grid(row=2, column=1)

#___________________________Create ComboBox__________________________
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=17, textvariable=gender_var,state="readonly")
gender_combobox["values"] = ("Male", "Female", "Others")
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

#__________________________Create radiobutton________________________
radiobtn_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text="Student", value="Student",variable=radiobtn_var)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text="Teacher", value="Teacher",variable=radiobtn_var)
radiobtn2.grid(row=4, column=1)

#_________________________Create CheckButton_________________________
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text="Check if you want to subscribe to our newsletter", variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


#_________________________Create Submit Button_______________________
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    usergender = gender_var.get()
    userradiobtn = radiobtn_var.get()
    if checkbtn_var.get() == 1:
        subscribed = "Yes"
    else:
        subscribed = "No"
#     print(f"{username} is {userage} years old, {useremail}")
#     print(f"{usergender}, {userradiobtn}, {subscribed}")

#     with open("file.txt","a") as f:
#         f.write(f"{username},{userage}.{useremail},{usergender},{userradiobtn},{subscribed}\n")

#___________________________CSV File_________________________________

    with open("file.csv","a") as f:
        dict_writer = DictWriter(f, fieldnames=["UserName", "UserAge", "User Email Id", "User Gender", "User Radio Button", "Subscribed"])

        if os.stat("file.csv").st_size == 0:
            dict_writer.writeheader()
            
        dict_writer.writeheader()
        dict_writer.writerow({
            "UserName" : username,
            "UserAge" : userage,
            "User Email Id" : useremail,
            "User Gender" : usergender,
            "User Radio Button" : userradiobtn,
            "Subscribed" : subscribed
        })

    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
#     submit_button.configure(foreground="Blue")

submit_button = tk.Button(win, text="Submit", command=action)
submit_button.grid(row=6, column=0)

win.mainloop()
