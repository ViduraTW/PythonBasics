

#ifs and else statements
good_weather = False
bad_weather = False


#the bad weather function will only work if good weather is false
#the else one only works when both values are false
if good_weather:
    print("good weather")
elif bad_weather:
    print("bad weather")
else:
    print("No weather")


is_hungry = True
is_thirsty = True

#both values have to match for it to output with and
if is_hungry and is_thirsty:
    print("eat and drink")

#only one of the values have to match for it output for or
if is_hungry or is_thirsty:
    print("eat or drink")

hungry = False
thirst = True

#this one only works when the not one is false and the other one is true
if thirst and not hungry:
    print("drink but dont eat")



num = 65

#greater than 0 or less than or if it is 0
if num > 0:
    print("number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("the number is 0")


age = 19

#greate than or equal to
if age >= 18:
    print("adult")
else:
    print("minor")


letter = "H"

if letter == "H":
    print("its letter H")

# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to

total = int(input("How many?"))
num_out_of_total = int(input("how many out of the total?"))
fraction = round(num_out_of_total/total, 2)
print("overall " + str(fraction))

if fraction < 0.5:
    print("Less than 50")
else:
    print("over 50")



