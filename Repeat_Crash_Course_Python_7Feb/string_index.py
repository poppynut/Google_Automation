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