import csv
import os

DATA_FILE = "transactions.csv"

def save_transaction(transaction):
    """Save a transaction to CSV file"""
    file_exists = os.path.isfile(DATA_FILE)
    
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Type", "Amount", "Category", "Description", "Date"])
        writer.writerow([
            transaction["type"],
            transaction["amount"],
            transaction["category"],
            transaction["description"],
            transaction["date"]
        ])

def load_transactions():
    """Load all transactions from CSV file"""
    transactions = []
    if not os.path.isfile(DATA_FILE):
        return transactions
    
    with open(DATA_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions
