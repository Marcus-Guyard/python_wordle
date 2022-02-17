class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"

            total += item['amount']
        output = title + items + "Total: " + str(total) + "\n"
        return output

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_currency = 0
        for item in self.ledger:
            total_currency += item['amount']

        return total_currency

    def transfer(self, amount: float, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def get_withdraw(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total += item['amount']
        return total


def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    # Retrieve total expense of each category
    total = 0
    expenses = []
    names = []
    len_names = 0

    for item in categories:
        expense = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
        total += expense

        if len(item.name) > len_names:
            len_names = len(item.name)

        expenses.append(expense)
        names.append(item.name)

    # Convert to percent + pad names
    expenses = [(x / total) * 100 for x in expenses]
    names = [label.ljust(len_names, " ") for label in names]

    # Format output
    for c in range(100, -1, -10):
        output += str(c).rjust(3, " ") + '|'
        for x in expenses:
            output += " o " if x >= c else "   "
        output += " \n"

    # Add each category name
    output += "    " + "---" * len(names) + "-\n"

    for i in range(len_names):
        output += "    "
        for label in names:
            output += " " + label[i] + " "
        output += " \n"

    return output.strip("\n")


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print("here")
print(clothing)

print(create_spend_chart([food, clothing, auto]))


