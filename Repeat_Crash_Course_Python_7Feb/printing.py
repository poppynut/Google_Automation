from tkinter.messagebox import YES


print("Mountains".upper())

answer = "yes"
if answer.lower() == "yes":
    print("User said yes")

print(" yes ".strip())
print("    yes".lstrip())
print("yes    ".rstrip())
print("13473763".isnumeric())
print("Forest".isnumeric())


print(int("12345") + int("54321"))


print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))