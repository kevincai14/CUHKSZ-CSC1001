final = float(input("Enter the final account value:"))
rate = float(input("Enter the annual interest rate:"))
year = float(input("Enter the number of years:"))
value = final / (1 + 0.01 * rate) ** year
print("The initial value is: " + str(value))