def isAnagram(s1, s2):
    
    """
    Write a function that checks whether two words are anagrams. 
    Two words are anagrams if they contain the same letters.
    You can write a program to change the 'result' to Ture or False 
    For example, silent and listen are anagrams, and the result = True.
    """
    
    # initialize result
    result = True

    ############## Start your codes ##############
    def apart_word(word):
        length = len(word)
        letter = []
        for i in range(length):
            letter.append(word[i])
        letter.sort()
        return letter
    if apart_word(s1) == apart_word(s2):
        result = True
    else:
        result = False

    ##############  End your codes  ##############

    return result
        

if __name__ == '__main__':

    # Example test cases
    # Note: there will be more test cases in scoring
    s1 = ["listen", "car", "anagram", "a", "ttttttta"]
    s2 = ["slient", "rat", "nagaram", "an", "tatttttt"]

    for i in range(5):
        print(isAnagram(s1[i], s2[i]))

    # The display of output will be:
    # True
    # False
    # True
    # False
    # True