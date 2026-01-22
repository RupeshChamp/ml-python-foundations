#DAY 1 – ML Foundations
#Part A: Python Concepts Required for ML
from fcntl import FASYNC

from pandas.tseries.holiday import after_nearest_workday

#Variables & Data Types (ML View)
name = "Rupesh" #String
age =28         #Int
salary = 10000.50  #Float
is_married = False

print(f"Name: {name}\t Type: {type(name)}")
print(f"Age: {age} \t Type: {type(age)}")
print(f"Salary: {salary}\t Type: {type(salary)}")
print(f"Is Married: {is_married}\t Type: {type(is_married)}")


#Lists vs Tuples vs Dictionaries
# List – ordered, changeable
hours_worked_per_week = [8, 9, 8, 10, 7]
employee_data = ["Rupesh", 27, 10000.50, False] # list is collection of all data type
print(f"\nHours worked per week: {hours_worked_per_week}\t Type: {type(hours_worked_per_week)}")
print(f"Employee Data: {employee_data}")

# Tuple – ordered, NOT changeable
resolutions = (1920, 1080)
print(f"\nResolutions: {resolutions}\t Type: {type(resolutions)}")
print(f"Count of Data: {resolutions.count(1920)}")
print(f"Index of the Data: {resolutions.index(1920)}")

#Dictionary – KEY for ML configs,feature mappings, model parameters
employee = {"name": "Rupesh", "age": 28, "salary": 10000.50, "is_married": False,"hours_worked_per_week": [8, 9, 8, 10]}
print(f"\nEmployee data: {employee}\t Type: {type(employee)}")
print(f"Key: {employee.keys()}")
print(f"Value: {employee.values()}")
print(f"Items: {employee.items()}\n")

#Loops -> for, while

for key, value in employee.items():
    print(f"{key}: {value}")
    if value == "Rupesh":
        employee["salary"] = 20000
print(f"\nEmployee data updated: {employee}")

#Functions (ML Building Blocks)
def calculate_productivity(hours, breaks):
    return hours - (breaks * 0.5)

obj = calculate_productivity(9,1)
print(f"\nProductivity: {obj}")

#Lambda Functions -> anonymous function used everywhere

score = lambda mark1, mark2, mark3, mark4, mark5: (mark1 + mark2 +mark3 + mark4 +mark5)/5
print(f"\nAverage mark achieved: {score(60, 70, 50, 80, 90)}")

def myfunc(n):
  return lambda a : a ** n

squaring = myfunc(2)

print(squaring(9))

#List Comprehension

actual_working_hours = [hr-1 for hr in hours_worked_per_week ]
print(f"Actual working hours: {actual_working_hours}")
less_working_hours = [l_hr for l_hr in actual_working_hours if l_hr <= 8]
print(f"Less working hours: {less_working_hours}")

#File Handling

