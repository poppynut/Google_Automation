def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
    if (numerator == 0):
        fraction = 0
    elif (denominator == 0):
        fraction = 0
    else:
        fraction = (numerator / denominator)
        while fraction > 1:
            fraction = fraction - 1
    return fraction

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


#print(5/3)
#print(5%3)
#print(5//3)