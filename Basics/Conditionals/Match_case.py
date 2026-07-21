# Ask the user to enter a number between 1 and 10 and print a corresponding prize using match case.
a= int(input("enter a number between 1 and 10 :"))

match a :
    case 1:
        print("you won a charger")
    case 3:
        print("you won a chocolate")
    case 5:
        print("you won a camera")
    case _:
        print("better luck next time")


# Ask the user to enter two numbers and an operator (+, -, *, /) and perform the corresponding operation using match case.
n = int(input())
m = int(input())

operation = input("Enter the operator:")

match operation :
    case "+":
        print(n + m)
    case "-":
        print(n - m)
    case "*":
        print(n * m)
    case "/":
        print(n / m)
