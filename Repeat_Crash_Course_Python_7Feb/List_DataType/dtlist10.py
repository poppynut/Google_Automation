animals=["lion", "zebra", "dolphimn", "monkey"]
chars=0

for animal in animals:
    chars += len(animal)

print("Total Characters: {}, Average Length: {}".format(chars, chars/len(animals)))
