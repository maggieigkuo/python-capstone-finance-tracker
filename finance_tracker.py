print("Welcome to the Personal Finance Tracker!")

#Creating the dictionary to organize expenses by category
expenses_by_category = {}

#Defining the function to view all expenses
def view_expenses(expenses_by_category):
    for category, expenses in expenses_by_category.items():
        print(f"Category: {category}")
        for description, amount in expenses: 
            print(f"{description}: ${amount:.2f}")

#Defining the function to view summary by category
def view_summary(expenses_by_category):
    print("Summary:")
    for category, expenses in expenses_by_category.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

#While loop to create a menu setting
while True:
    print("Choose an option:")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("No empty descriptions")
        
        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("NO empty category")
        
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Enter a number.")
            continue

        expense = (description, amount)
        if category not in expenses_by_category:
            expenses_by_category[category] = []
        expenses_by_category[category].append(expense)
        
        print("Expense added successfully.")

    elif choice == "2":
        view_expenses(expenses_by_category)

    elif choice == "3":
        view_summary(expenses_by_category)
    
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Choose another number!")