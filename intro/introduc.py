

# print("Hello World"," ", 1, 2, 3, sep='|', end='.', flush=True, )

"""

The print funtion outputs the values that it is given. It has a couple of arguments:
*Separator (sep): This determines the sepatator between values passed to the print. The default is space " "- if no value is passed.
*end: Defines the end of the line parament. Default is the new line character. Always pass the new line character if another end parameter is defined.

"""

#VARIABLES

a, b, c = "Banana", "Apple", "Orange" #Variable assignment using a single line

# print("\n",a,b,c, "\n")

#full_name = str (input("Type your full name: "))

#full_name=full_name.upper() #same as print(fullname.upper())

# print(full_name, "\n")


test_numbers=range(1,10,2)
print(test_numbers)


x=1
x +=3
print(x)

y=40
y-=5
print(y)

z=15
z*=2
print(z)

"""

user_input=str(input("Please enter a text: "))

len_user_input=len(user_input)
print("The text is ", len_user_input, "characters long")

print("Please enter a value less than: ", len_user_input)
user_input_len=int(input())
user_input_len-=1
print(user_input[user_input_len])




num_x=10
num_y=2
results=num_x**num_y
print(results)
num_y=4
print(num_y)

"""

#Strings and using the format printer

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: write a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

# String Formatting

message = username + " " + "really accessed the site" + " " + url + " " + timestamp #replace with your code
message2= "{} accessed the site {} at {}"

print(message)
print(message2.format(username, url, timestamp))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

#Another implementation using F Strings Below:

print(f"MY name is {username} and I visited the website {url} at {timestamp}")

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(len(verse))
#print(verse.split())
#print(verse.split(sep='none', maxsplit=1))

#What is the index of the first occurrence of the word 'and' in verse?
print(verse.find("and"))

#What is the index of the last occurrence of the word 'you' in verse?
print(verse.rfind("you"))

#What is the count of occurrences of the word 'you' in the verse?
print(verse.count("you"))

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))
