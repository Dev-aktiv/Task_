#Inheritance practical
class demo:
	def __init__(self,student,student_id):
		self.student=student
		self.student_id=student_id
	def test1(self):
		print(self.student)
		print(self.student_id)
class demo1(demo):
	def __init__(self,student,student_id,school_name,Area):
		self.school_name=school_name
		self.Area=Area
		print(self.school_name)
		print(self.Area)
		demo.__init__(self,student,student_id)# this is calling by class name
demo2=demo1('dev',22,'DD-group','jivraj')
demo2.test1()

