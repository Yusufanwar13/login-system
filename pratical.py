import tkinter as tk
from tkinter import messagebox

# Dummy database for storing user credentials
users_db = {}

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users_db:
        messagebox.showerror("Error", "Username already exists!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        users_db[username] = password
        messagebox.showinfo("Success", "Registration successful!")
        registration_window.destroy()

def open_registration_window():
    global registration_window, username_entry, password_entry
    registration_window = tk.Toplevel(root)
    registration_window.title("Register")
    
    tk.Label(registration_window, text="Username", font=("Arial", 14)).pack(pady=5)
    username_entry = tk.Entry(registration_window, font=("Arial", 14), width=25, bg="green")
    username_entry.pack(pady=5)
    
    tk.Label(registration_window, text="Password", font=("Arial", 14)).pack(pady=5)
    password_entry = tk.Entry(registration_window, show='*', font=("Arial", 14), width=25, bg="lightyellow")
    password_entry.pack(pady=5)
    
    tk.Button(registration_window, text="Register", command=register_user, font=("Arial", 14), bg="lightblue", width=15).pack(pady=10)

def login_user():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users_db and users_db[username] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Main application window
root = tk.Tk()
root.title("Login System")

# Login Form
tk.Label(root, text="Username", font=("Arial", 14)).pack(pady=10)
username_entry = tk.Entry(root, font=("Arial", 14), width=25, bg="lightyellow")
username_entry.pack(pady=10)

tk.Label(root, text="Password", font=("Arial", 14)).pack(pady=10)
password_entry = tk.Entry(root, show='*', font=("Arial", 14), width=25, bg="lightyellow")
password_entry.pack(pady=10)

tk.Button(root, text="Login", command=login_user, font=("Arial", 14), bg="lightblue", width=15).pack(pady=10)
tk.Button(root, text="Register", command=open_registration_window, font=("Arial", 14), bg="lightblue", width=15).pack(pady=10)

root.mainloop()