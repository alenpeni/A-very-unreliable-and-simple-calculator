" This is a calculator that I wrote because I felt like it"
"ver 1"

def multi():
    num_1 = float(input("Please enter the first number"))
    num_2 = float(input("Please enter the second number"))
    product = num_1 * num_2

    print("The product of " + str(num_1) + " and " + str(num_2) + " is " + str(product))

def addi():
    num_1 = float(input("Please enter the first number"))
    num_2 = float(input("Please enter the second number"))
    asuma = num_1 + num_2

    print("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(asuma))

def sub():
    num_1 = float(input("Please enter the first number"))
    num_2 = float(input("Please enter the second number"))
    diff = num_1 - num_2
    """Note: 2 - 5 != 5 - 2"""

    print("The difference of " + str(num_1) + " and " + str(num_2) + " is " + str(diff))

def divi():
    num_1 = float(input("Please enter the first number"))
    num_2 = float(input("Please enter the second number"))
    quot = num_1 / num_2

    print("The quotient of " + str(num_1) + " and " + str(num_2) + " is " + str(quot))

"main body coming up"

print("Hi there this is a simple calculator I created to test out my current knowledge on python")
name = input("Whats your name? ")
print("Well its nice to meet you " + name )
print("Anyways enough of that, what would you like to do?")
print("\n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide")
option = int(input())

if option == 1:
    addi()
elif option == 2:
    sub()
elif option == 3:
    multi()
else:
    divi()

      
