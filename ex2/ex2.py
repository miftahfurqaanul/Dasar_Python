import math
#task 1
print("Task 1")
x = 4
y = 3
z = 2
w = ((x+y+z)/(x*y))**2
print("w = ", w)

#task 3
print("Task 3")
day=input("your days are numbered:")
days=float(day)
weeks=days/7
months=days/30
years=days/30
print(days, "days")
print(weeks, "weeks")
print(months, "months")
print(years, "years")

#task 4
print("task 4")
budi = 49/(1+0.4)#andi + budi = 49, andi / budi 0.4
andi = 49-budi
andi2 = andi+2
budi2 = budi+2
print("Andi is", andi, "y.o., and will be", andi2, "y.o. in 2 years")
print("budi is", budi, "y.o., and will be", budi2, "y.o. in 2 years")

#task 5
print("task 5")
sum_s = 60+40
t = 120/sum_s
m = (t-1)*60
print("Cars A and B will collide at", int(9+t), ":", int(math.ceil(m)), "wib")
