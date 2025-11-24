from storage import load_transactions

def add_transaction():
    """Add a new transaction"""
    print("\n--- Add Transaction ---")
    
    # Get input from user
    transaction_type = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")
    date = input("Date (YYYY-MM-DD): ")
    
    # Create transaction dictionary
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    
    return transaction

def view_summary():
    """View financial summary"""
    transactions = load_transactions()
    
    if not transactions:
        print("\nNo transactions found!")
        return
    
    total_income = 0
    total_expense = 0
    
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += float(transaction["amount"])
        else:
            total_expense += float(transaction["amount"])
    
    balance = total_income - total_expense
    
    print("\n--- Financial Summary ---")
    print(f"Total Income: ₹{total_income:.2f}")
    print(f"Total Expense: ₹{total_expense:.2f}")
    print(f"Balance: ₹{balance:.2f}")
