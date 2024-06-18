state = False
while state == False:
    try:
        n = int(input("Enter a number:"))
        if n > 0:
            print("m\tm+1\tm**(m+1)")
            for m in range(1, n + 1):
                print(str(m) + "\t" + str(m + 1) + "\t" + str(m ** (m + 1)))
            state = True
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a positive integer.")
