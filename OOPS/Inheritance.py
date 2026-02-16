# Single inheritance
# Parents --> child class - properties of parent class are acquired to child class
# create the object of child classes to bring inheritance in picture

#Parent class
class Employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def empdetails(self):
        print(self.name, self.empid)

# Child Class
class Manager(Employee):
    def approve_Leave(self):
        print("leave Approved")

m = Manager("Jay",45872)
m.empdetails()
m.approve_Leave()


# cerate a python program with class name savingsccount and functions
# deposit in parent class  and  addinterest in the child class

class SavingAccount:
    accNum = 12345
    val = 0

    def __init__(self, accountnum):

        self.accountNum = accountnum
        self.current_balance = 0
        if accountnum == self.accNum:
            print("Valid Account :) Carry On")
        else:
            self.val=1
            print("Invalid Account")


    def deposit(self, bal):
        if self.val==1:
            pass
        else:
            self.current_balance += bal
            print("Balance deposited")

    def currBal(self):
        if self.val == 1:
            pass
        print("Current Balance:", self.current_balance)


class AddInterest(SavingAccount):
    def addInterest(self, rate):
        interest = self.current_balance * rate / 100
        self.current_balance += interest
        print("Interest Added:", interest)



accNum = input()

A = AddInterest(accNum)

A.currBal()
deposit_Amount = 10000
Rate = 5
A.deposit(deposit_Amount)
A.currBal()

A.deposit(deposit_Amount)
A.currBal()
A.addInterest(Rate)
A.currBal()

