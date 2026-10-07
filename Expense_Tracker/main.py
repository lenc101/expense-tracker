expenses = [
    {
        "description": "McDonald's",
        "amount": 250,
        "category": "Food"
    },
    {
        "description": "Train ticket",
        "amount": 120,
        "category": "Transport"
    },
    {
        "description": "Coffee",
        "amount": 60,
        "category": "Food"
    }
]

menu = {
    "1.": "Add expense",
    "2.": "View expenses",
    "3.": "View total",
    "4.": "View expenses by category",
    "5.": "Delete expense",
    "6.": "Exit"
}


def show_menu():

    for options, description in menu.items():
        print(options, description)

    option = input("\nChoose an option: ").strip()
    return option


def add_expense():

    new_expense = {}

    new_expense["description"] = input("What did you spend your money on?: ").strip()
    if not new_expense["description"]:
        print("Description cannot be empty!")
        return

    try:
        new_expense["amount"] = int(input("How much did it cost?: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if new_expense["amount"] <= 0:
        print("Amount must be greater than 0!")
        return

    new_expense["category"] = input("What category does this expense belong to?: ").strip()
    if not new_expense["category"]:
        print("Category cannot be empty!")
        return

    expenses.append(new_expense)


def view_expenses():

    for expense in expenses:
        print(
            expense["description"],
            "|",
            expense["amount"],
            "CZK",
            "|",
            expense["category"]
        )


def view_total():

    total = 0

    for expense in expenses:
        total = expense["amount"] + total

    print("Total:", total, "CZK")


def view_expenses_by_category():

    search = input("Search by category: ").strip()

    for expense in expenses:
        if expense["category"] == search:
            print(
                expense["description"],
                "|",
                expense["amount"],
                "CZK",
                "|",
                expense["category"]
            )


def delete_expense():

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            expense["description"],
            "|",
            expense["amount"],
            "CZK",
            "|",
            expense["category"]
        )

    try:
        option = int(input("Choose an expense to delete: ").strip()) - 1
    except ValueError:
        print("Please enter a valid number!")
        return

    if option < 0 or option >= len(expenses):
        print("Invalid expense number!")
        return

    expenses.pop(option)


while True:
    option = show_menu()

    if option == "1":
        add_expense()

    elif option == "2":
        view_expenses()

    elif option == "3":
        view_total()

    elif option == "4":
        view_expenses_by_category()

    elif option == "5":
        delete_expense()

    elif option == "6":
        break

    else:
        print("Invalid input! Please choose an option from 1 to 6.")