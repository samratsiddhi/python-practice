class burger:
    
    def buns(self):
        print("buns")
        return self
    
    def cheese(self):
        print("cheese")
        return self
    
    def patty(self):
        print("patty")
        return self
    
burger = burger()

burger.buns().patty().cheese()