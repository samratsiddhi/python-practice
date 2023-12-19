# def fun1():
#     global a
#     a=10
#     print(a, "inside")
    

    
# a=20
# print(a)
# fun1()
# print(a)

a=10
def outer():
    global a
    print("outer sees",a)
    a=11
    def inner():
        global a
        print("inner sees",a)

        a=12
    inner()
outer()
print("main sees",a)