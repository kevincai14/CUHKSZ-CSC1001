def eight_queens():

    """
    The classic Eight Queens puzzle is to place eight queens on a 
    chessboard such that no two queens can attack each other (i.e., no two queens are in the 
    same row, same column, or same diagonal). There are many possible solutions. Write a 
    program that displays one such solution.

    Note: you cannot just pre-define a solution and display it. 
    Please use algorithm to display a possible solution.
    """

    ############## Start your codes ##############

    """穷举 程序可以判断答案是否正确 不断随机生成坐标"""
    state = False
    state2 = True

    #随机坐标生成
    while state == False:
        import random#
        x = [1, 2, 3, 4, 5, 6, 7, 8]
        y = [1, 2, 3, 4, 5, 6, 7, 8]
        result = []
        for i in x:
            a = random.randint(0, len(y) - 1)
            b = y.pop(a)
            result.append([i, b])
            test_result = result[::-1]
        print(result)
        # 一个正确答案测试
        # result = [[1,8],[2,4],[3,1],[4,3],[5,6],[6,2],[7,7],[8,5]]
        # test_result = result[::-1]


    #判断坐标是否正确
        for xy in result[:7]:
            if state2 == True:
                x_1 = xy[0]
                y_1 = xy[1]
                if len(test_result) > 2:
                    test_result.pop()
                    for xy_2 in test_result:
                        x_2 = xy_2[0]
                        y_2 = xy_2[1]
                        if abs(x_1 - x_2) != abs(y_1 - y_2):
                            continue
                        else:
                            state2 = False
                            break
                else:
                    state = True
                    break
            else:
                break
    print(state)
    print(result)




    # def get_next_coordinate(y_possible):
    #     if y_possible != []:
    #         y = y_possible.pop()
    #         return y
    #     else:
    #         return False
    # 
    # 
    # 
    # def judge_coordinate(x_y, result):
    #     x = x_y[0]
    #     y = x_y[1]
    #     state = True
    #     for x_y_result in result:
    #         x_result = x_y_result[0]
    #         y_result = x_y_result[1]
    #         if abs(x - x_result) != abs(y - y_result) and y_result != y:
    #             continue
    #         else:
    #             state = False
    #     return state
    # 
    # 
    # 
    # 
    # def get_right_coordinate(y_possible,result,x):
    #     y = get_next_coordinate(y_possible,result)
    #     if y == False:
    #         result.pop()
    #     else:
    #         x_y = [x, y]
    #         if len(result) == 0:
    #             result.append(x_y)
    #         else:
    #             judge_coordinate(x_y, result)
    #             if judge_coordinate(x_y, result) == True:
    #                 result.append([x, y])
    #                 return result
    #             else:
    #                 get_right_coordinate(y_possible, result,x)
    # 
    # def try_xy(result):
    #     for x in range(len(result) + 1, 9):
    #         y_possible = [1, 2, 3, 4, 5, 6, 7, 8]
    #         if x - len(result) == 3:
    #             print(result)
    #             try_xy(result)
    #         else:
    #             print(result)
    #             get_right_coordinate(y_possible, result,x)
    # 
    # result = []
    # try_xy(result)
    ##############  End your codes  ##############


if __name__ == '__main__':
    eight_queens()

    # This function does not need a return value. 
    # You can just print your solution. For example:
    # |Q| | | | | | | |
    # | | | | |Q| | | |
    # | | | | | | | |Q|
    # | | | | | |Q| | |
    # | | |Q| | | | | |
    # | | | | | | |Q| |
    # | |Q| | | | | | |
    # | | | |Q| | | | |