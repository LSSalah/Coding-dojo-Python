class User:
    def __init__(self,first_name,last_name,account_balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account_balance
    
    def make_withdraw (self, amount):
        self.account -= amount

    def make_deposite(self , amount):
        self.account += amount
    
    def display_account_info(self):
        print(f"Name : {self.first_name}, Balance : {self.account}")

sal = User("Salah" , "Abu Karsh" , 1000)
man = User("Manar" , "Hasan" , 400)
moh = User("Mohammad" , "Hussinie" , 500)

moh.make_deposite(200)
moh.make_deposite(200)
moh.make_deposite(200)
moh.make_withdraw(300)
moh.display_account_info()

man.make_deposite(100)
man.make_deposite(100)
man.make_withdraw(50)
man.make_withdraw(100)
man.make_withdraw(50)
man.display_account_info()

sal.make_deposite(300)
sal.make_withdraw(100)
sal.make_withdraw(200)
sal.make_withdraw(50)
sal.display_account_info()

