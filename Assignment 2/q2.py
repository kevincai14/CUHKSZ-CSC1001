
def emirps_100():
    '''
    Displays the first 100 emirps. Display 10 numbers per line and align the numbers properly.
    This function does not need a return value. 
    '''
    ########### Start your code ############
    ### hint: When aligh the numbers, monospaced font will be helpful.
    def judge_prime(n):
        judge_counter = 0
        for a in range(1, n + 1):
            if n % a == 0:
                judge_counter = judge_counter + 1
        if judge_counter == 2:
            return True
        else:
            return False

    line_counter = 0
    number_counter = 0
    for a in range(1, 9999):
        judge_prime(a)
        if judge_prime(a) == True:
            reverse_a = int(str(a)[::-1])
            if str(a)[0] != str(reverse_a)[0]:
                judge_prime(reverse_a)
                if judge_prime(reverse_a) == True:
                    if number_counter != 100:
                        if line_counter <= 9:
                            print(str(a).rjust(4), end=" ")
                            line_counter = line_counter + 1
                            number_counter = number_counter + 1
                        else:
                            print("\n")
                            print(str(a).rjust(4), end=" ")
                            number_counter = number_counter + 1
                            line_counter = 1
    ############ End your code #############

if __name__ == '__main__':
    emirps_100()

    # You can just print your solution. Like this:
    #    13   17   31   37   71   73   79   97  107  113
    #   149  157  167  179  199  311  337  347  359  389
    # ...