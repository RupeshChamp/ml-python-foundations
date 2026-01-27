# 🧠 Python Fundamentals – Practical Practice (ML Context)
# 🟢 Level 1 – Warm-up (Must be instant)

"""
Q1. Feature Scaling (List)
Given working hours of employees, increase every value by 1 without using a loop.
"""

hours = [6, 7, 8, 9]

updated_hours = [hour+1 for hour in hours]
print("updated hours: ", updated_hours)

# expected = [7, 8, 9, 10]

"""
Q2. Filter data
From the list, keep only hours greater than 7.
"""

filter_hours = [hour for hour in updated_hours if hour > 7]
print("filtered hours: ", filter_hours)

"""
Q3. Convert categorical to numeric
"""

labels = ["yes", "no", "yes", "no"]

numeric_labels = [1 if lab == "yes"  else 0 for lab in labels ]

print(numeric_labels)

#🟡 Level 2 – Core ML Logic

"""
Q4. Feature engineering
"""

data = [
    {"hours": 8, "breaks": 2},
    {"hours": 6, "breaks": 3},
    {"hours": 9, "breaks": 1}
]

productivity = []
for data in data:
    hours = data["hours"]
    breaks = data["breaks"]
    prod = hours - (breaks *0.5)
    productivity.append(prod)
print("Productivity: ", productivity)

productivity = [
    item for item in data
]
print(productivity)

# productivity = hours - (breaks * 0.5)

