#Part B
import random 
list = ["3", 1, 1.002, "floop", 4] 
x = random.choice(list) 
print(x)

#Part A
weeks = 16
classes_per_week = 5
tuition = 6000
cost_per_week = ((tuition / classes_per_week) / weeks)
print("This is your cost per class: ", cost_per_week/classes_per_week)
print("Cost per week:", cost_per_week)
print(weeks, type(weeks))
print(classes_per_week, type(classes_per_week))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))