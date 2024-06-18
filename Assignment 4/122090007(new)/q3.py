"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""


def HanoiTower(n, from_rod ='A',aux_rod ='B',to_rod ='C'):
    result_list = []
    # Start writing your code.
    a = []
    b = []
    c = []
    for i in range(1, n + 1):
        a.append(i)
    a.reverse()
    if n % 2 == 0:
        b.append(a.pop())
        result_list.append('A' + ' --> ' + 'B')
        main = b
        move1 = a
        move1Name = 'A'
        move2 = c
        move2Name = 'C'
        while len(c) != n:
            move2.append(move1.pop())
            result_list.append(move1Name + ' --> ' + move2Name)
            if main == b:
                c.append(b.pop())
                result_list.append('B' + ' --> ' + 'C')
                main = c
                if a == [] and b == []:
                    break
                elif a == [] and b != []:
                    move1 = b
                    move2 = a
                    move1Name = 'B'
                    move2Name = 'A'
                elif a != [] and b == []:
                    move1 = a
                    move2 = b
                    move1Name = 'A'
                    move2Name = 'B'
                else:
                    if min(a) < min(b):
                        move1 = a
                        move2 = b
                        move1Name = 'A'
                        move2Name = 'B'
                    else:
                        move1 = b
                        move2 = a
                        move1Name = 'B'
                        move2Name = 'A'
            elif main == a:
                b.append(a.pop())
                result_list.append('A' + ' --> ' + 'B')
                main = b
                if a == [] and c == []:
                    break
                elif a == [] and c != []:
                    move1 = c
                    move2 = a
                    move1Name = 'C'
                    move2Name = 'A'
                elif a != [] and c == []:
                    move1 = a
                    move2 = c
                    move1Name = 'A'
                    move2Name = 'C'
                else:
                    if min(a) < min(c):
                        move1 = a
                        move2 = c
                        move1Name = 'A'
                        move2Name = 'C'
                    else:
                        move1 = c
                        move2 = a
                        move1Name = 'C'
                        move2Name = 'A'
            elif main == c:
                a.append(c.pop())
                result_list.append('C' + ' --> ' + 'A')
                main = a
                if b == [] and c == []:
                    break
                elif b == [] and c != []:
                    move1 = c
                    move2 = b
                    move1Name = 'C'
                    move2Name = 'B'
                elif b != [] and c == []:
                    move1 = b
                    move2 = c
                    move1Name = 'B'
                    move2Name = 'C'
                else:
                    if min(b) < min(c):
                        move1 = b
                        move2 = c
                        move1Name = 'B'
                        move2Name = 'C'
                    else:
                        move1 = c
                        move2 = b
                        move1Name = 'C'
                        move2Name = 'B'
    else:
        c.append(a.pop())
        result_list.append('A' + ' --> ' + 'C')
        main = c
        move1 = a
        move1Name = 'A'
        move2 = b
        move2Name = 'B'
        while len(c) != n:
            move2.append(move1.pop())
            result_list.append(move1Name + ' --> ' + move2Name)
            if main == b:
                a.append(b.pop())
                result_list.append('B' + ' --> ' + 'A')
                main = a
                if b == [] and c == []:
                    break
                elif b == [] and c != []:
                    move1 = c
                    move2 = b
                    move1Name = 'C'
                    move2Name = 'B'
                elif b != [] and c == []:
                    move1 = b
                    move2 = c
                    move1Name = 'B'
                    move2Name = 'C'
                else:
                    if min(b) < min(c):
                        move1 = b
                        move2 = c
                        move1Name = 'B'
                        move2Name = 'C'
                    else:
                        move1 = c
                        move2 = b
                        move1Name = 'C'
                        move2Name = 'B'
            elif main == a:
                c.append(a.pop())
                result_list.append('A' + ' --> ' + 'C')
                main = c
                if a == [] and b == []:
                    break
                elif a == [] and b != []:
                    move1 = b
                    move2 = a
                    move1Name = 'B'
                    move2Name = 'A'
                elif a != [] and b == []:
                    move1 = a
                    move2 = b
                    move1Name = 'A'
                    move2Name = 'B'
                else:
                    if min(a) < min(b):
                        move1 = a
                        move2 = b
                        move1Name = 'A'
                        move2Name = 'B'
                    else:
                        move1 = b
                        move2 = a
                        move1Name = 'B'
                        move2Name = 'A'
            elif main == c:
                b.append(c.pop())
                result_list.append('C' + ' --> ' + 'B')
                main = b
                if a == [] and c == []:
                    break
                elif a == [] and c != []:
                    move1 = c
                    move2 = a
                    move1Name = 'C'
                    move2Name = 'A'
                elif a != [] and c == []:
                    move1 = a
                    move2 = c
                    move1Name = 'A'
                    move2Name = 'C'
                else:
                    if min(a) < min(c):
                        move1 = a
                        move2 = c
                        move1Name = 'A'
                        move2Name = 'C'
                    else:
                        move1 = c
                        move2 = a
                        move1Name = 'C'
                        move2Name = 'A'
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
