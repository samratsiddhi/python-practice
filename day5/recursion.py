def num(a=1):
    if a>=0:
        num(a-1)
    else:
        return
    print(a)
    
    
num(4)


