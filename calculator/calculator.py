#Calculator

def add(n1, n2):
    return n1 + n2

def subs(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operator = {
    "+" : add,
    "-" : subs,
    "*" : multi,
    "/" : div
}

satu = 1 

def calc():
    
    num1 = int(input("What's the first number? : "))
    for key in operator:
        print(key)


    while satu > 0:
        operations = input("Pick an operation : ")

        num2 = int(input("What's the second number : "))
        calculation = operator[operations]
    
        answer = calculation(num1,num2)

        print(f"{num1} {operations} {num2} = {answer} ")

        decision = input("Type 'y' if you want to continue or 'n' for new calculation of 'q' for quit")
        if decision == 'y':
            num1 = answer
        elif decision == 'n':
            calc()
        else:
            break

calc()
