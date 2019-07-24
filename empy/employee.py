class Employee:
    def __init__(self,empno,ename,qualification,salary,dept_name):
        self.empno=empno
        self.ename=ename
        self.qualification=qualification
        self.salary=salary
        self.dept_name=dept_name

    def show_info(self):
        print(f"{self.empno}-{self.ename}-{self.qualification}-{self.salary}-{self.dept_name}")
    def increment_salary(self,inc_amoount):
        self.salary+=inc_amoount
        print(f"{self.ename} salary after increment:{self.salary}")