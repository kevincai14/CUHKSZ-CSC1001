
def sqrt(n):
    ''' Babylonian Method of Computing the Square Root 
    param n: You need to get the squre root of n.
    return: The square root of n.
    '''
    ########### Start your code ############
    ### hint: the stop condition should be abs(nextGuess - lastGuess) < 0.0001
    lastGuess = 1
    nextGuess = (lastGuess + (n/lastGuess))/2
    while abs(nextGuess - lastGuess) > 0.0001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2
    return nextGuess
    ############ End your code #############



if __name__ == '__main__':
    # Example test cases
    # Note: there will be more test cases in scoring
    ans1 = sqrt(5)
    ans2 = sqrt(37)
    print(ans1,ans2)
    ######## We will judge the correctness by examing the result of sqrt() function. #########