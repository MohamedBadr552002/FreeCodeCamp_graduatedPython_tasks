class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    #identify the deposit
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=""):
        #Check there is fund or not
        if self.check_funds(amount):
            #store it as a negative number
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output
    


def create_spend_chart(categories):
    # Calculate percentage spent for each category
    total_spending = 0
    percentage_spent = {}
    for category in categories:
        category_spending = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spending -= item["amount"]
                total_spending -= item["amount"]
        percentage_spent[category.name] = category_spending

    # Calculate percentage spent rounded down to the nearest 10
    for category in percentage_spent:
        percentage_spent[category] = int((percentage_spent[category] / total_spending) * 100)
        percentage_spent[category] = percentage_spent[category] // 10 * 10

    # Create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += "{:>3d}| ".format(i)
        for category in categories:
            if percentage_spent[category.name] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    "
    chart += "-" * (len(categories) * 3 + 1)
    chart += "\n"
    max_len = max([len(category.name) for category in categories])
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    return chart[:-1]
