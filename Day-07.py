class Expense:
    def __init__(self,amount,category):
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {'amount':self.amount,'category':self.category}

import json
def load_expenses(filename="expenses.json"):
    try:
        with open(filename,"r") as f:
            data = json.load(f)
            return [Expense(item["amount"],item["category"]) for item in data]
    except FileNotFoundError:
        return []
def save_expenses(expenses,filename="expenses.json"):
    with open(filename,"w") as f:
        json.dump([e.to_dict()for e in expenses],f)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append(Expense(amount,category))
        print("Expenses saved!")
    except ValueError:
        print(" Invalid amount, Please enter numeric value")
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet!")
    for e in expenses:
        print(f"{e.category}: {e.amount}")
def total_spent(expenses):
    return sum(e.amount for e in expenses)


def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add expense\n2. View expenses\n3. Total spent\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print(f"Total spent: {total_spent(expenses)}")
        elif choice == "4":
            save_expenses(expenses)
            print("Saved. Bye👋")
            break
        else:
            print("Invalid choice, please try again")
main()
