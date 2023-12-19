class granpa():
    def __init__(self):
        print("grandfather")
    
    def get_house(self):
        return self.house
    
    house = "mansion"

class grandma():
    jwellery = "diamond"
    
class father(granpa,grandma):
    car = "bugatti"
    
    def get_house(self):
        super().get_house()
        return "jhan ramro ghar"
    
class son(father):
    def __init__(self):
        print("father")
    console = "ps5"
    
father =  father()

# print(father.get_house())
# print(father.jwellery)
# print(father.house)

# son =  son()
# print(son.jwellery)
# print(son.house)
# print(son.car)