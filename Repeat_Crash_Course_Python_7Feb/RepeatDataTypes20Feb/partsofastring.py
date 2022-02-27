#Only Iterate over length of string - 1, because a name string starts from 0.
#  Negative Indexing

#name="Jaylen"
#print(name[5])#
#
#print([name[-1]])

#def first_and_last(message):
#    if  message[0] == message[-1]:
#        return True
#    else:
#        return False
#
#print(first_and_last("else"))
#print(first_and_last("tree"))
#print(first_and_last(""))


def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))