from tkinter import *
from tkinter import messagebox
import random
import pyperclip as pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)

    print(f"Your password is: {password}")
    pass_entry.insert(0, password)

    # save the string into the clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_entries():
    website_val = website_entry.get()
    email_val = email_entry.get()
    pass_val = pass_entry.get()

    # show warning that a field is left empty!
    if website_val == "" or email_val == "" or pass_val == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # standard dialogs
        # messagebox.showinfo(title="Tile", message="message")
        is_ok = messagebox.askokcancel(title=website_val, message=f"These are the details entered: \nEmail: {email_val}\n"
                                                                  f"Password: {pass_val}\nIs it ok to save? ")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
                # delete function from an entry
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(columnspan=2, column=1, row=0)

# 3 Labels
# Website:
website = Label(text="Website: ")
website.grid(column=0, row=1)
# Email/Username:
email = Label(text="Email/Username: ")
email.grid(column=0, row=2)
# Password
password = Label(text="Password: ")
password.grid(column=0, row=3)

# 3 Entry fields
# Website_entry
website_entry = Entry(width=40)
website_entry.grid(columnspan=2, column=1, row=1)
website_entry.focus()
# Email/Un entry
email_entry = Entry(width=40)
email_entry.grid(columnspan=2, column=1, row=2)
email_entry.insert(END, "text@gmail.com")
# Password_entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# 2 Buttons
# Generate Password
gen_pass = Button(text="Generate Password", command=pass_gen)
gen_pass.grid(column=2, row=3)
# Add
add_button = Button(text="Add", width=34, command=write_entries)
add_button.grid(columnspan=2, column=1, row=4)

window.mainloop()
