class parent1:
    def __int__(self,x,y):

        self.x=x
        self.y=y
    def sum(self):

        print("Sum of number is:",self.x+self.y)

class parent2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def multiply(self):
        print("Multiplication of number is:",self.x*self.y)

class child(parent1,parent2):

    def __init__(self,x,y):
        self.x=x
        self.y=y

c=child(10,2)
c.sum()
c.multiply()


