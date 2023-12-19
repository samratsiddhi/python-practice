error_a = 0
while error_a < 1:
    a = input("enter first number :")

    try :
        a = float(a)
        error_a = 1
    except ValueError as e:
        print("Error you must enter a numeric value")


error_b = 0
while error_b < 1:

    b = input("enter second number :")

    try :
        b = float(b)
        error_b = 1
    except ValueError as e:
        print("Error you must enter a numeric value ")

c = input("Error enter operation to perform :")

if(c == '+'):
    result = a + b
elif(c == '-'):
    result = a - b
elif(c == '*'):
    result = a * b
elif(c == '/'):
    if b !=0:
        result = a / b
    else:
        print("cannot divide by zero")
        result = None
elif(c == '**'):
    result = a ** b
elif(c == '%'):
    result = a % b
else:
    result = None
    print("{string}".format(string="enter a valid operator"))

if result != None:
    print('{} {} {} = {}'.format(a,c,b,result))

