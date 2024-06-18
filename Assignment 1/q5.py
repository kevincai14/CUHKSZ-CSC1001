state = False
counter1 = 1
while state == False:
    try:
        n = int(input("Enter a number:"))
        if n > 1:
            print("The prime numbers smaller than " + str(n) + " include:")
            for a in range(1, n):
                counter2 = 0
                for b in range(1, a + 1):
                    if a % b == 0:
                        counter2 = counter2 + 1
                if counter2 == 2:
                    if a < n:
                        if counter1 <= 8:
                            print(a, end=" ")
                            counter1 = counter1 + 1
                        else:
                            print("\n")
                            counter1 = 1
            state = True
        else:
            print("Please enter a positive integer greater than 1.")
    except ValueError:
        print("Please enter a positive integer greater than 1.")