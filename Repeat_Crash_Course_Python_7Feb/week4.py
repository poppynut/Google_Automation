def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    if denominator == 0:
        return 0 #raise Exception('Not possible')
    elif numerator == 0:
        return 0
    # check if result of division is already smaller than 1
    if numerator < denominator:
       return numerator / denominator

    remainder  = numerator % denominator
    return remainder / denominator


print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
print(fractional_part(2, 5))

print(2/5)
print(5%5)