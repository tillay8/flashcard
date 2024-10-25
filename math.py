import os
import random

# Set maximum factor for multiplication/division
max_factor = 12
os.system("clear")

def ask_multiplication():
    a = random.randint(1, max_factor)
    b = random.randint(1, max_factor)
    correct_answer = a * b
    while True:
        user_input = input(f"What is {a} * {b}? ")
        if check_answer(user_input, correct_answer):
            break

def ask_division():
    b = random.randint(1, max_factor)
    correct_answer = random.randint(1, max_factor) * b
    a = correct_answer // b
    while True:
        user_input = input(f"What is {correct_answer} / {b}? ")
        if check_answer(user_input, a):
            break

def check_answer(user_input, correct_answer):
    if user_input.strip() == "":
        print(f"The answer is: {correct_answer}")
        return False
    try:
        if int(user_input) == correct_answer:
            print("\033[92mCorrect!\033[0m")
            os.system("sleep 0.5 && clear")
            return True
        else:
            print(f"\033[31mIncorrect.\033[0m The answer is: {correct_answer}")
            return False
    except ValueError:
        print("\033[31mInvalid input. Please enter a number.\033[0m")
        return False

while True:
    operation = random.randint(0, 1)  # 0 for multiplication, 1 for division
    if operation == 0:
        ask_multiplication()
    else:
        ask_division()
