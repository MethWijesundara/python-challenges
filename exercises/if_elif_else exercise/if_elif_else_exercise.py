print('if elif else - Exercise')

mode = input("Enter math operation(+,-,*,/):")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number"))

if mode == '+':
    print(f'Answer is {num1 + num2}')
elif mode == '-':
    print(f'Answer is {num1-num2}')
elif mode == "*":
    print(f"Answer is {num1*num2}")
else:
    print(f"Answer if {num1/num2}")