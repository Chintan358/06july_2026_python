import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as sql


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    return sql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="6july_python"
    )


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("Student Registration System")
root.geometry("1000x650")
root.resizable(False, False)

root.configure(bg="#f4f6f8")


# ============================================================
# VARIABLES
# ============================================================

id_var = tk.StringVar()
name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
search_var = tk.StringVar()


# ============================================================
# FUNCTIONS
# ============================================================

def clear_fields():
    """Clear all input fields."""

    id_var.set("")
    name_var.set("")
    email_var.set("")
    phone_var.set("")

    name_entry.focus()


def validate_form():

    name = name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()

    if name == "":
        messagebox.showerror("Validation Error", "Please enter student name.")
        name_entry.focus()
        return False

    if email == "":
        messagebox.showerror("Validation Error", "Please enter email.")
        email_entry.focus()
        return False

    if phone == "":
        messagebox.showerror("Validation Error", "Please enter phone number.")
        phone_entry.focus()
        return False

    if len(phone) != 10 or not phone.isdigit():
        messagebox.showerror(
            "Validation Error",
            "Phone number must contain exactly 10 digits."
        )
        phone_entry.focus()
        return False

    return True


# ============================================================
# CREATE STUDENT
# ============================================================

def add_student():

    if not validate_form():
        return

    name = name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()

    try:

        con = get_connection()
        cursor = con.cursor()

        query = """
            INSERT INTO student (name, email, phone)
            VALUES (%s, %s, %s)
        """

        values = (name, email, phone)

        cursor.execute(query, values)

        con.commit()

        cursor.close()
        con.close()

        messagebox.showinfo(
            "Success",
            "Student registered successfully."
        )

        clear_fields()
        load_students()

    except sql.Error as e:

        messagebox.showerror(
            "Database Error",
            f"Error: {e}"
        )


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def load_students(search=""):

    # Clear existing rows
    for row in student_table.get_children():
        student_table.delete(row)

    try:

        con = get_connection()
        cursor = con.cursor()

        if search == "":

            query = """
                SELECT id, name, email, phone
                FROM student
                ORDER BY id DESC
            """

            cursor.execute(query)

        else:

            query = """
                SELECT id, name, email, phone
                FROM student
                WHERE name LIKE %s
                   OR email LIKE %s
                   OR phone LIKE %s
            """

            search_value = "%" + search + "%"

            cursor.execute(
                query,
                (search_value, search_value, search_value)
            )

        students = cursor.fetchall()

        for student in students:

            student_table.insert(
                "",
                tk.END,
                values=student
            )

        cursor.close()
        con.close()

    except sql.Error as e:

        messagebox.showerror(
            "Database Error",
            f"Error: {e}"
        )


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student(*args):

    search = search_var.get().strip()

    load_students(search)


# ============================================================
# GET SELECTED STUDENT
# ============================================================

def select_student(event):

    selected = student_table.focus()

    if selected == "":
        return

    data = student_table.item(selected)

    values = data["values"]

    if values:

        id_var.set(values[0])
        name_var.set(values[1])
        email_var.set(values[2])
        phone_var.set(values[3])


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():

    if id_var.get() == "":
        messagebox.showwarning(
            "Select Student",
            "Please select a student from the table first."
        )
        return

    if not validate_form():
        return

    student_id = id_var.get()

    name = name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()

    try:

        con = get_connection()
        cursor = con.cursor()

        query = """
            UPDATE student
            SET name = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """

        values = (
            name,
            email,
            phone,
            student_id
        )

        cursor.execute(query, values)

        con.commit()

        cursor.close()
        con.close()

        messagebox.showinfo(
            "Success",
            "Student updated successfully."
        )

        clear_fields()
        load_students()

    except sql.Error as e:

        messagebox.showerror(
            "Database Error",
            f"Error: {e}"
        )


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    if id_var.get() == "":
        messagebox.showwarning(
            "Select Student",
            "Please select a student from the table first."
        )
        return

    student_id = id_var.get()

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if not confirm:
        return

    try:

        con = get_connection()
        cursor = con.cursor()

        query = """
            DELETE FROM student
            WHERE id = %s
        """

        cursor.execute(
            query,
            (student_id,)
        )

        con.commit()

        cursor.close()
        con.close()

        messagebox.showinfo(
            "Success",
            "Student deleted successfully."
        )

        clear_fields()
        load_students()

    except sql.Error as e:

        messagebox.showerror(
            "Database Error",
            f"Error: {e}"
        )


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#263238",
    height=80
)

header.pack(
    fill="x"
)

title_label = tk.Label(
    header,
    text="Student Registration System",
    font=("Arial", 24, "bold"),
    bg="#263238",
    fg="white"
)

title_label.pack(
    pady=22
)


# ============================================================
# FORM FRAME
# ============================================================

form_frame = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

form_frame.place(
    x=30,
    y=105,
    width=940,
    height=190
)


# ============================================================
# FORM TITLE
# ============================================================

form_title = tk.Label(
    form_frame,
    text="Student Details",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#263238"
)

form_title.place(
    x=20,
    y=15
)


# ============================================================
# ID
# ============================================================

tk.Label(
    form_frame,
    text="Student ID",
    font=("Arial", 11, "bold"),
    bg="white"
).place(
    x=30,
    y=60
)

id_entry = ttk.Entry(
    form_frame,
    textvariable=id_var,
    width=25,
    state="readonly"
)

id_entry.place(
    x=30,
    y=88
)


# ============================================================
# NAME
# ============================================================

tk.Label(
    form_frame,
    text="Name",
    font=("Arial", 11, "bold"),
    bg="white"
).place(
    x=260,
    y=60
)

name_entry = ttk.Entry(
    form_frame,
    textvariable=name_var,
    width=28
)

name_entry.place(
    x=260,
    y=88
)


# ============================================================
# EMAIL
# ============================================================

tk.Label(
    form_frame,
    text="Email",
    font=("Arial", 11, "bold"),
    bg="white"
).place(
    x=510,
    y=60
)

email_entry = ttk.Entry(
    form_frame,
    textvariable=email_var,
    width=30
)

email_entry.place(
    x=510,
    y=88
)


# ============================================================
# PHONE
# ============================================================

tk.Label(
    form_frame,
    text="Phone",
    font=("Arial", 11, "bold"),
    bg="white"
).place(
    x=770,
    y=60
)

phone_entry = ttk.Entry(
    form_frame,
    textvariable=phone_var,
    width=20
)

phone_entry.place(
    x=770,
    y=88
)


# ============================================================
# BUTTONS
# ============================================================

add_button = tk.Button(
    form_frame,
    text="Add Student",
    font=("Arial", 10, "bold"),
    bg="#2e7d32",
    fg="white",
    width=14,
    cursor="hand2",
    command=add_student
)

add_button.place(
    x=250,
    y=135
)


update_button = tk.Button(
    form_frame,
    text="Update",
    font=("Arial", 10, "bold"),
    bg="#1565c0",
    fg="white",
    width=12,
    cursor="hand2",
    command=update_student
)

update_button.place(
    x=390,
    y=135
)


delete_button = tk.Button(
    form_frame,
    text="Delete",
    font=("Arial", 10, "bold"),
    bg="#c62828",
    fg="white",
    width=12,
    cursor="hand2",
    command=delete_student
)

delete_button.place(
    x=510,
    y=135
)


clear_button = tk.Button(
    form_frame,
    text="Clear",
    font=("Arial", 10, "bold"),
    bg="#616161",
    fg="white",
    width=12,
    cursor="hand2",
    command=clear_fields
)

clear_button.place(
    x=630,
    y=135
)


# ============================================================
# SEARCH FRAME
# ============================================================

search_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

search_frame.place(
    x=30,
    y=315,
    width=940,
    height=50
)


tk.Label(
    search_frame,
    text="Search Student:",
    font=("Arial", 12, "bold"),
    bg="#f4f6f8"
).pack(
    side="left",
    padx=(0, 10)
)


search_entry = ttk.Entry(
    search_frame,
    textvariable=search_var,
    width=40
)

search_entry.pack(
    side="left"
)


search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 10, "bold"),
    bg="#455a64",
    fg="white",
    width=12,
    cursor="hand2",
    command=search_student
)

search_button.pack(
    side="left",
    padx=10
)


show_all_button = tk.Button(
    search_frame,
    text="Show All",
    font=("Arial", 10, "bold"),
    bg="#00838f",
    fg="white",
    width=12,
    cursor="hand2",
    command=lambda: [
        search_var.set(""),
        load_students()
    ]
)

show_all_button.pack(
    side="left"
)


# ============================================================
# STUDENT TABLE
# ============================================================

table_frame = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

table_frame.place(
    x=30,
    y=375,
    width=940,
    height=240
)


columns = (
    "id",
    "name",
    "email",
    "phone"
)


student_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=9
)


# Column headings

student_table.heading(
    "id",
    text="ID"
)

student_table.heading(
    "name",
    text="Name"
)

student_table.heading(
    "email",
    text="Email"
)

student_table.heading(
    "phone",
    text="Phone"
)


# Column widths

student_table.column(
    "id",
    width=80,
    anchor="center"
)

student_table.column(
    "name",
    width=250
)

student_table.column(
    "email",
    width=350
)

student_table.column(
    "phone",
    width=200
)


# Scrollbar

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=student_table.yview
)

student_table.configure(
    yscrollcommand=scrollbar.set
)


student_table.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Select row

student_table.bind(
    "<ButtonRelease-1>",
    select_student
)


# Search while typing

search_var.trace_add(
    "write",
    search_student
)


# ============================================================
# LOAD DATA WHEN APPLICATION STARTS
# ============================================================

load_students()

name_entry.focus()


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()