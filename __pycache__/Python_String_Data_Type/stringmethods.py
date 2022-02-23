print ("Mountains".upper())
print ("Mountains".lower())
########################################
answer="YES"
if answer.lower() == "yes":
    print("The user said Yes")
else:
    print("The user said no.")
########################################
striptease=" Sheryl  "
print(striptease.strip())
print(striptease.lstrip())
print(striptease.rstrip())


print("The number of times e occurs in this string is 4".count("e"))
print("Forest".endswith("resti"))

print("Forest".isnumeric())
print("12345".isnumeric())

print(int("12345") + int("1"))

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase"]))
############################################################