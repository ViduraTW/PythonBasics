
first_name = input("What is your first name?")
last_name = input("What is your last name?")

print(last_name + " " + first_name)


first_number = input("What is the first number?")
second_number = input("What is the second number?")

print(int(first_number)+int(second_number))


chickens = input("How many Chickens?")
chicken_legs = 2*int(chickens)

cows = input("How many Cows?")
cow_legs = 4*int(cows)

pigs = input("How many pigs?")
pig_legs = 4*int(pigs)

sum_of_legs = chicken_legs+cow_legs+pig_legs


print("The sum of the legs across all animals is " + str(sum_of_legs))

num_1 = int(input("First number?"))
num_2 = int(input("Second number?"))
num_3 = int(input("Third number?"))

if num_1 == num_2 == num_3:
    print(num_1*3)
else:
    print(num_1+num_2+num_3)


grade = int(input("Grade?"))

if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
elif grade < 60:
    print("F")

year = int(input("Year?"))

if year%4 == 0:
    print("Leap Year")
else:
    print("Not a leap Year")















































