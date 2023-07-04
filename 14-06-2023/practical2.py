class Bank:
    def __init__(self,acc_num,bal,customer_name):
         self.acc_num=acc_num
         self.bal=bal
         self.customer_name=customer_name
    def deposite(self,amount):
        self.bal += amount
        print("Deposite amount: ",amount)
    
    def print_detail(self):
        print("Account Number is:",self.acc_num)
        print("Balance is:",self.bal)
        print("Customer name is:",self.customer_name)
    
    def check_balance(self):
        print("Current balance is",self.bal)
b=Bank(100,1000,'dev')
b1=Bank(101,5000,'yash')
b2=Bank(102,2000,'raj')
b.print_detail()
b1.print_detail()
b2.print_detail()

print("-------------------------------------")
b1.print_detail()
b1.deposite(1000)
b1.check_balance()

print("-------------------------------------")
b2.print_detail()
b2.deposite(1000)
b2.check_balance()
