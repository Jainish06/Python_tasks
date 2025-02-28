class Employee :
    employees = []    #[{emp_id : [name, salary, role, extra_info]}]

    '''Show all employees'''
    def add_employees(self, employee_dict):
        self.employees.append(employee_dict)

    '''Prints details of all employees.'''
    def display_all_employees(self):
        print(self.employees)

    '''Filters and prints employees of a specific role (Manager/Developer)'''
    def filter_by_role(self, emp_role):
        emp_role_list = []
        for emp_info in self.employees:
            info_list = list(emp_info.values())
            if emp_role == info_list[0][2]:
                emp_role_list.append(info_list[0])
        print(f"Employees with {emp_role} are : {emp_role_list}")

    '''Filters and prints employees within a salary range.'''
    def filter_by_salary(self,min_salary,max_salary):
        emp_salary_list = []
        for emp_info in self.employees:
            info_list = list(emp_info.values())
            if min_salary <= info_list[0][1] <= max_salary:
                emp_salary_list.append(info_list[0])
        print(f"Employees within {min_salary} and {max_salary} salary range are : {emp_salary_list}")

emp_obj = Employee()

'''Employee Creation via User Input'''
def user_input():
    num_of_employees = int(input("Enter number of employees : \n"))
    while num_of_employees>0:
        emp_id = input("Enter employee ID : \n")
        name = input("Enter employee name : \n")
        salary = int(input("Enter employee salary : \n"))
        role = input("Enter employee role (Manager/Developer) : \n").capitalize()
        if role!='Manager' and role!= 'Developer':
            print("Invalid role entered. Entry skipped")
            continue
        extra_info = input("Enter employee's extra information (Department for Manager, Programming Language for Developer) : \n")
        emp_dict = {emp_id : [name,salary, role, extra_info]}
        emp_obj.add_employees(emp_dict)
        num_of_employees -= 1

def option_1() :
    user_input()

def option_2():
    emp_obj.display_all_employees()

def option_3() :
    role = input("Enter employee role (Manager/Developer) : \n").capitalize()
    emp_obj.filter_by_role(role)

def option_4():
    min_salary = int(input("Enter min salary : \n"))
    max_salary = int(input("Enter max salary : \n"))
    emp_obj.filter_by_salary(min_salary, max_salary)

options_dict = {
    1 : 'Add employees',
    2 : 'Display all employees',
    3 : 'Filter employees by role',
    4 : 'Filter employees by salary'
}

def check_option(n):
    match n:
        case 1 :
            option_1()
        case 2:
            option_2()
        case 3:
            option_3()
        case 4:
            option_4()

flag = True

while flag :
    print(f"Available operations : \n {options_dict}")
    num = int(input("Enter your option number : \n"))
    check_option(num)
    res = input("Do you want to continue (y/n) : \n").lower()
    if res == 'y':
        flag = True
    else:
        flag = False
