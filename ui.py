import tkinter as tk
from tkinter import ttk, messagebox
from operations import add_student, fetch_students, update_student, delete_student
import style

def build_ui():
    root = tk.Tk()
    root.title("🎓 Student CRUD App")
    root.geometry("700x500")
    root.configure(bg=style.BG_COLOR)

    # ======== Entries ========
    fields = ["Name", "Roll", "Class", "City"]
    entries = {}
    for i, field in enumerate(fields):
        tk.Label(root, text=field, bg=style.BG_COLOR, fg=style.LABEL_COLOR, font=style.FONT).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(root, bg=style.ENTRY_BG, font=style.FONT)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries[field.lower()] = entry

    tk.Label(root, text="Student ID (for Update/Delete)", bg=style.BG_COLOR, fg="#880e4f", font=style.FONT).grid(row=4, column=0, padx=10, pady=5, sticky="e")
    id_entry = tk.Entry(root, bg=style.ENTRY_BG, font=style.FONT)
    id_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    # ======== Buttons ========
    ttk.Button(root, text="➕ Add", command=lambda: handle_add(entries), style="Add.TButton").grid(row=5, column=0, pady=10)
    ttk.Button(root, text="📖 View", command=handle_view, style="View.TButton").grid(row=5, column=1, pady=10)
    ttk.Button(root, text="✏️ Update", command=lambda: handle_update(id_entry, entries), style="Update.TButton").grid(row=6, column=0, pady=10)
    ttk.Button(root, text="❌ Delete", command=lambda: handle_delete(id_entry), style="Delete.TButton").grid(row=6, column=1, pady=10)

    # ======== Styles ========
    s = ttk.Style()
    s.configure("Add.TButton", background=style.BTN_ADD, foreground="black")
    s.configure("View.TButton", background=style.BTN_VIEW, foreground="black")
    s.configure("Update.TButton", background=style.BTN_UPDATE, foreground="black")
    s.configure("Delete.TButton", background=style.BTN_DELETE, foreground="black")

    root.mainloop()

# ========== CRUD Handlers ==========

def handle_add(entries):
    data = [entries[k].get() for k in ['name', 'roll', 'class', 'city']]
    if all(data):
        add_student(*data)
        messagebox.showinfo("Success", "Student added!")
    else:
        messagebox.showwarning("Validation", "Please fill all fields.")

def handle_view():
    records = fetch_students()
    top = tk.Toplevel()
    top.title("📚 Student Records")
    top.geometry("600x400")
    top.configure(bg="#fff3e0")

    for idx, row in enumerate(records):
        tk.Label(top, text=row, bg="#fff3e0", font=("Consolas", 10)).grid(row=idx, column=0, padx=10, pady=2, sticky="w")

def handle_update(id_entry, entries):
    id_val = id_entry.get()
    if id_val:
        data = [entries[k].get() for k in ['name', 'roll', 'class', 'city']]
        if all(data):
            update_student(id_val, *data)
            messagebox.showinfo("Success", "Student updated!")
        else:
            messagebox.showwarning("Validation", "Fill all fields to update.")
    else:
        messagebox.showwarning("Validation", "Enter Student ID to update.")

def handle_delete(id_entry):
    id_val = id_entry.get()
    if id_val:
        delete_student(id_val)
        messagebox.showinfo("Deleted", f"Student with ID {id_val} deleted!")
    else:
        messagebox.showwarning("Validation", "Enter Student ID to delete.")
