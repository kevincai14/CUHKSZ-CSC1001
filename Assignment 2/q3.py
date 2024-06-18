
def isValid(number):
    ''' Return True if the card number is valid.
    param number: The card number.
    return: True of False
    '''
    ########### Start your code ############
    a = sumOfDoubleEvenPlace(number)
    b = sumOfOddPlace(number)
    result = a + b
    if result % 10 == 0:
        return True
    else:
        return False
    ############ End your code #############

def sumOfDoubleEvenPlace(number):
    ''' Get the result from step 2.
    param number: The card number.
    return: Sum of double even place.
    '''
    ########### Start your code ############
    number = str(number)
    all_even_Place_number = number[::2]
    length = len(all_even_Place_number)
    even_Place_number = []
    for a in range(length):
        even_Place_number.append(int(all_even_Place_number[a]))
    pre_DoubleEvenPlace = [each_number * 2 for each_number in even_Place_number]
    DoubleEvenPlace = []
    for each_number in pre_DoubleEvenPlace:
        result = getDigit(each_number)
        DoubleEvenPlace.append(result)
    return sum(DoubleEvenPlace)
    ############ End your code #############

def getDigit(number):
    ''' Get digit of the number. For instance: getDigit(5) = 5, getDigit(15) = 6.
    param number: A number who only has one or two digits.
    return: Return this number if it is a single digit, otherwise return the sum of the two digits.
    '''
    ########### Start your code ############
    number = str(number)
    if len(number) == 2:
        return int(number[0]) + int(number[1])
    else:
        return int(number)
    ############ End your code #############

def sumOfOddPlace(number):
    ''' Return the sum of odd place digits in number.
    param number: The card number.
    return: The sum of odd place digits.
    '''
    ########### Start your code ############
    number = str(number)
    all_odd_Place_number = number[1::2]
    length = len(all_odd_Place_number)
    odd_Place_number = []
    for a in range(length):
        odd_Place_number.append(int(all_odd_Place_number[a]))
    return sum(odd_Place_number)
    ############ End your code #############


if __name__ == '__main__':
    # Example test cases
    # Note: there will be more test cases in scoring
    ans1 = isValid(4388576018402626)
    ans2 = isValid(4388576018410707)
    print(ans1, ans2)
    ######## We will judge the correctness by examing the result of isValid() function. #########