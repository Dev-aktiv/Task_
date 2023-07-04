class demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class demo1(demo):
    def __init__(self, x=1, y=2):
        super().__init__(x, y)
        self.xx = x
        self.yy = y

    def show(self):
        print("Sum is:",self.xx + self.yy)


class demo2(demo):
    def __init__(self, x=2, y=3):
        super().__init__(x, y)
        self.xx = x
        self.yy = y

    def show(self):
        print("Multiplication is:",self.xx * self.yy)


d = demo1()
d.show()
d=demo2()
d.show()
