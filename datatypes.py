Variable="I am Great"
print (type(Variable))

length=10
width=2
area=length*width
print(area)

print(7+9.245)
print("a"+"b"+"c")

print("This " + "is "+ "Pretty ")

base=6
height=3
area=(base*height)/2
print("The area of a triangle is: " + str(area))

def greeting(name):
    print("Welcome, " + name)

greeting("raj")


def greetings(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greetings("Rajkumar", "Devops")


def area_triangle(base, height):
    return base*height/2

area_triangle(2, 4)



def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b

print("The sum of both areas is: " + str(sum))


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)