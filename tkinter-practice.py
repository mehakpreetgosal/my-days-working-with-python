from logging import root
import tkinter as tk
root = tk.Tk()
Label = tk.Label(root, text="Hello, Its me!", font=("Ubuntu", 24, "italic"))
Label.pack()
def click():
    print("Button clicked")

Label.place(x=50, y=50)
btn = tk.Button(root, text="Click Me", font=("Times New Roman", 14, "italic"), command=click)
btn.pack()
btn.place(x=100, y=100)
#loding an image
img = tk.PhotoImage(file="C:\Users\kau13192\projects\wp9581362.jpg")

root.configure(bg="#ADD8E6")

root.mainloop()