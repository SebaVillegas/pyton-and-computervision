from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass(**kwargs):
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password
        }
    }
    
    if website == '' or email == '' or password == '':
        messagebox.showwarning(title="Warning!", message=f'There is an empty field!')
    else: 
        is_ok = messagebox.askokcancel(title=website, message=f'Is it all ok to save?')
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file) # para leer un json
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    #savind updated data
                    json.dump(new_data, data_file, indent=4)
                    
            else:
                with open("data.json", "w") as data_file:
                    #updating old data with new data
                    data.update(new_data)
                    #savind updating data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                
                    
# write json.dump()
# read json.load()
# update json.update()

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='You do not save any yet')
    else:       
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n Password:{password}')
        else:
            messagebox.showinfo(title='Error', message=f'{website} is not added')
            

# ---------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas =  Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/user:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=23)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=23)
email_entry.grid(row=2,column=1)
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)


generate_password_btn = Button(text='Generate', width=8, command=generate_password)
generate_password_btn.grid(row=3, column=2)
add_button = Button(text='Add', width=35, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search', width=8, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()