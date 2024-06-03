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

num1 = int(input("What's the first number : "))

for key in operator:
    print(key)

operations = input("Pick an operation : ")

num2 = int(input("What's the second number : "))
calculation = operator[operations]
function_1 = calculation(num1,num2)

print(f"{num1} {operations} {num2} = {function_1} ")

operations_2 = input("Pick another operation : ")

num3 = int(input("What's the number : "))
calculation = operator[operations_2]
function_2 = calculation(function_1, num3)

print(function_2)
