#Write a BankAccount class with deposit(amount), withdraw(amount) and get_balance(). Add basic error check for overdraft.
class BankAccount:
    def __init__(self,amount):
        self.amount = amount

    def deposit(self, deposit):
        self.deposit= deposit
        if deposit <0:
            print("The deposit cannot be negative. ")
        else:
            self.amount = self.amount + self.deposit

    def withdraw(self, withdraw):
        self.withdraw= withdraw
        if withdraw > amount:
            print("You cannot withdraw more than amount. ")
        else:
            self.amount= self.amount - self.withdraw

    def get_balance(self):
        print(f"The final amount after transation is {amount}")
        
amount= int(input("Enter a total amount in yr bank: "))
a1= BankAccount(amount)
question= input("Enter deposit if you wanna deposit, and withdraw if you wanna withdraw")
if question == "deposit":
    deposit= int(input("Enter a deposit money: "))
    a1.deposit(deposit)
    print(f"The final amount is{amount+deposit}")

else:
    withdraw= int(input("Enter a withdraw money: "))
    a1.withdraw=withdraw
    print(f"The final amount is{amount-withdraw}")