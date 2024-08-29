class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} a été déposé sur le compte de {self.account_holder}.")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} a été retiré du compte de {self.account_holder}.")
            else:
                print("Fonds insuffisants pour cette opération.")
        else:
            print("Le montant du retrait doit être positif.")

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}, Solde : {self.balance:.2f} euros")


account = BankAccount("Alice", 100.0)
account.display_balance()

account.deposit(50)
account.display_balance()

account.withdraw(30)
account.display_balance()

account.withdraw(150)
account.display_balance()
