import sqlite3

# Create or connect to a database #
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Create a table #9
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()

import sqlite3

# Function to add a product #
def add_product(product_id, name, quantity, price):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (id, name, quantity, price) VALUES (?, ?, ?, ?)", 
                   (product_id, name, quantity, price))
    conn.commit()
    conn.close()

# Function to update product quantity #
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", 
                   (new_quantity, product_id))
    conn.commit()
    conn.close()

# Function to fetch all products #
def fetch_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

# Function to find the most expensive product #
def most_expensive_product():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1")
    product = cursor.fetchone()
    conn.close()
    return product


# Example Usage #
'''if __name__ == "__main__":
  add_product(2, "Smartphone", 20, 45000)
    
    update_quantity(1, 12)
    
    print("All Products:", fetch_products())
    print("Most Expensive Product:", most_expensive_product())'''

# Close connection #
conn.close()
