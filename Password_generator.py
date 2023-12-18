
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random



class User_pass:

    user_pass = []

    def __init__(self, length):
        self.length = length


    def get_simple_pass(self):
        self.user_pass = []

        while len(self.user_pass) < self.length - 3 and len(self.user_pass) < 100: 

            random_range = random.randrange(1, 26)
            result_r_word = chr(ord("`") + random_range) #Gemerate word 


            self.user_pass.append(result_r_word) #add word in the list 

        result = "".join(self.user_pass) # get together words
        result += str(random.randrange(100,999)) # adds three digits to the end
        return result 
    

    
    def get_complex_pass(self):
        self.user_pass = []
        
        while len(self.user_pass) < self.length and len(self.user_pass) < 100:

            r_choice = random.choice([[97, 122], [48, 57], [65, 91]]) # Selecting lower or Upper registr word or num
            random_word = random.randrange(r_choice[0], r_choice[1]) # Get random word or num
            word = chr(random_word) # Get specific value

            self.user_pass.append(word) # add to the dict
        
        result = "".join(self.user_pass) # get together words


        if result.isupper() or result.islower() or result.isdigit(): 

            self.user_pass = [] # del all values 
            return self.get_complex_ass(self)

        else:

            return result 


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

        if 78 > int(spin_var.get()) >= 8: 

            if var.get() == 0:
                get_pass = User_pass(int(spin_var.get()))
                text_var.set(get_pass.get_simple_pass())

            else:
                get_pass = User_pass(int(spin_var.get()))
                text_var.set(get_pass.get_complex_pass())
        else:
            messagebox.showwarning("Warning", "Enter correct password length (from 8 to 77)")
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

label = ttk.Label(text = "Select length password (From 8 to 77)")
label.pack()

spinbox = ttk.Spinbox(from_ = 8, to = 77, width=10, textvariable=spin_var)
spinbox.pack()

label_pass = ttk.Entry(textvariable=text_var, justify="center", width=88)
label_pass.pack(pady=55)

btn = ttk.Button(text="Generate password", command=output_password)
btn.pack(side="bottom", pady=5)


center_window(root)
root.mainloop()