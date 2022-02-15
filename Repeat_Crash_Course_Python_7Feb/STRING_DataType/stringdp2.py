from hashlib import new


def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:  # skipped if first condition was met
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

color="Orange"
print(color[1:4])
fruit="pineapple"
print(fruit[0:2])
print(fruit[4:])
print(fruit[:4])

message="A Kong String with a silly typo"
print(message[0:4])
new_message=message[0:2] + "L" + message[3:]
print(new_message)
message=new_message
print(message)

pets="Cats & Dogs"
print(pets.index("&"))

print("ogs" in pets)

if "sog" in pets:
    print("ogs is Available in pets")
elif "& " in pets:
    print("& " + "is Available in pets")
