# Case Study 27: Advanced Numeric Pattern Generator
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, pattern generation

print("=" * 60)
print("ADVANCED NUMERIC PATTERN GENERATOR")
print("=" * 60)
print("1. Hollow Numeric Diamond")
print("2. Symmetric Palindromic Numeric Diamond")
print("3. Generate Both Patterns")

choice = input("Select pattern option (1/2/3): ").strip()
while choice != "1" and choice != "2" and choice != "3":
    print("[ERROR] Invalid option! Please enter 1, 2, or 3.")
    choice = input("Select pattern option (1/2/3): ").strip()

raw_n = input("Enter diamond half-height n (integer between 2 and 9): ").strip()
while (not raw_n.isdigit()) or int(raw_n) < 2 or int(raw_n) > 9:
    print("[ERROR] Invalid dimension! Enter an integer from 2 to 9.")
    raw_n = input("Enter diamond half-height n (integer between 2 and 9): ").strip()

n = int(raw_n)

if choice == "1" or choice == "3":
    print("\n--- Hollow Numeric Diamond (n =", n, ") ---")
    # Upper half including middle row
    for i in range(1, n + 1):
        line = ""
        # Leading spaces
        for s in range(n - i):
            line = line + "  "
        # Row numbers and inner spaces
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                line = line + str(i) + " "
            else:
                line = line + "  "
        print(line.rstrip())

    # Lower half
    for i in range(n - 1, 0, -1):
        line = ""
        for s in range(n - i):
            line = line + "  "
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                line = line + str(i) + " "
            else:
                line = line + "  "
        print(line.rstrip())

if choice == "2" or choice == "3":
    print("\n--- Symmetric Palindromic Numeric Diamond (n =", n, ") ---")
    # Upper half including middle row
    for i in range(1, n + 1):
        line = ""
        for s in range(n - i):
            line = line + "  "
        for num in range(1, i + 1):
            line = line + str(num) + " "
        for num in range(i - 1, 0, -1):
            line = line + str(num) + " "
        print(line.rstrip())

    # Lower half
    for i in range(n - 1, 0, -1):
        line = ""
        for s in range(n - i):
            line = line + "  "
        for num in range(1, i + 1):
            line = line + str(num) + " "
        for num in range(i - 1, 0, -1):
            line = line + str(num) + " "
        print(line.rstrip())
