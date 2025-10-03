import sqlite3

# Connect (creates sales_data.db if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sample_data = [
    ("Laptop", 5, 60000),
    ("Laptop", 3, 62000),
    ("Mobile", 10, 15000),
    ("Mobile", 8, 16000),
    ("Tablet", 6, 20000),
    ("Tablet", 4, 21000),
    ("Headphones", 12, 2000),
    ("Headphones", 7, 2500),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("✅ sales_data.db created with sample data")
