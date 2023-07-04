class demo:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def sum(self):
		print(self.a+self.b)
class demo1(demo):
	def __init__(self,a,b):
		self.Aa=a
		self.Bb=b
		super().__init__(a, b)
	def average(self):
		print((self.Aa+self.Bb)/2)
demo2=demo1(10,20)
demo2.sum()
demo2.average()
