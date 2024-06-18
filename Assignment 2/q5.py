def locker_puzzle():

    """
     A school has 100 lockers and 100 students. All lockers are closed on 
    the first day of school. As the students enter, the first student, denoted S1, opens every 
    locker. Then the second student, S2, begins with the second locker, denoted L2, and closes 
    every other locker. Student S3 begins with the third locker and changes every third locker 
    (closes it if it was open, and opens it if it was closed). Student S4 begins with locker L4 and 
    changes every fourth locker. Student S5 starts with L5 and changes every fifth locker, and 
    so on, until student S100 changes L100.

    Note: the first lock is L1 rather than L0.
    """

    # initialize all lockers as closed
    lockers = []
    for i in range(100):
        lockers.append(False)
        
    # initialize open_lockers
    open_lockers = []

    ############## Start your codes ##############
    for student in range(1,101):
        for locker in range(student,101,student):
                if locker in open_lockers:
                    open_lockers.remove(locker)
                else:
                    open_lockers.append(int(locker))
    ##############  End your codes  ##############

    return open_lockers


if __name__ == '__main__':
    open_lockers = locker_puzzle()
    print(open_lockers)

    # For example, if your program believe lock L1, L3, L5, L7 are open, which means open_lockers = [1, 3, 5, 7]. The display of output will be:
    # [1, 3, 5, 7]