import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

# Initialize main window
root = Tk()
root.title("Inventory Control System")
root.geometry("400x300")

# Initialize DB connection
def Database():
    global conn, cursor
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS admin (
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS product (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        product_qty INTEGER,
        product_price REAL)""")
    cursor.execute("SELECT * FROM admin WHERE username='admin' AND password='admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO admin (username, password) VALUES ('admin', 'admin')")
        conn.commit()

# Exit function
def Exit():
    root.destroy()

# Login form
def ShowLoginForm():
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x200")

    Label(login_window, text="Username:").pack(pady=5)
    username_entry = Entry(login_window)
    username_entry.pack()

    Label(login_window, text="Password:").pack(pady=5)
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    def do_login():
        username = username_entry.get()
        password = password_entry.get()
        Database()
        cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
        if cursor.fetchone():
            login_window.destroy()
            ShowDashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
        conn.close()

    Button(login_window, text="Login", command=do_login).pack(pady=10)

# Dashboard
def ShowDashboard():
    dash = Toplevel(root)
    dash.title("Dashboard")
    dash.geometry("800x600")

    menubar = Menu(dash)
    dash.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=dash.destroy)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", menu=filemenu)

    invmenu = Menu(menubar, tearoff=0)
    invmenu.add_command(label="Add Product", command=ShowAddProduct)
    invmenu.add_command(label="View Products", command=ShowViewProducts)
    invmenu.add_command(label="Stock Management", command=ShowStockManagement)
    menubar.add_cascade(label="Inventory", menu=invmenu)

    Label(dash, text="Welcome to Inventory System", font=('Arial', 18)).pack(pady=20)

# Add Product
def ShowAddProduct():
    add_window = Toplevel(root)
    add_window.title("Add Product")

    Label(add_window, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
    name_entry = Entry(add_window)
    name_entry.grid(row=0, column=1)

    Label(add_window, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
    qty_entry = Entry(add_window)
    qty_entry.grid(row=1, column=1)

    Label(add_window, text="Price:").grid(row=2, column=0, padx=10, pady=5)
    price_entry = Entry(add_window)
    price_entry.grid(row=2, column=1)

    def add_product():
        name = name_entry.get()
        try:
            qty = int(qty_entry.get())
            price = float(price_entry.get())
            Database()
            cursor.execute("INSERT INTO product (product_name, product_qty, product_price) VALUES (?, ?, ?)",
                           (name, qty, price))
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(add_window, text="Add", command=add_product).grid(row=3, columnspan=2, pady=10)

# View Products
def ShowViewProducts():
    view_window = Toplevel(root)
    view_window.title("Product List")
    view_window.geometry("600x400")

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Qty", "Price"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Qty", text="Quantity")
    tree.heading("Price", text="Price")
    tree.pack(fill=BOTH, expand=True)

    Database()
    cursor.execute("SELECT * FROM product")
    for row in cursor.fetchall():
        tree.insert("", END, values=row)
    conn.close()

# Stock Management
def ShowStockManagement():
    stock_window = Toplevel(root)
    stock_window.title("Stock Update")

    Database()
    cursor.execute("SELECT product_name FROM product")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()

    Label(stock_window, text="Select Product:").grid(row=0, column=0, padx=10, pady=5)
    product_combo = ttk.Combobox(stock_window, values=names, state="readonly")
    product_combo.grid(row=0, column=1)

    Label(stock_window, text="New Quantity:").grid(row=1, column=0, padx=10, pady=5)
    new_qty_entry = Entry(stock_window)
    new_qty_entry.grid(row=1, column=1)

    def update_stock():
        name = product_combo.get()
        try:
            new_qty = int(new_qty_entry.get())
            Database()
            cursor.execute("UPDATE product SET product_qty=? WHERE product_name=?", (new_qty, name))
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated", "Stock updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(stock_window, text="Update Stock", command=update_stock).grid(row=2, columnspan=2, pady=10)

# Main Window UI
Label(root, text="Inventory System", font=('Arial', 20)).pack(pady=30)
Button(root, text="Login", width=20, command=ShowLoginForm).pack(pady=10)
Button(root, text="Exit", width=20, command=Exit).pack(pady=10)

# Run it
root.mainloop()
