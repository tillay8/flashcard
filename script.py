import os, csv, re, time

def normalize_text(text):
    # Normalize by converting to lowercase and removing punctuation
    return re.sub(r'[^\w\s]', '', text).strip().lower()

def ask_and_check(current_line, next_line, attempts):
    while True:
        user_input = input("")
        normalized_input = normalize_text(user_input)
        normalized_next_line = normalize_text(next_line)
        
        if normalized_input == normalized_next_line:
            print("\033[92mCorrect!\033[0m")
            time.sleep(0.5)
            break
        else:
            print(f"\033[31mIncorrect. Try again. Word {attempts} is '{normalized_next_line.split()[attempts - 1]}'\033[0m")
            attempts += 1

# Open and read the CSV file
filename = "script.csv"
while not os.path.exists(filename):
    print(f"\033[31mError: \033[93mFile '{filename}' not found.")
    os.system("printf '\033[94mValid csv file(s): \033[96m' && ls *.csv")
    filename = input("\033[36mName of csv file to import: \033[96m")

lines = []
with open(filename, newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        lines.extend(row)  # Extend to handle CSVs with multiple columns

# Iterate through each line in the script
for i in range(len(lines) - 1):
    current_line = lines[i]
    next_line = lines[i + 1]
    
    # Print the entire script up to the current line
    os.system("clear")
    for j in range(i + 1):
        print(f"\033[94m{lines[j].strip()}\033[0m")
    
    # Ask for the next line with attempts tracking
    ask_and_check(current_line, next_line, attempts=1)

