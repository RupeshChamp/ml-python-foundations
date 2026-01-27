# DAY 1 – CSV & JSON File Handling (with Dataset)

""""
We’ll learn:

What CSV & JSON are actually used for

How to read / write / update them

How ML workflows depend on them

Real datasets you can immediately practice on

"""
import os.path

""""
1. CSV FILES (Comma Separated Values)
What is a CSV?

A CSV is a table stored as text.
"""

import csv

# with open("employee.csv", "a", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow([7, "Akshaya", 26, "HR", 100000])

with open("employee.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row)

with open("employee.csv", "r") as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)

    for row in csv_dict_reader:
        print(f" {row['name']} : {row['salary']}")
        # for col, value in row.items():
            # print(f"Key: {col}, Value: {value}")

# Filtering a data from the csv file

with open("employee.csv", "r") as csv_file:
    csv_reader2 = csv.DictReader(csv_file)
    #finding the higher salary among the employees
    print()
    # for row in csv_reader2:
    #     if int(row['salary']) >= 80000:
    #         print(f" {row['name']} : {row['salary']}")

    high_salary = [f" {row['name']} : {row['salary']}" for row in csv_reader2 if int(row['salary']) >= 60000]
    print(high_salary)

#sorting a csv file in python

with open ("employee.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)
    print(rows)

rows.sort(key=lambda x: int(x['salary']))

print("Sorted rows:", rows)
# for row in rows:
with open("ordered_employee.csv", "w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=rows[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(rows)

with open ("ordered_employee.csv", "r") as csv_file:
    csv_file_ordered = csv.reader(csv_file)
    for row in csv_file_ordered:
        print(row)



import csv

x = [["Indira", 25, 25000], ["Preethi", 25, 25000]]
file_exist = os.path.exists("prac_data.csv")
with open("prac_data.csv","a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    header = ["name", "age", "salary"]
    if not file_exist:
        writer.writerow(header)
    writer.writerows(x)

with open("prac_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        print(row)

with open("prac_data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        if row["name"] == "Indira":
            print(row["salary"])

# y = {"name": "Livya", "age": 26, "salary": 30000}
#
# with open("prac_data.csv", "a", newline="") as csvfile:
#     reader = csv.DictWriter(csvfile, fieldnames=["name", "age", "salary"])
#     if not os.path.exists("prac_data.csv"):
#         reader.writeheader()
#     reader.writerow(y)

with open("prac_data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    final_data = list(reader)

final_data.sort(key=lambda x: x["age"])

final_data.sort(key=lambda x: x["salary"], reverse=True)
print(final_data)

with open("order_practice.csv", "a", newline="") as csvfile:
    reader = csv.DictWriter(csvfile, fieldnames=final_data[0].keys())
    if not os.path.exists("order_practice.csv"):
        reader.writeheader()
    reader.writerows(final_data)
with open("order_practice_salary.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=final_data[0].keys())
    if not os.path.exists("order_practice_salary.csv"):
        reader.writeheader()
    writer.writerows(final_data)

import csv
import os

#Increase salary by 10% and save to new CSV
with open("employee.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    new_row = []
    for row in reader:
        if row['salary'].isdigit():
            new_salary = int(row['salary']) + (int(row['salary']) * 10/100)
            row['salary'] = int(new_salary)
            new_row.append(row)

if not new_row:
    print("Updated employee salary: ", new_row)

new_row.sort(key=lambda x: int(x['age']))
with open ("Employee_Incremented_Data.csv", "w", newline='') as csvfile1:
    writer1 = csv.DictWriter(csvfile1, fieldnames=new_row[0].keys())
    # if not os.path.exists("Employee_Incremented_Data.csv"):
    writer1.writeheader()
    writer1.writerows(new_row)
