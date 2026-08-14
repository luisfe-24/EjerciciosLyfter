class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount
        print("Monto ingresado con exito")

    def withdraw_money(self, amount):
        self.balance -= amount
        print("Monto retirado con exito")


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):

        if (self.balance - amount) < self.min_balance:
            raise ValueError("No puede retirar: supera el monto minimo")

        super().withdraw_money(amount)


my_account = SavingsAccount(10, 5)

my_account.withdraw_money(5)

my_account.deposit_money(10)

my_account.withdraw_money(11)
