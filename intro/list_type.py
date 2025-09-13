Months =["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(Months)
print(Months[-1])
print(Months[2])

x = "I am hungry this morning"

for n in x:
    print(n,end="_")

y = len(Months)
print("\n",y)

"""
z=0
for n in Months:
    print(Months[z])
    z=z+1

print(Months[2:5]) #In a list the upper value is inclusive and the lowwer value is exclusive. Returns element 2, 3, 4

print(Months[:5]) #Starts from element 0 and resturns a list containing element 0, 1, 2, 3, 4

print(Months[0:]) #Prints all the elements in the list

print('Monday' in Months)

days_of_the_week=[10,  4, 5, 6, 80, 10000,]

print(days_of_the_week)

print(days_of_the_week.sort)


print(sorted(days_of_the_week))

Months.append('Monday')
print(Months)

Months[12] = 'Tuesday'

print(Months)

"""
dimensions = 10, 20, 30

dimensions1 = [10, 20, 30]

dimensions2 = (10, 20, 30)

dimensions3 = {10, 20, 30}

print(type(dimensions))

print(type(dimensions1))

print(type(dimensions2))

print(type(dimensions3))