class house:
   
    def __init__(self,price=2, window=1, door=1, color="yellow"):
        print("my house")
        self.price = price
        self.window = window
        self.door = door
        self.color = color
    def set_color(self,color):
        self.color = color
    
    def get_color(self):
        return self.color 
    
    def __eq__(self,value):
        return self.window == value.window
    
    def __str__(self):
        print(self.window)
        
    def __gt__(self,other):
        return self.price>other.price
 

ghar1 = house(55,4,5,"blueeee")
ghar2 = house(56,4)

print(ghar1.color)
print(ghar2.color)

print(ghar1.__eq__(ghar2))

ghar1.__str__()

print(ghar1.__gt__(ghar2))

# ghar.set_color("black")

# print(ghar.color)

# print(ghar.get_color())