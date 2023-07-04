# class demo:
#     def __init__(self,var1,var2):
#         self.var1=var1
#         self.var2 = var2
#
#     def calculate(self):
#         print(self.var1+self.var2)
# class demo1(demo):
#
#
#     def calculate(self,var1,var2):
#         super().__init__(var1, var2)
#         print(self.var1+self.var2)
#
# demo2=demo1()
# demo2.calculate(2,3)
class demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_area(self):
        print(self.x * self.y)
class demo1(demo):
    def __init__(self, a, b, x, y):
        self.Aa = a
        self.Bb = b
        super().__init__(x, y)

    def find_area(self):
        demo.find_area(self)
        print(3.14 * self.Aa * self.Bb)


demo2 = demo1(2, 3, 2, 3)
demo2.find_area()
