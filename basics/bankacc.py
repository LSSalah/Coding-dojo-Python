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
		self.account=self.account+(self.account * self.int_rate)
		return self
		

sal = BankAccount(0.001 , 1000)
man = BankAccount(0.002 ,  400)
sal.deposit(300).deposit(100).deposit(200).withdraw(100).yield_interest().display_account_info()
man.deposit(300).deposit(100).withdraw(200).withdraw(50).withdraw(100).withdraw(150).yield_interest().display_account_info()
