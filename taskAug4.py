def get_sum(number1, number2, number3):
    """
    calculates sum of three numbers ,if numbers are equal ,calculate three times of sum
    :param number1: integer giving first number
    :param number2: integer giving second number
    :param number3: integer giving third number
    :return: sum of numbers or three times sum of numbers
    O(1) time and O(1) space
    """
    if number1 == number2 and number2 == number3:
        return (number1+number2+number3)*3
    return number1+number2+number3


num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
num3 = int(input("Enter number3:"))
print("Sum is:", get_sum(num1,num2,num3))


class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print("Total employee", Employee.emp_count)

    def display_employee(self):
        print("Name", self.name, ",Salary:", self.salary)


emp1 = Employee("Zara", 2000)
emp1.display_employee()
emp1.display_count()
emp2 = Employee("Manni", 5000)
emp2.display_employee()
emp1.display_count()
emp1.age = 7
print(hasattr(emp1, 'age'))
print(getattr(emp1, 'age'))
