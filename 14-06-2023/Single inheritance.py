class demo:
    def __init__(self,Customer_name,Customer_id):
        self.Customer_name=Customer_name
        self.Customer_id=Customer_id
    def display(self):
        print (f"Name of Customer is:{self.Customer_name}")
        print(f"Name of Customer is:{self.Customer_id}")

class demo1(demo):

    def print(self):
        print("this is only print function")

d=demo1('dev',20)
d.display()
d.print()