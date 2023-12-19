class Person:
    def __init__(self,name,age,password):
        self.name = name
        self._age = age
        self.__password = password
        
    # def get_password(self):
    #     return self.__password
    
    # def set_password(self,password):
    #     self.__password = password
    
    # password = property(get_password,set_password)
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password = password
    
person = Person("Ram", 44, "acsas")
print(person.name)
print(person._age)
# print(person.get_password())

person.password = "new password"
print(person.password)
