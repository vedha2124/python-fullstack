
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []  

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be more than zero.")
            return
        self.balance = self.balance + amount
        self.history.append("Deposited " + str(amount))
        print("Deposited", amount, "| Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be more than zero.")
            return
        if amount > self.balance:
            print("Not enough money. Balance is", self.balance)
            return
        self.balance = self.balance - amount
        self.history.append("Withdrew " + str(amount))
        print("Withdrew", amount, "| Balance:", self.balance)

    def show_history(self):
        print("\n--- History for", self.owner, "---")
        if len(self.history) == 0:
            print("No transactions yet.")
        for line in self.history:
            print("-", line)
        print("Current balance:", self.balance)
class Bank:
    def __init__(self):
        self.accounts = {}  

    def create_account(self, name):
        if name in self.accounts:
            print("That account already exists.")
            return
        self.accounts[name] = Account(name)
        print("Account created for", name)
    def get_account(self, name):
        if name in self.accounts:
            return self.accounts[name]
        print("No account found for", name)
        return None
    def transfer(self, from_name, to_name, amount):
        sender = self.get_account(from_name)
        receiver = self.get_account(to_name)
        if sender is None or receiver is None:
            return
        if amount <= 0:
            print("Amount must be more than zero.")
            return
        if amount > sender.balance:
            print("Not enough money to transfer.")
            return
        sender.balance = sender.balance - amount
        receiver.balance = receiver.balance + amount
        sender.history.append("Transferred " + str(amount) + " to " + to_name)
        receiver.history.append("Received " + str(amount) + " from " + from_name)
        print("Transferred", amount, "from", from_name, "to", to_name)


def read_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please type a number.")
def main():
    bank = Bank()
    while True:
        print("\n===== Bank Menu =====")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Show history")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Account name: ")
            bank.create_account(name)
        elif choice == "2":
            name = input("Account name: ")
            account = bank.get_account(name)
            if account is not None:
                amount = read_number("Amount to deposit: ")
                account.deposit(amount)
        elif choice == "3":
            name = input("Account name: ")
            account = bank.get_account(name)
            if account is not None:
                amount = read_number("Amount to withdraw: ")
                account.withdraw(amount)
        elif choice == "4":
            from_name = input("From account: ")
            to_name = input("To account: ")
            amount = read_number("Amount to transfer: ")
            bank.transfer(from_name, to_name, amount)
        elif choice == "5":
            name = input("Account name: ")
            account = bank.get_account(name)
            if account is not None:
                account.show_history()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1-6.")
main()