import csv

rows = [
    {"id": 1, "product": "Laptop", "price": 1200},
    {"id": 2, "product": "Mouse", "price": 25}
]

# Write tabular data using DictWriter (serialization)
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "product", "price"])
    writer.writeheader()
    writer.writerows(rows)

# Read tabular data using DictReader (deserialization)
with open("products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Product: {row['product']}, Price: ${row['price']}")