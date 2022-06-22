import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import datetime


class WritingApp(tk.Frame):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self._after_id = None
        self.text_area = tk.Text()
        self.text_area.config(state="disabled", bg="#FF5C8D", fg="#323232",height=10, pady=20, padx=20, font=("Comic Sans MS", 15, "bold"))
        self.text_area.grid(row=1, column=1, columnspan=3)
        self.text_area.bind("<Key>", self.handel_wait)
        # counts for five minutes.
        self.count = 5 * 60
        # minutes
        self.start_button = Button(text="Start Writing", command=self.start_writing, bg="#524A4E", fg="#FDEFF4")
        self.start_button.grid(row=0, column=2, columnspan=1)

        self.words = 0
        self.number_words = tk.Label(text=f"Number of Words: {self.words}", fg="#524A4E",bg="#FDEFF4", font=("Comic Sans MS", 10, "bold"))
        self.number_words.grid(row=0, column=3)

    def handel_wait(self, event):
        if event.char == " ":
            self.words += 1
            self.number_words.config(text=f"Number of Words: {self.words}")
        if self._after_id is not None:
            self.after_cancel(self._after_id)

        self._after_id = self.count_down()

    def delete_text(self):
        self.text_area.delete("1.0", END)
        self.words = 0
        self.number_words.config(text=f"Number of Words: {self.words}""")

    def count_down(self):
        print("Text Can be Deleted")
        return self.after(5000, func=self.delete_text)

    def start_writing(self):
        self.text_area.config(state="normal")
        self.start_button.config(state="disabled")
        self.start_timer(self.count)
        self.words = 0
        self.number_words.config(text=f"Number of Words: {self.words}""")

    def start_timer(self, count):
        if count > 0:
            self.window.after(1000, self.start_timer, count-1)
        else:
            showinfo(
                title="Done",
                message=f"You wrote {self.words} words. what you have written is in the text_written.txt"
            )
            with open("text_written.txt", 'a') as writings:
                writings.write(str(datetime.datetime.now().date()))
                writings.write('\n')
                text = self.text_area.get("1.0", END)
                print(text)
                writings.write(text)

            self.delete_text()
            self.text_area.config(state="disabled")
            self.after_cancel(self._after_id)
            self.start_button.config(text="Restart Timer", state="normal")




