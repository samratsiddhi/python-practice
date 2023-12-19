from abc import ABC, abstractmethod

class person(ABC):
    
    @abstractmethod
    def sprint(self):
        pass
    
    def walk(self):
        self.sprint()
        
class boy(person):
    
    def sprint(self):
        print("he is sprinting")
    
boy = boy()
boy.walk()       