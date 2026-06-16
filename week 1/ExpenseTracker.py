import json
import os
DATA_FILE = "expenses.json"
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=2)

def read_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please type a number, like 250.")
def add_expense(expenses):
    amount = read_number("Amount spent: ")
    category = input("Category (food, travel, etc.): ")
    date = input("Date (YYYY-MM-DD), e.g. 2026-06-14: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense saved!\n")

def show_all(expenses):
    if len(expenses) == 0:
        print("No expenses yet.\n")
        return

    print("\n----- All Expenses -----")
    for expense in expenses:
        print(expense["date"], "|", expense["category"], "|", expense["amount"])
    print()


def monthly_total(expenses):
    month = input("Enter month (YYYY-MM), e.g. 2026-06: ")

    total = 0
    for expense in expenses:
        if expense["date"].startswith(month):
            total = total + expense["amount"]

    print("Total spent in", month, "is", total, "\n")

def category_spending(expenses):
    if len(expenses) == 0:
        print("No expenses yet.\n")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in totals:
            totals[category] = totals[category] + amount
        else:
            totals[category] = amount

    print("\n----- Spending by Category -----")
    for category in totals:
        print(category, ":", totals[category])
    print()


def main():
    expenses = load_expenses()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Monthly total")
        print("4. Spending by category")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_all(expenses)
        elif choice == "3":
            monthly_total(expenses)
        elif choice == "4":
            category_spending(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1-5.\n")
main()
