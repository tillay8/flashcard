import os
import random

max_value = 12 

os.system("clear")

def generate_problem():
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    if random.choice([True, False]):
        return (num1, num2, num1 * num2, '*')
    else:
        num1 = num1 * num2
        return (num1, num2, num1 // num2, '/')

def repeat(problem):
    uinput = input("\033[94m[ok]\033[0m ")
    os.system("clear")
    while (uinput != str(problem[2])):
        uinput = input(f"What is {problem[0]} {problem[3]} {problem[1]}? ")
        check(problem, uinput)
        os.system("clear")
        problem = generate_problem()

def check(problem, answer):
    if answer == str(problem[2]):
        print("\033[92mCorrect!\033[0m")
        os.system("sleep 0.5&&clear")
    elif answer == "":
        print(f"The answer is {problem[2]}.")
        repeat(problem)
    else:
        print("\033[31mIncorrect.\033[0m Answer is:", problem[2])
        repeat(problem)

while True:
    problem = generate_problem()
    uinput = input(f"What is {problem[0]} {problem[3]} {problem[1]}? ")
    check(problem, uinput)
