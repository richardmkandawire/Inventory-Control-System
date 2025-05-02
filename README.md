# Inventory-Control-System using Tkinter and Sqlite

📌 Objective:
To build a desktop-based Inventory Control System that allows users to log in, manage products (add/view), and update stock quantities using a graphical user interface.

🧩 Modules Used:
tkinter – GUI toolkit for Python

sqlite3 – Lightweight embedded database

💡 Features:
Login Authentication

Default credentials: admin / admin

Stored in the admin table in SQLite.

Product Management

Add new products (name, quantity, price).

View all products in a sortable table.

Stock Management

Update stock quantity for existing products.

GUI Interface

Intuitive interface with Tkinter for easy navigation.

🔑 Login Credentials:
Username	Password
admin	admin

📁 Project Structure:
plaintext
Copy
Edit
full_program.py      # Main application script
inventory.db         # SQLite database (auto-generated)
🛠️ Functional Description:
1. Login Window
Validates credentials using the admin table.

On success, opens the Dashboard.

2. Dashboard
Main navigation window.

Menu bar includes:

Add Product

View Products

Stock Management

Logout / Exit

3. Add Product
Opens a new window.

User inputs:

Product Name

Quantity

Price

Saves to the product table.

4. View Products
Opens a table view with:

Product ID

Name

Quantity

Price

5. Stock Management
Lets user select a product from a dropdown.

Updates the stock quantity.

🗃️ Database Schema:
admin table:
Column	Type
admin_id	INTEGER PRIMARY KEY AUTOINCREMENT
username	TEXT
password	TEXT

product table:
Column	Type
product_id	INTEGER PRIMARY KEY AUTOINCREMENT
product_name	TEXT
product_qty	INTEGER
product_price	REAL

🖥️ How to Run:
Make sure Python is installed (preferably 3.8+).

Save the script as full_program.py.

Run using:

bash
Copy
Edit
python full_program.py
The database will be auto-created on first run.

📌 Future Enhancements:
Export product list to CSV

Implement user roles (Admin/User)

Low stock alerts

Product search and filters

Transaction log and history

PDF or chart-based reporting

👨‍💻 Developed With:
Python 3.x

Tkinter (Standard GUI toolkit)

SQLite (Built-in lightweight database)
