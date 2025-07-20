import tkinter as tk
from student_form import create_form
import student_operations as ops

if __name__ == "__main__":
    ops.init()
    root = tk.Tk()
    create_form(root)
    root.mainloop()
