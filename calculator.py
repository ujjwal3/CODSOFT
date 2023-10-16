# import math
# import re


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("Welcome to the Simple Calculator!")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operations = ["+", "-", "*", "/"]
c = input("Enter the arithmetic operator (+, -, *, or /): ")

while c not in operations:
    print("Please use given operations only!")
    c = input("Enter the arithmetic operator (+, -, *, or /): ")


if c == "+":
    print(f"Result: {add(a, b)}")
elif c == "-":
    print(f"Result: {sub(a, b)}")
elif c == "*":
    print(f"Result: {mul(a, b)}")
elif c == "/":
     if b == 0:
        print("Cannot divide by zero.")
     else:
        print(f"Result: {div(a, b)}")
else:
    print("INVALID INPUT!")
