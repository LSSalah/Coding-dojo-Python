class User:
    def __init__(self,first_name,last_name,account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account_balance
        

    
    def make_withdraw (self, amount):
        self.account -= amount
        return self

    def make_deposite(self , amount):
        self.account += amount
        return self

    def display_amount(self):
        print(self.account)


sal = User("Salah" , "Abu Karsh" , 1000)
man = User("Manar" , "Hasan" , 400)
moh = User("Mohammad" , "Hussinie" , 500)

moh.make_deposite(200).make_deposite(200).make_deposite(200).make_withdraw(300).display_amount()

man.make_deposite(100).make_deposite(100).make_withdraw(50).make_withdraw(100).make_withdraw(50).display_amount()

sal.make_deposite(300).make_withdraw(100).make_withdraw(200).make_withdraw(50).display_amount()

