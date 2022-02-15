print("Mountains".upper())

answer='YES'
if answer.lower()=="yes":
    print("User said yes")

# strip removes whitespace and tab and newline characters
print(" yes ".rstrip())
print(" yes ".lstrip())
print("yes ".strip())
print("The number of times e occurs in this string is".count("e"))
print("Forest".endswith("rest"))

print("Fores1t".isnumeric())
print("1234".isnumeric())

print(int("12345") + int("54321"))

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
print("This is another example".split())