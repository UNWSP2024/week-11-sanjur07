'''Program 1'''
import tkinter as tk

root = tk.Tk()
root.title("Favorite Saying")

root.geometry("400x200")


favorite_saying = "The journey of a thousand miles begins with a single step."
label = tk.Label(root, text=favorite_saying, wraplength=300, font=("Arial", 14), pady=20)
label.pack()

root.mainloop()

'''Program 2'''
import tkinter as tk

root = tk.Tk()
root.title("Show Info")

root.geometry("400x200")

def show_info():
    info_label.config(text="Name: Sanjana Raveendranath\nAddress: 123 Maple Street, Prior Lake, MN")

def quit_app():
    root.destroy()

show_button = tk.Button(root, text="Show Info", command=show_info, font=("Arial", 12))
show_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app, font=("Arial", 12))
quit_button.pack(pady=10)

info_label = tk.Label(root, text="", font=("Arial", 12), pady=20)
info_label.pack()

root.mainloop()

