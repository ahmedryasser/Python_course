x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
sign = input("Enter the sign you will use")
    if sign == "plus" or "+":
        print (x+y)
    
    elif sign == "multiply" or "*" or "x":
        print (x*y)
    
    elif sign == "divide" or "/":
        print (x/y)
    
    elif sign == "subtract" or "subtraction" or "-":
        print (x-y)
    
    else:
        print ("Enter a proper sign")
