expenses = []

def add_expense(amount, category, date):
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added successfully.")

def remove_expense(index):
    if 0 <= index < len(expenses):
        del expenses[index]
        print("Expense removed successfully.")
    else:
        print("Invalid index.")

def view_expenses():
    if expenses:
        for i, expense in enumerate(expenses):
            print(f"{i+1}. Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")
    else:
        print("No expenses to display.")

while True:
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. View Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = input("Enter the amount: ")
        category = input("Enter the category: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        add_expense(amount, category, date)

    elif choice == "2":
        view_expenses()
        index = int(input("Enter the index of the expense to remove: ")) - 1
        remove_expense(index)

    elif choice == "3":
        view_expenses()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please choose again.")
