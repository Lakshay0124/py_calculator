class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(num1, num2):
        return num1+num2

    def minus(num1, num2):
        return num1-num2

    def multiply(num1, num2):
        return num1*num2

    def divide(num1, num2):
        return num1/num2

    a1 = input("what you want to do +,-,x,/ __   ")

    if(a1 == "/"):
        number = divide(int(input()), int(input()))
        print(f"{number}")
    elif(a1 == "x"):
        number = multiply(int(input()), int(input()))
        print(f"{number}")
    elif(a1 == "-"):
        number = minus(int(input()), int(input()))
        print(f"{number}")
    elif(a1 == "+"):
        number = add(int(input()), int(input()))
        print(f"{number}")
    else:
        print("ERROR")
