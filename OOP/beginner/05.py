#Add a __str__ method to BankAccount that shows account id and balance. Demonstrate with print(account).
class BankAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance
    
    def __str__(self):
        print("The account id: ",self.account_id)
        print("The balance id: ",self.balance)

s1= BankAccount(5323230,6000)
s1.__str__()