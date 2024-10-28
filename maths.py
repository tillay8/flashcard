import os, random, time

max_factor = 12

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def ask_multiplication():
    a = random.randint(1, max_factor)
    b = random.randint(1, max_factor)
    correct_answer = a * b
    while True:
        clear_console()
        user_input = input(f"What is {a} * {b}? ")
        if check_answer(user_input, correct_answer, a, b, " * "):
            break

def ask_division():
    b = random.randint(1, max_factor)
    a = random.randint(1, max_factor) * b
    correct_answer = a // b
    while True:
        clear_console()
        user_input = input(f"What is {a} / {b}? ")
        if check_answer(user_input, correct_answer, a, b, " / "):
            break

def check_answer(user_input, correct_answer, a, b, operation):
    if user_input.strip() == "":
        clear_console()
        print(f"{a}{operation}{b} = {correct_answer}")
        input("[ok]")
        return False
    try:
        if int(user_input) == correct_answer:
            print("\033[92mCorrect!\033[0m")
            time.sleep(0.5)
            clear_console()
            return True
        else:
            print(f"\033[31mIncorrect.\033[0m The answer is: {correct_answer}")
            input("[ok]")
            return False
    except ValueError:
        print("\033[31mInvalid input. Please enter a number.\033[0m")
        input("[ok]")
        return False

while True:
    operation = random.choice(['multiplication', 'division'])
    if operation == 'multiplication':
        ask_multiplication()
    else:
        ask_division()
