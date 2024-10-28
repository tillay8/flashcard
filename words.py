import os, random, csv

way = 0  # 0: English to German, 1: German to English
learning = "German"
known = "English"

os.system("clear")
filename = os.path.splitext(os.path.basename(__file__))[0] + ".csv"
while not os.path.exists(filename):
    print(f"\033[31mError: \033[93mFile '{filename}' not found.")
    os.system("printf '\033[94mValid csv file(s): \033[96m'&& ls *.csv")
    filename = input("\033[36mName of csv file to import: \033[96m")

def repeat(card):
    uinput = input("\033[94m[ok]\033[0m")
    os.system("clear")
    while (uinput.lower() != card[1 ^ way].lower()):  # Convert to lowercase
        prompt = f"\033[0m{learning} of " if way == 0 else f"\033[0m{known} of "
        uinput = input(f"{prompt}{card[way]}: ")
        check(card, uinput)
        os.system("clear")
        card = random.choice(cards)

cards = []
with open(filename, newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cards.append(row)

def check(card, answer):
    if answer.lower() == card[1 ^ way].lower():  # Convert to lowercase
        print("\033[92mCorrect!\033[0m")
        os.system("sleep 0.5&&clear")
    elif answer == "":
        print(f"{card[way]}", f"in {learning if way == 0 else known} is {colorify(card[1 - way])}.")
        repeat(card)
    else:
        print("\033[31mIncorrect.\033[0m Answer is:", colorify(card[1 - way]))
        repeat(card)

def colorify(word):
    article = word[:3]
    color = {"das": "\033[32m", "der": "\033[34m", "die": "\033[31m"}
    return color.get(article, "") + word + "\033[0m"

while True:
    card = random.choice(cards)
    prompt = f"{learning} of " if way == 0 else f"{known} of "
    uinput = input(f"{prompt}{card[way]}: ")
    check(card, uinput)
