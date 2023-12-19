def hash(func):
    def wrapper1():
        print("#" * 15)
        func()
        print("#" * 15)
    return wrapper1


def star(func1):
    def wrapper():
        print("*" * 10)
        func1()
        print("*" * 10)
    return wrapper

def equals(func2):
    def wrapper2():
        print('='*10)
        func2()
        print('='*10)
    return wrapper2

# @star
# @hash
# @equals
def hello():
    print('hello')
    
equals(star(hash(hello)))()