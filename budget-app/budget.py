class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        s = self.name.center(30, '*') + '\n'
        for d in self.ledger:
            s += f"{d['description'][:23]:<23}{d['amount']:>7.2f}\n"
        s += f'Total: {self.get_balance()}'
        return s

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(d['amount'] for d in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True


def create_spend_chart(categories):
    total_spend = sum(abs(d['amount']) if d['amount'] < 0 else 0 for category in categories for d in category.ledger)
    total_spend = round(total_spend, 2)
    category_names = [category.name for category in categories]
    categories_spend = []

    for category in categories:
        category_spend = 0
        for d in category.ledger:
            if d['amount'] < 0:
                category_spend += abs(d['amount'])
        categories_spend.append(round(category_spend, 2))

    percent_spend_category = [int(round((spend/total_spend) * 100, -1)) for spend in categories_spend]
    chart = 'Percentage spent by category\n'

    for n in range(100, -10, -10):
        chart += f'{n:>3}|'
        for i, percentage in enumerate(percent_spend_category):
            if n <= percentage:
                chart += ' o '
            else:
                chart += ' ' * 3
        chart += ' \n'

    chart += ' ' * 4 + '-' * (pow(len(categories), 2) + 1) + '\n' + ' ' * 4

    for i in range(0, len(max(category_names, key=len))):
        for k, name in enumerate(category_names):
            if len(name) - 1 >= i:
                chart += f' {name[i]} ' if k < len(category_names) - 1 else f' {name[i]}  '
            else:
                chart += ' ' * 3 if k < len(category_names) - 1 else ' ' * 4
        chart += '\n' + ' ' * 4 if i < len(max(category_names, key=len)) - 1 else ''

    return chart
