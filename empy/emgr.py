from employee import Employee

lst_emp=[]
def load_emp():
    with open("emp.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno=int(edata[0])
            ename=edata[1]
            qualification=edata[2]
            salary=int(edata[3])
            dept_name=edata[4]
            emp=Employee(empno,ename,qualification,salary,dept_name)
            lst_emp.append(emp)
    print(f"total employees count:{len(lst_emp)}")

def showDeptNmaes():
    dnames=set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)
def showAllQualification():
    qualification=set(map(lambda emp:emp.qualification,lst_emp))
    for qual in qualification:
        print(qual)
def maxSalaryEmp():
    max_salary=max(list(map(lambda emp:emp.salary,lst_emp )))
    lst=list(filter(lambda x:x.salary==max_salary,lst_emp))
    for emp in lst:
        emp.show_info()
    
def showEmpCountByDeptName():
    pass
def showTotalByDeptName():
    pass
def showEmpCountByQual():
    pass


load_emp()
print("all departments name:")
showDeptNmaes()
print("all qualification:")
showAllQualification()
print("max salary:")
maxSalaryEmp()
