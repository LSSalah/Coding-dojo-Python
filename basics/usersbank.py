class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

class BankAccount:
	def __init__ (self , int_rate, balance):
		self.account = balance
		self.int_rate = int_rate
		
	def deposit(self, amount):
		self.account += amount
		return self
	
	def withdraw(self, amount):
		self.account -= amount
		return self

	def display_account_info(self):
		print(self.account)

	def yield_interest(self):
		self.account * self.int_rate
		return self

sal = User("Salah Abu Karsh", "gsdhdf@email.com" )
man = User("Manar Hasan", "gsdhdf@email.com" )
moh = User("Mohammad Hussinie", "gsdhdf@email.com")



