stock = 5000
buy = 6000
john = 2010
ali= 2000
name = input(" What is your name ")
dept = input(" What is your department ")
if name == "john":
    if dept == "stock":
        sal1 = stock*3
        print (" Your salary is ", sal1)

    elif dept == "buy":
        sal2 = buy*3
        print (" Your salary is ", sal2)

    else:
        print (" Your dapartment is not found ")


elif name == "ali":
    if dept == "stock":
        sal3 = stock*1.5
        print (" Your salary is ", sal3)

    elif dept == "buy":
        sal4 = buy*1.5
        print (" Your salary is ", sal4)

    else:
        print (" Your dapartment is not found ")


else:
    print (" Your name is not registered ")          
