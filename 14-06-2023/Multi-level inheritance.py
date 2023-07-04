class demo:
    def __init__(self,employee_name,employee_id):

        self.employee_name=employee_name
        self.employee_id=employee_id

class demo1(demo):

    def __init__(self,employee_name,employee_id,employee_attendance,employee_payout):
        self.employee_attendance=employee_attendance
        self.employee_payout=employee_payout
        demo.__init__(self,employee_name,employee_id)


class demo2(demo1):
    def __init__(self, employee_name, employee_id, employee_attendance, employee_payout,employee_exp):
        self.employee_exp=employee_exp
        demo1.__init__(self, employee_name, employee_id, employee_attendance, employee_payout)

    def display(self):
        print(f"Name of Employee is: {self.employee_name}\n",f"Employee id is: {self.employee_id}")
        print(f"Name of Employee is: {self.employee_attendance}\n", f"Employee id is: {self.employee_payout}")
        print(f"Expirense of employee {self.employee_exp}")


d=demo2('dev',22,30,1500,6)
d.display()




