
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

user_pass = []


#Cyclically
def get_easy_pass(length):
    user_pass = []
    while len(user_pass) < length: 

        i = random.randrange(1, 26)
        word = chr(ord("`") + i) #Gemerate word 
        if word in user_pass:
            del user_pass[user_pass.index(word)] #del identical word
        user_pass.append(word) #add word in the list 

    result = "".join(user_pass) # get together words
    return result # end




#Recursively
def get_complex_pass(length, user_pass=None):
    if user_pass is None:
        user_pass = []    

    if len(user_pass) < length:
        i = random.choice([[97, 122], [48, 57], [65, 91]]) # Selecting lower or Upper registr word or num
        random_word = random.randrange(i[0], i[1]) # Get random word or num
        word = chr(random_word) # Get specific value

        if word in user_pass:
            del user_pass[user_pass.index(word)] #del identical word

        user_pass.append(word) # add to the dict
        return get_complex_pass(length, user_pass) # Next itteration 
    
    result = "".join(user_pass) # get together words
        

    if result.isupper() or result.islower() or result.isdigit(): 

        user_pass = [] # del all values 
        return get_complex_pass(length, user_pass) # restart geretaion

    else:
        user_pass = []
        return result # end
   



#Tkinter

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def output_password():
    if spin_var.get().isdigit():

        if 26 > int(spin_var.get()) >= 8: 

            if var.get() == 0:
                get_pass = get_easy_pass(int(spin_var.get()))
                text_var.set(get_pass)

            else:
                get_pass = get_complex_pass(int(spin_var.get()))
                text_var.set(get_pass)
        else:
            messagebox.showwarning("Warning", "Enter correct password length (from 8 to 25)")
    else:
        messagebox.showwarning("Warning", "Enter password length")


root = Tk()
root.title("Password generator")
root.geometry("600x300")

var = IntVar()
var.set(0)

text_var = StringVar()
spin_var = StringVar()
spin_var.set(8)



easy_pass_btn = ttk.Radiobutton(text = "Easy password", variable=var, value = "0")
easy_pass_btn.pack(pady = 5, anchor="w")

complex_pass_btn = ttk.Radiobutton(text = "Strong password", variable=var, value = "1")
complex_pass_btn.pack(pady = 5, anchor='w')

label = ttk.Label(text = "Select length password (From 8 to 25)")
label.pack()

spinbox = ttk.Spinbox(from_ = 8, to = 25, width=10, textvariable=spin_var)
spinbox.pack()

label_pass = ttk.Entry(textvariable=text_var, justify="center", width=35)
label_pass.pack(pady=55)

btn = ttk.Button(text="Generate password", command=output_password)
btn.pack(side="bottom", pady=5)


center_window(root)
root.mainloop()