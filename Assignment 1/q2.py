integer = str(input("Enter an integer:"))
length = len(integer)
for position in range(1,length + 1):
    number = integer[position - 1]
    print(number)


