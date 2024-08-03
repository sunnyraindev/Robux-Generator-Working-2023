import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("Robux Generator Working 2023")
root.iconbitmap(resource_path("robux.ico"))
root.geometry("400x300")
root.attributes("-topmost", True)
root.resizable(False, False)

bg_image = Image.open(resource_path("roblox.jpg"))
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)


label_username = tk.Label(root, text="Username", bg="lightgrey")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create a label and entry for the password
label_password = tk.Label(root, text="Password", bg="lightgrey")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create a label and entry for the amount of robux
label_robux = tk.Label(root, text="How much robux you want", bg="lightgrey")
label_robux.pack(pady=5)
entry_robux = tk.Entry(root)
entry_robux.pack(pady=5)

def submit_form():
    
    messagebox.showinfo("Robux", "Enjoy your robux")
    root.after(100, pc_has_virus)

def pc_has_virus():
    messagebox.showerror("Your pc has virus", "All your robux are gone!")
    root.after(100, pc_has_virus)


button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.pack(pady=20)

# Run the application
root.mainloop()