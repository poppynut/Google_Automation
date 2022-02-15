#Repetetative Tasks#
#While loops#
#

x=0
while x < 5:
    print("Not there Yet, x=" + str(x))
    x+=1
print("x=" + str(x))

#A while loop will continuously execute code depending on the value of a condition. 
#It begins with the keyword while, followed by a comparison to be evaluated, then a colon. 
#On the next line is the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. 
#What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. 
#Once the statement is no longer true, the loop exits and the next line of code will be executed.  


#While Loop Inside a Function#
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
#############################################

def count_down(start_number):
  current=5
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(5)
#============================================
#x=range(1, 10)
#while x%2 == 0:
#    x = x/2
#print(x)
#=====================================
def print_range(start, end):
	# Loop through the numbers from start to end
	n = 1
	while n <= end:
		print(n)
		n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

#############################################
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
########################################################################################################################

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False