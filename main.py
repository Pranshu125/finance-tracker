from transactions import add_transaction, view_summary
from storage import save_transaction

def main():
    print("Personal Finance Tracker")
    
    while True:
        print("\n1. Add Transaction")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            transaction = add_transaction()
            save_transaction(transaction)
            print("Transaction added successfully!")
            
        elif choice == "2":
            view_summary()
            
        elif choice == "3":
            print("Thank you for using Finance Tracker!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
