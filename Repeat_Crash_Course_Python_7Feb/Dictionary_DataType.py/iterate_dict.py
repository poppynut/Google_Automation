file_Counts={"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_Counts:
    print(extension)

for ext, amount in file_Counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))


print(file_Counts.keys())
print(file_Counts.values())

for value in file_Counts.values():
    print(value)