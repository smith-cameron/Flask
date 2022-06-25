class User:
  def __init__(self, firstName, lastName, email, age, memberStatus = False):
    self.first_name = firstName
    self.last_name = lastName
    self.email = email
    self.age = age
    self.is_rewards_member = memberStatus
    self.points = 0

  def display(self):
    print(f"User Info: \n First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Age: {self.age}")
    if self.is_rewards_member == True:
      print(f"Your Gold Card Points: {self.points}")
    else:
      print("What's in YOUR wallet?")
    return self

  def enroll(self):
    if self.is_rewards_member == False:
      self.is_rewards_member = True
      self.points += 200
    else:
      print("You are already enrolled")
    return self
  
  def spendPoints(self, amount):
    if self.points >= amount:
      self.points -= amount
    else:
      print("Your withdraw request exceeds your balance.")
    return self

# user1 = User("Cameron", "Smith", "cs@email.com", 33)
# user1.display().enroll().display().enroll()
# user2 = User("Ben", "Jammin", "bj@email.com", 48)
# user3 = User("Timmy", "Jimmy-Jam", "tjj@email.com", 32)
# user2.enroll().spendPoints(180).spendPoints(50).display()
# user3.enroll().spendPoints(50).display()