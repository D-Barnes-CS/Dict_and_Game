"""
D Barnes
Revision: 10/11/23
Begin
"""

import tkinter as tk

votingInfo = {}
votingInfo["YES"] = []
votingInfo["NO"] = []


def add_to_list():
# take input and separate it by commas then add it to a list and a dictionary. separate by YES/NO
    my_input = ent_info.get()
    separated = my_input.split(", ")

    my_info = ["You entered: " + my_input]

    for s in separated:
        if s == "YES":
            votingInfo["YES"] += my_info
        elif s == "NO":
            votingInfo["NO"] += my_info

    print(my_info)
    label2 = tk.Label(text=my_info)
    label2.pack()


window = tk.Tk()
window.title("political_poll")
window.geometry("750x450")
window.configure(bg='gray')

add_info = tk.Button(
# button to be clicked and also shows/tells user how to format their input
    master=window,
    text="Enter Voter Name, Age, Address, Contact, YES/NO on Prop 30, and Comment\n" +
         "Must Be Separated by a ',', DO NOT USE COMMA FOR ADDRESS(only spaces) ",
    command=add_to_list
)
lbl_result = tk.Label(master=window, text="results")

frm_entry = tk.entry = tk.Frame(master=window)
ent_info = tk.Entry(master=frm_entry, width=50)
lbl_info = tk.Label(master=frm_entry, text="See Terminal Output Below")

ent_info.pack()
lbl_info.pack()
add_info.pack()
frm_entry.pack()
lbl_result.pack()

window.mainloop()

print(votingInfo)
"""
Revision 10/11/2023
END
"""