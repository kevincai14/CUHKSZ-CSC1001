#### Please do not use input() function!!!
class Flower(object):
    def __init__(self, Name, petals, price):
        # Name:flower name
        # petals: number of petals
        # price
        self.Name = Name
        self.petals = petals
        self.price = price

    def Information(self):
        # use return to display the result instead of using print function. You should follow the example format. Do not use input()
        if type(self.Name) != str:
            return 'The input of the flower name is incorrect. A string is required.'
        elif type(self.petals) != int:
            return 'The input of the number of petals is incorrect. An integer is required.'
        elif type(self.price) == str:
            return 'The input of the flower price is incorrect. An integer or float number is required.'
        else:
            info = 'Here is the information of your flower. Name: ' + str(self.Name) + ', Number of petals: ' + str(self.petals) + ', price: ' + str(self.price) + '.'
            return info  # e.g. "Here is the information of your flower. Name: juice, Number of petals: 5, price: 7.82"

    def set_name(self,name):
        if type(self.Name) != str:
            return 'The input of the flower name is incorrect. A string is required.'
        else:
            self.Name = name

    def set_petals(self,petals):
        if type(self.petals) != int:
            return 'The input of the number of petals is incorrect. An integer is required.'
        else:
            self.petals = petals

    def set_price(self,price):
        if type(self.price) == str:
            return 'The input of the flower price is incorrect. An integer or float number is required.'
        else:
            self.price = price

    def get_name(self):
        return self.Name
    def get_petals(self):
        return self.petals
    def get_price(self):
        return self.price