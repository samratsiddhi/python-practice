def division():
    try:
        a = int(input("enter a number1 : "))
        b = int(input("enter a number2 : "))
        if a==4:
            raise Exception("cannot be 4")
        print(a/b)
    except Exception as e:
        print("something went wrong", e)
        
        