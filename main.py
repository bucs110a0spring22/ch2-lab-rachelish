#Part B
import random 
list = ["3", 1, 1.002, "floop", 4] 
x = random.choice(list) 
print(x)

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(cost_per_week, type(cost_per_week))


