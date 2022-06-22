import tkinter as tk
from writing_app import *


window = tk.Tk()
window.geometry("1200x800")
window.config(bg="#FDEFF4", padx=100, pady=100)
label = tk.Label(master=window, text="Write with none stop", pady=20, padx=20, fg="#524A4E",bg="#FDEFF4", font=("Comic Sans MS", 10, "bold"))
label.grid(row=0, column=0, columnspan=2)
writing_app = WritingApp(window)
writing_app.mainloop()