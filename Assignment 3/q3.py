#### Please do not use input() function!!!
class ecosystem(object):

    def __init__(self, river_len, num_fish, num_bear, steps):
        #######initialization#######
        self.river_len = river_len
        self.num_fish = num_fish
        self.num_bear = num_bear
        self.steps = steps

    def simulation(self):
        # You should follow the example format. Use print() tp display the result as given in AS3 read me.pdf. Do not use input()
        import random
        '''初始化河流'''
        state = False
        while state == False:
            river_1 = []
            for i in range(self.river_len):
                river_1.append('N')
            fish_location = []
            for i in range(self.num_fish):
                random_location = random.randint(0, self.river_len - 1)
                if random_location in fish_location:
                    state = False
                    break
                else:
                    fish_location.append(random_location)
                    river_1[random_location] = 'F'
                    state = True
        state = False
        while state == False:
            river_2 = river_1[:]
            used_location = fish_location[:]
            bear_location = []
            for i in range(self.num_bear):
                random_location = random.randint(0, self.river_len - 1)
                if random_location in used_location:
                    state = False
                    break
                else:
                    used_location.append(random_location)
                    bear_location.append(random_location)
                    river_2[random_location] = 'B'
                    state = True
        river_3 = river_2[:]

        used_location.sort()

        def step(river,judge_river,used_location):
            print(river)
            len_used = len(used_location)
            for location in used_location:
                if river[location] != judge_river[location]:
                    continue
                else:
                    print('Animal:' + river[location] + ', ',end='')
                    if location == 0:
                        movement = random.randint(0, 1)
                    elif location == len(river) - 1:
                        movement = random.randint(-1, 0)
                    else:
                        movement = random.randint(-1, 1)
                    print('Action:' + str(movement))
                    if river[location] == 'B':
                        if movement == 1:
                            try:
                                if river[location + 1] == 'F':
                                    river[location] = 'N'
                                    river[location + 1] = 'B'
                                    len_used -= 1
                                    print('The current ecosystem after the action:')
                                    print(river)
                                elif river[location + 1] == 'N':
                                    river[location] = 'N'
                                    river[location + 1] = 'B'
                                    print('The current ecosystem after the action:')
                                    print(river)
                                elif river[location + 1] == 'B':
                                    if len_used != len(river):
                                        location_counter = -1
                                        n_location = []
                                        for i in river:
                                            location_counter += 1
                                            if i == 'N':
                                                n_location.append(location_counter)
                                            else:
                                                continue
                                        random_n_location = random.randint(0, len(n_location) - 1)
                                        river[n_location[random_n_location]] = 'B'
                                        print('The current ecosystem after the action:')
                                        print(river)
                                    if len_used == len(river):
                                        print('The current ecosystem after the action:')
                                        print(river)
                            except:
                                print('The current ecosystem after the action:')
                                print(river)
                                continue

                        elif movement == -1:
                            if location != 0:
                                try:
                                    if river[location - 1] == 'F':
                                        river[location] = 'N'
                                        river[location - 1] = 'B'
                                        len_used -= 1
                                        print('The current ecosystem after the action:')
                                        print(river)
                                    elif river[location - 1] == 'N':
                                        river[location] = 'N'
                                        river[location - 1] = 'B'
                                        print('The current ecosystem after the action:')
                                        print(river)
                                    elif river[location - 1] == 'B':
                                        if len_used != len(river):
                                            location_counter = -1
                                            n_location = []
                                            for i in river:
                                                location_counter += 1
                                                if i == 'N':
                                                    n_location.append(location_counter)
                                                else:
                                                    continue
                                            random_n_location = random.randint(0, len(n_location) - 1)
                                            river[n_location[random_n_location]] = 'B'
                                            print('The current ecosystem after the action:')
                                            print(river)
                                        if len_used == len(river):
                                            print('The current ecosystem after the action:')
                                            print(river)
                                            continue
                                except:
                                    print('The current ecosystem after the action:')
                                    print(river)
                                    continue
                            else:
                                print('The current ecosystem after the action:')
                                print(river)
                        else:
                            print('The current ecosystem after the action:')
                            print(river)
                            continue

                    if river[location] == 'F':
                        if movement == 1:
                            try:
                                if river[location + 1] == 'B':
                                    river[location] = 'N'
                                    print('The current ecosystem after the action:')
                                    print(river)
                                elif river[location + 1] == 'N':
                                    river[location] = 'N'
                                    river[location + 1] = 'F'
                                    print('The current ecosystem after the action:')
                                    print(river)
                                elif river[location + 1] == 'F':
                                    if len(used_location) != len(river):
                                        location_counter = -1
                                        n_location = []
                                        for i in river:
                                            location_counter += 1
                                            if i == 'N':
                                                n_location.append(location_counter)
                                            else:
                                                continue
                                        random_n_location = random.randint(0, len(n_location) - 1)
                                        river[n_location[random_n_location]] = 'F'
                                        print('The current ecosystem after the action:')
                                        print(river)
                                    if len(used_location) == len(river):
                                        print('The current ecosystem after the action:')
                                        print(river)
                                        continue
                            except:
                                print('The current ecosystem after the action:')
                                print(river)
                                continue
                        elif movement == -1:
                            if location != 0:
                                try:
                                    if river[location - 1] == 'B':
                                        river[location] = 'N'
                                        print('The current ecosystem after the action:')
                                        print(river)
                                    elif river[location - 1] == 'N':
                                        river[location] = 'N'
                                        river[location - 1] = 'F'
                                        print('The current ecosystem after the action:')
                                        print(river)
                                    elif river[location - 1] == 'F':
                                        if len(used_location) != len(river):
                                            location_counter = -1
                                            n_location = []
                                            for i in river:
                                                location_counter += 1
                                                if i == 'N':
                                                    n_location.append(location_counter)
                                                else:
                                                    continue
                                            random_n_location = random.randint(0, len(n_location) - 1)
                                            river[n_location[random_n_location]] = 'F'
                                            print('The current ecosystem after the action:')
                                            print(river)
                                        if len(used_location) == len(river):
                                            print('The current ecosystem after the action:')
                                            print(river)
                                            continue
                                except:
                                    print('The current ecosystem after the action:')
                                    print(river)
                                    continue
                            else:
                                print('The current ecosystem after the action:')
                                print(river)
                        else:
                            print('The current ecosystem after the action:')
                            print(river)
                            continue
            used_location = []
            counter = -1
            for i in river:
                counter += 1
                if i != 'N':
                    used_location.append(counter)
            return [river,used_location]

        print('The ecosystem at the beginning of the step 1:')
        a = step(river_3,river_2,used_location)
        for i in range(self.steps-1):
            print('The ecosystem at the beginning of the step ' + str(i + 2) + ':')
            c = a[1]
            a = step(a[0],a[0],c)