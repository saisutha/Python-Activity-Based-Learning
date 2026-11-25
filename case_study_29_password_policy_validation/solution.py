# Case Study 29: Password Policy Validation Engine
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, unpacking

print("=" * 72)
print("PASSWORD POLICY VALIDATION ENGINE")
print("=" * 72)

MIN_LENGTH = 8
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
PROHIBITED_SUBSTRINGS = ["password", "1234", "admin", "qwerty", "nri", "welcome"]

n = int(input("Enter number of sample passwords to validate: "))
passwords = []
for i in range(n):
    pwd = input("Enter password " + str(i + 1) + ": ")
    passwords.append(pwd)

results = []
passed_count = 0

for pwd in passwords:
    failures = []

    # 1. Minimum length check
    if len(pwd) < MIN_LENGTH:
        failures.append("Length is " + str(len(pwd)) + " (minimum required: " + str(MIN_LENGTH) + ")")

    # 2. Character category checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIAL_CHARS:
            has_special = True
        elif ch == " " or ch == "\t":
            has_space = True

    if not has_upper:
        failures.append("Missing uppercase letter (A-Z)")
    if not has_lower:
        failures.append("Missing lowercase letter (a-z)")
    if not has_digit:
        failures.append("Missing numeric digit (0-9)")
    if not has_special:
        failures.append("Missing special character from " + SPECIAL_CHARS)
    if has_space:
        failures.append("Contains whitespace character")

    # 3. Repetition check (3 or more identical consecutive characters)
    has_triple_repeat = False
    repeat_seq = ""
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] and pwd[i + 1] == pwd[i + 2]:
            has_triple_repeat = True
            repeat_seq = pwd[i:i + 3]
            break
    if has_triple_repeat:
        failures.append("Contains 3+ repeated consecutive characters ('" + repeat_seq + "')")

    # 4. Prohibited substring check (case-insensitive)
    lower_pwd = pwd.lower()
    matched_banned = []
    for sub in PROHIBITED_SUBSTRINGS:
        if sub in lower_pwd:
            matched_banned.append(sub)
    if len(matched_banned) > 0:
        failures.append("Contains prohibited substring(s): " + ", ".join(matched_banned))

    if len(failures) == 0:
        passed_count = passed_count + 1
        strength = "STRONG" if len(pwd) >= 12 else "ACCEPTABLE"
        results.append((pwd, "PASS (" + strength + ")", failures))
    else:
        results.append((pwd, "FAIL", failures))

print("\n" + "=" * 72)
print("VALIDATION REPORT")
print("=" * 72)
for idx in range(len(results)):
    pwd, status, failures = results[idx]
    print(f"\n[{idx + 1}] Password: '{pwd}' -> {status}")
    if len(failures) > 0:
        for reason in failures:
            print("    - Failed:", reason)
    else:
        print("    - All password policy rules satisfied.")

print("\n" + "-" * 72)
print(f"Summary: {passed_count} Passed, {len(results) - passed_count} Failed out of {len(results)} passwords.")
