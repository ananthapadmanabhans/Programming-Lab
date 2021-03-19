class Bank:
    def __init__(self):
        self.name=input("Enter Depositor name")
        self.no=int(input("Account Number"))
        self.atype=input("Account Type")
        self.bal=0
        print("Account Created")
    def deposite(self):
        amount=int(input("Enter amount to deposite"))
        self.bal=self.bal+amount
        print("Amount Deposited:",amount)
        print("Balance:",self.bal)
    def withdraw(self):
        amount=int(input("Enter amount to withdraw"))
        self.bal=self.bal-amount
        print("Amount Withdrawed:",amount)
        print("Balance:",self.bal)
    def display(self):
        print("Name : ",self.name)
        print("Account no : ",self.no)
        print("Type of Account : ",self.atype)
        print("Balance : ",self.bal)

        


s=Bank()
s.deposite()
s.withdraw()
s.display()
s.copy()
        
        
