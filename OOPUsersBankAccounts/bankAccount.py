class BankAccount:
  allAccounts =[]
  def __init__(self, name, intRate = .02, amount = 0): 
    self.accountName = name.title()
    self.int_rate = intRate
    self.balance = amount
    BankAccount.allAccounts.append(self)

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if self.balance < amount:
      self.balance -= 5
      print("Insufficient funds: Charging a $5 fee")
    else:
      self.balance -= amount
    print(f"Withdrew: ${amount}") 
    self.display()
    return self

  def display(self):
    print(f"{self.accountName} Balance: {self.balance} -- At {self.int_rate} interest.")
    return self

  def interestYield(self):
    if self.balance >= 0:
      print(f"You've earned {(self.balance * self.int_rate)} in interest.")
      self.balance += (self.balance * self.int_rate)
    return self

  @classmethod
  def displayAll(cls):
    print(f"{len(cls.allAccounts)} Total Accounts")
    for i in cls.allAccounts:
      i.display()
    return cls

# account1 = BankAccount("checking", .03)
# account2 = BankAccount("savings", .01)
# account3 = BankAccount("checking", .04)
# account4 = BankAccount("checking", .05)
# account1.deposit(100).deposit(1200).deposit(10000).withdraw(1000).interestYield().display()
# account2.deposit(100000).deposit(100000).withdraw(8000).withdraw(2000).interestYield().display()

# BankAccount.displayAll()