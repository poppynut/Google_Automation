######################
#Variables, Expressions, Conditional Blocks####


##DataTypes##
#Text between Quotes is a String. String is a Datatype##
#Integer is a Datatype## String, Integer, Float####
print(7+7)
print("7"+"8")
print(7+8)

print(7+8)
######################
a=7+7

print(type('b'))
print(type(a))
print(type(2.5))

#print("1234"+5678)
#######################
#Variables in Python##
#Containers for Data.#
#Expression is a combination of num, symbols and other variables which on evaluation produces a result##
#Can not have a variable with the name print#
#Variable names can not start. Variables are case sensitive##
# 
length=10
width=2
area=length*width
print(area)
print(7+8.5)
#Implicit Cnversion of DataTypes. Intepreter automatically converts one datatype into another.####
print("a"+"b"+"c")
#######################
print("This "+ "is "+"pretty " + "neat!")
#It is possible to combine string and a number##
#Only with explicit conversion##

base=6
height=3
area=(base*height)/2

print("The area of the Triangle is: " + str(area))

#print("1234"+5678)
#######################

total = 2048 + 4537 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))
#######################


#Implicit Conversion == Automatically converts one DataType to another#
#Explicit Conversion == Manually convert one Datatype to another##



#######################
bill = 47.28
tip = bill * (15/100)
total = bill + tip
share = total/2 
print("Each person needs to pay: " + str(share))
#######################
numerator = 10
denominator = 10
result = numerator / denominator
print(int(result))
#######################
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1  + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5 + ' ' + word6 + ' ' + word7)
#######################
#Functions, Defining Functions, 

#print()
#type()
#str()

#Defining own functions

def greeting(name):
    print("Welcome ",name)

greeting("Rajk")
greeting("Cameron")
#######################

def employee(name, department, empid):
    print("Hello " + name + ". " + "You are Welcome to" + department)
    print("Your Employee ID is: ",empid)

employee("Sher","Accounts","123")
#######################
def print_seconds(hours, minutes, seconds):
    print(hours * 60 * 60 + minutes * 60 + seconds)

print_seconds(1,2,3)
#######################
def triangle(base, height):
    area=((base*height)/2)
    return area

area_a=triangle(3,5)
area_b=triangle(5,5)

sum=area_a+area_b

print("The Total area is: ", sum)

#######################

def area_triangle(base, height):
    return base*height/2
area_a=area_triangle(5,4)
area_b=area_triangle(7,3)
sum=area_a+area_b
print("The sum of both areas is: " + str(sum))
#######################
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)
#######################
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds-hours * 3600) // 60
    remaining_seconds = seconds - hours * 360 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
#######################
def greeting(name):
    print("Welcome, " + name)
    return result

result=greeting("Christine")
print(result)
#######################
def lucky_number(name):
    number = len(name)*9
    print("Hello "+ name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Mary")

#######################
def month_days(month, days):
    print(month + " has " + str(days) + " days.")
month_days("june", 30)
month_days("july", 31)


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
#june_days = 30
#print("June has " + str(june_days) + " days.")
#july_days = 31
#print("July has " + str(july_days) + " days.")

#######################
def rectangle_area(base, height):
	area = base * height # the area is base*height
	print("The area is " + str(area))

rectangle_area(5, 6)
#######################
#Question 1
#This function converts miles to kilometers (km).
#
#Complete the function to return the result of the conversion
#
#Call the function to convert the trip distance from miles to kilometers
#
#Fill in the blank to print the result of the conversion
#
#Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))
#######################

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger  = order_numbers(100, 99)
print(smaller, bigger)
#######################
def lucky_number(name):
  number = len(name) * 9
  return number
  return("Hello " + name + ". Your lucky number is " + str(number))
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
#######################
#Logical Operators
#=================

print(10>1)
print("cat" == "dog")
print(1!=1)

#print(1<"1")
print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25>50 or 1!=2)
print(not 42 == "Answer")
#######################

def valid_user(name):
    if len(name)<3:
        print("Invalid Username. Must be at least 3 characters long")

valid_user("Ra")
#######################
def is_positive(number):
  if number>0:
    return True
  else:
    return None

print(is_positive(-2))
#######################
def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at least 3 characters long")
    else:
        print("Valid Username")

#######################
def is_num_positive(number):
  if number>0:
    return True
  else:
    return None

print(is_num_positive(-5))
print(is_num_positive(0))
print(is_num_positive(13))
#######################
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(-3))
print(is_even(2))


print(5//2)
print(6%2)
#######################
def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at least 3 characters long")
    elif len(username)>15:
        print("Invalid Username. Must be at most 15 charcters long")
    else:
        print("Valid Username")

hint_username("Rajkumar")
#######################
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
#######################


print( "big" > "small")
#######################
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
#######################
def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
#######################

print(11 % 5)
print(((10 >= 5*2) and (10 <= 5*2)))
#######################

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
#######################
#######################
#######################
#######################
#######################
#######################
#######################
#######################


print(5/5)
print(5%5)
print(5//4)


def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
    if (numerator == 0):
        fraction = 0
    elif (denominator == 0):
        fraction = 0
    else:
        fraction = numerator % denominator
    return fraction

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0