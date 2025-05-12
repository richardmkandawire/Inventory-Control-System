import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ======================
# DATABASE SETUP
# ======================

def create_table():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price_mwk REAL NOT NULL,
            category TEXT NOT NULL CHECK(category IN (
                'Electronics', 'Stationary', 'Grocery', 'Clothing',
                'Home Appliances', 'Medical Supplies', 'Tools and Hardware',
                'Books and Media', 'Food and Beverage', 'Miscellaneous Items'
            ))
        )
    ''')
    conn.commit()
    conn.close()
