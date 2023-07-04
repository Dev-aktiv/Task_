class demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_area(self):
        print(self.x * self.y)
class demo1(demo):
    def __init__(self, x, y):
        self.Aa = x
        self.Bb = y
        super().__init__(x, y)

    def find_area(self):
        demo.find_area(self)
        print(3.14 * self.Aa * self.Bb)


demo2 = demo1(2, 3)
demo2.find_area()