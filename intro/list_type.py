Months =["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(Months)
print(Months[-1])
print(Months[2])

x = "I am hungry this morning"

for n in x:
    print(n,end="_")

y = len(Months)
print("\n",y)

z=0
for n in Months:
    print(Months[z])
    z=z+1

print(Months.sort())
