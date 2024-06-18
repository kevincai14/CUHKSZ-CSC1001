#### Please do not use input() function!!!
class process_derivative(object):

    def __init__(self, polynominal):
        self.polynominal = polynominal

    def get_first_derivative(self):
        # You should follow the example format. Do not use input()
        def apart_polynominal(polynominal, result):
            location = polynominal.find('-', 1)
            if location == -1:
                if polynominal[0] == str(0):
                    return False
                else:
                    result.append(polynominal)
            else:
                result.append(polynominal[0:location])
                sub = polynominal[location:]
                apart_polynominal(sub, result)
            return result

        def get_each_derivative(monomial):
            try:
                monomial = float(monomial)
                return str(0)
            except:
                try:
                    list = monomial.split('*')
                    if '^' in list[1]:
                        list2 = list[1].split('^')
                        if list2[1] == '2':
                            result = str(int(list2[1]) * int(list[0])) + '*' + str(list[1][0])
                            return result
                        elif list2[1] == '1':
                            result = str(list[0])
                            return result
                        elif list2[1] == '0':
                            return str(0)
                        else:
                            result = str(int(list2[1]) * int(list[0])) + '*' + str(list[1][0]) + '^' + str(
                                int(list2[1]) - 1)
                            return result
                    else:
                        return list[0]
                except:
                    if len(monomial) == 1:
                        return str(1)
                    else:
                        list = monomial.split('^')
                        if list[1] == '0':
                            return str(0)
                        elif list[1] == '2':
                            return str(list[1]) + '*' +str(list[0])
                        elif list[1] == '1':
                            return str(list[0])
                        else:
                            return str(list[1]) + '*' + str(list[0]) + '^' + str(int(list[1]) - 1)

        split1 = self.polynominal.split('+')
        monomial = []
        for each_split1 in split1:
            pre_split = apart_polynominal(each_split1, monomial)
        final_result = []
        for each_split2 in pre_split:
            each_derivative = get_each_derivative(each_split2)
            if each_derivative == '0':
                continue
            else:
                if each_derivative[0] != '-':
                    each_derivative = '+' + each_derivative
                final_result.append(each_derivative)
        try:
            result_two = ''
            for each_split2 in final_result:
                result_two = result_two + each_split2
            if result_two[0] == '+':
                result_two = result_two[1:]
        except:
            result_two = str(0)

        # result_two = 'your calculator result'
        return "The first derivative is:" + result_two  # e.g. "The first derivative is: '6*x^2+6*x+5'"
