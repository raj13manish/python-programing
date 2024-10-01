# Problem statement: 
# You have a list of dictionaries where each dictionary contains a 
# student's name and a list of their grades:

students = [
    {'name': 'Alice', 'grades': [85, 92, 78]},
    {'name': 'Bob', 'grades': [88, 76, 90]},
    {'name': 'Charlie', 'grades': [95, 82, 89]}
]

# You need to compute the average grade for each student and 
# create a new dictionary where the keys are the student names and 
# the values are their average grades. 

# What will be the resulting dictionary?
average_grades={}
for i in students:
    name = i['name']
    grades = i['grades']
    average = round(sum(grades) / len(grades),2)  
    average_grades[name] = average
print(average_grades)
