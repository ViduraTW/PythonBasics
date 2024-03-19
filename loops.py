

#while loops
#this will always be running since until the conditions are no longer met


i = 1

while i <= 10:
    print(i)
    i = i +1

# this command will occur when the while loop is finished
print("Done")


secret_number = 8
guess = 0
tries = 0

while tries < 3 and guess != secret_number:
    guess = int(input("guess a number between 1 and 10"))
    tries = tries + 1

if guess == secret_number:
    print("You won")
else:
    print("you lost")



fruits = ["apple", "mango", "banana", "pear"]
name = "Mike"

for item in fruits:
    print(item)

for i in name:
    print(i)


#the first number in the range is where the sequence begins from
#the second is where the sequence will end at
#the third is the increments it will go up by
for i in range(3, 7, 2):
    print(i)


costs = [3, 5, 7, 9, 10, 2]
total = 0


for i in costs:
    total = total + i
    print(total)


#lists
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

#the first number is the row and the next is the column
print(grid[1][2])


for row in grid:
    for col in row:
        print(col)



fruits = ["apple", "mango", "banana", "pear"]

#append adds a variable into the list
#.count will return how many times a certain variable exists within the list
#.index shows when the element first appear in the list
#the .insert lets you specify which position in the index to insert a new variable
fruits.insert(1, "orange")
fruits.append("blueberry")
print(fruits.count("apple"))
print(fruits.index("apple"))

#.pop lets u remove a variable at the specified index
#.remove removes the first instance of a variable
fruits.remove("pear")
fruits.pop(3)

#the reverse function will simply reverse the order of the list
#sort sorts the items in either alphabetical or numerical order
fruits.reverse()
fruits.sort()
print(fruits)


#the .copy allows u to copy a list
fruits2 = fruits.copy()

print(fruits2)


fruit = ["apple", "mango", "banana", "pear"]

#.clear removes everything in the list
fruit.clear()
print(fruit)




#tuples are created with () lists are []
#the values in tuples cannot be changed or modified in anyway
tuples = (1, 2, 5, 3, 2, 1, 9)

#len gives you how many items are within a tuple
print(tuples[0])
print(len(tuples))

