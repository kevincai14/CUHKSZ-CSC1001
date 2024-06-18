"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""


def HanoiTower(n, from_rod ='A',aux_rod ='B',to_rod ='C'):
    result_list = []
    # Start writing your code.
    list = []
    while n > 0 or len(list) > 0:
        while n > 0:
            step1 = [True, n - 1,from_rod,to_rod,aux_rod]
            step2 = [False,n,from_rod,to_rod]
            step3 = [False,n - 1,aux_rod,from_rod,to_rod]
            info = []
            info.append(step1)
            info.append(step2)
            info.append(step3)
            list.append(info)
            from_rod,aux_rod,to_rod = from_rod,to_rod,aux_rod
            n = n - 1
        pre_result = list.pop()


        if pre_result[1][0] == False:
            result_list.append(pre_result[1][2] + ' --> ' + pre_result[1][3])
            pre_result[1][0] = True

        if pre_result[2][0] == False:
            n = pre_result[2][1]
            pre_result[2][0] = True

            if n > 0:
                list.append(pre_result)
                from_rod,aux_rod,to_rod = pre_result[2][2:]
    # End writing your code.
    return result_list


"""
You should store each line your output in result_list defined above.
For example, if the outputs of print() are: 
                A --> C
                A --> B
then please store them in result_list:

strs = "A --> C"
result_list.append(strs)
strs = "A --> B"
result_list.append(strs)

Thus, once you want to print something, please store them in result_list immediately, 
rather than utilizing print() to print it. 
Don't miss the space! For example, don't output:
                A-->C
                A-->B

We will utilize the code similar to the following to check your answer.
"""

if __name__ == '__main__':
    n = 3
    result_list = HanoiTower(n)
    for item in result_list:
        print(item)
