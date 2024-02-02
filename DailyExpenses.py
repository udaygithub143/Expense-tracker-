# Function to get user input for daily expenses
def get_expense_input():
    amount = float(input("Enter the amount spent: $"))
    description = input("Enter a brief description: ")
    category = input("Enter the category of expense: ")
    return {"amount": amount, "description": description, "category": category}
 
# Function to save expense data to a text file
def save_expense(expense):
    with open("expenses.txt", "a") as file:
        file.write(f"{expense['amount']},{expense['description']},{expense['category']}\n")
 
# Main function to test the functionality
def main():
    while True:
        expense = get_expense_input()
        save_expense(expense)
        choice = input("Do you want to add another expense? (yes/no): ")
        if choice.lower() != 'yes':
            break
 
if __name__ == "__main__":
    main()