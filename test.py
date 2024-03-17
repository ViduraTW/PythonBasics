#variable string
first_name = "Jeff"
last_name = "Test"

#combines the two variables with the + sign also creates a space between two words with the " "
full_name = first_name + " " + last_name

#defines class of the variable
print(type(first_name))

print(first_name)
print(full_name)
print("hello " + full_name + "!")

#variable integer
num_of_stuff = 40
print(type(num_of_stuff))
print(num_of_stuff)

#variable float
decimal = 34.13
print(type(decimal))
print(decimal)

#variable boolean
is_it = True
print(type(is_it))
print(is_it)

#converting float to interger
#it removes all the numbers after decimal point
float_number = 23.83
print(int(float_number))

#converting interger into float
int_number = 64
print(float(int_number))

#converting string to interger
#strings with letters cannot be converted into intergers
string_value = "52"
print(type(int(string_value)))
print(int(string_value))


#allows you to display strings and intergers together
number = 64
print("your number is" + str(number))

#indexes
#the string gets indexed beginning with 0 then so on 123456789
message = "Hello World"
print(message[4])

#negative numbers start from the end of the string starting with -1
print(message[-1])

#the len function lets you find how many characters are in the string
print(len(message))


#.find lets you finds the first e or so on in a string
print(message.find("e"))

#you can also use it to find a group of strings the output however will print out the first letter in the group
print(message.find("World"))

#if the string your looking for doesnt exist it will output -1 meaning it doesnt exist in the string
print(message.find("z"))

#the .replace function allows you to replace things within the string
print(message.replace("Hello", "Yo"))

#the .lower function turns the entire string into lowercase letters
print(message.lower())

#the .upper function turns the entire string into uppercase letters
print(message.upper())

#the .capitalize function turns the first letter into a capital and turns the rest into lowercase
message_1 = "pIE"
print(message_1.capitalize())


#adding
print(2.2+5)

#subtracting
print(5-2.7)

#multiplying
print(5*2)

#division out of division will always be a float
print(4/2)

#the % inbetween provides you with the remained you would get from the divison
print(5%2)

#python follows the order of operations
print(3+5*7/2)

#the round function lets you round up or down float numbers
print(round(2.84))

#the comma lets you specify how many decimal places you want the number to be rounded to
print(round(4.2352153, 3))

#the abs function provides you with the absolute value of a number
print(abs(-6))

#the power function provides you with the number to the power of another number
print(pow(2, 4))

#inputs
#the variable gets stored when the user replies to the question
#any input from the user is treated as a string value
name = input("name?")
print("Hi " + name)

age = input("Age?")
print("you are " + age + " years old")
