# String is a DataType in Python used to repesent text.
# Single or double. Pything will return error as could not find end of the string. 
# String could be 0 characters or really long.
# 
# 
def double_word(word):
    return word*2 + str(len(word*2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0