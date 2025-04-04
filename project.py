import sqlite3

def create_database():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_product(name, quantity, price):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()

def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

def fetch_all_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def find_most_expensive_product():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1")
    product = cursor.fetchone()
    conn.close()
    return product

# Example usage
if __name__ == "__main__":
    create_database()
    add_product("Laptop", 10, 75000)
    add_product("Smartphone", 20, 50000)
    add_product("Tablet", 15, 30000)
    
    print("All Products:")
    print(fetch_all_products())
    
    print("Most Expensive Product:")
    print(find_most_expensive_product())
