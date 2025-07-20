import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import student_operations as ops

def create_form(root):
    root.title("🎓 Student Management System")
    root.geometry("820x500")
    root.config(bg="#e0f7fa")
    root.resizable(False, False)

    name_var = tk.StringVar()
    roll_var = tk.StringVar()
    class_var = tk.StringVar()
    city_var = tk.StringVar()
    selected_id = [None]

    is_dark_mode = tk.BooleanVar()

    # ---------- Theme Styles ----------
    style = ttk.Style()
    style.theme_use("clam")

    def set_theme(dark):
        if dark:
            bg_color = "#263238"
            frame_color = "#37474f"
            fg_color = "white"
            entry_bg = "#455a64"
            tree_bg = "#37474f"
            tree_fg = "#eceff1"
            selected_bg = "#00acc1"
        else:
            bg_color = "#e0f7fa"
            frame_color = "#b2ebf2"
            fg_color = "#000000"
            entry_bg = "white"
            tree_bg = "white"
            tree_fg = "black"
            selected_bg = "#80deea"

        root.config(bg=bg_color)
        form_frame.config(bg=frame_color)
        list_frame.config(bg=bg_color)
        title.config(bg=bg_color, fg=fg_color)

        for widget in form_frame.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Entry) or isinstance(widget, tk.Button):
                widget.config(bg=frame_color, fg=fg_color)

        style.configure("Treeview", background=tree_bg, foreground=tree_fg, rowheight=30, fieldbackground=tree_bg)
        style.map("Treeview", background=[("selected", selected_bg)])
        style.configure("Treeview.Heading", background="#00838f", foreground="white")

    # ---------- Title ----------
    title = tk.Label(root, text="Student CRUD Application", font=("Helvetica", 18, "bold"))
    title.pack(pady=10)

    # ---------- Form Frame ----------
    form_frame = tk.Frame(root, bg="#b2ebf2", bd=2, relief=tk.GROOVE)
    form_frame.place(x=20, y=60, width=310, height=400)

    def create_field(label, var, row):
        tk.Label(form_frame, text=label, bg=form_frame["bg"], font=("Segoe UI", 10)).grid(row=row, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(form_frame, textvariable=var, width=25).grid(row=row, column=1, padx=10, pady=5)

    create_field("Name", name_var, 0)
    create_field("Roll No", roll_var, 1)
    create_field("Class", class_var, 2)
    create_field("City", city_var, 3)

    def clear_fields():
        name_var.set("")
        roll_var.set("")
        class_var.set("")
        city_var.set("")
        selected_id[0] = None

    def on_add():
        if name_var.get():
            ops.add(name_var.get(), roll_var.get(), class_var.get(), city_var.get())
            refresh_tree()
            clear_fields()
        else:
            messagebox.showwarning("Missing Data", "Name field is required.")

    def on_update():
        if selected_id[0] is not None:
            ops.update_record(selected_id[0], name_var.get(), roll_var.get(), class_var.get(), city_var.get())
            refresh_tree()
            clear_fields()
        else:
            messagebox.showinfo("Select Record", "Please select a record to update.")

    def on_delete():
        if selected_id[0] is not None:
            ops.delete_record(selected_id[0])
            refresh_tree()
            clear_fields()
        else:
            messagebox.showinfo("Select Record", "Please select a record to delete.")

    def export_to_csv():
        students = ops.get_all()
        if not students:
            messagebox.showinfo("Export", "No records to export.")
            return
        file = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
        if file:
            with open(file, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Roll No", "Class", "City"])
                writer.writerows(students)
            messagebox.showinfo("Exported", f"Data exported successfully to:\n{file}")

    btn_frame = tk.Frame(form_frame, bg=form_frame["bg"])
    btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

    tk.Button(btn_frame, text="Add", width=10, bg="#00796b", fg="white", command=on_add).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Update", width=10, bg="#0288d1", fg="white", command=on_update).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete", width=10, bg="#d32f2f", fg="white", command=on_delete).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Export", width=32, bg="#5e35b1", fg="white", command=export_to_csv).grid(row=1, column=0, columnspan=3, pady=10)

    # ---------- List Frame ----------
    list_frame = tk.Frame(root, bg="#e0f7fa")
    list_frame.place(x=350, y=60, width=450, height=400)

    columns = ("ID", "Name", "Roll No", "Class", "City")
    tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=85)
    tree.column("Name", width=130)
    tree.pack(fill="both", expand=True)

    def refresh_tree():
        for row in tree.get_children():
            tree.delete(row)
        for student in ops.get_all():
            tree.insert("", tk.END, values=student)

    def on_tree_select(event):
        selected = tree.focus()
        if selected:
            data = tree.item(selected)["values"]
            selected_id[0] = data[0]
            name_var.set(data[1])
            roll_var.set(data[2])
            class_var.set(data[3])
            city_var.set(data[4])

    tree.bind("<<TreeviewSelect>>", on_tree_select)

    # Dark Mode Checkbox
    mode_toggle = ttk.Checkbutton(root, text="🌙 Dark Mode", variable=is_dark_mode,
                                  command=lambda: set_theme(is_dark_mode.get()))
    mode_toggle.place(x=700, y=20)

    # Apply initial light theme
    set_theme(False)
    refresh_tree()
