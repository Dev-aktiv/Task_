#init method
class demo:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def sum(self):
		print("sum of value is:",self.a + self.b)
	def average(self):
		print("avarage is:",(self.a+self.b)/2)
demo1=demo(10,20)
demo1.sum()
demo1.average()

		
