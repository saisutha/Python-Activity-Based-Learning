# Case Study 1: University Scholarship Allocation
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, nested lists, tuples, unpacking

print("=" * 70)
print("UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM")
print("=" * 70)

n = int(input("Enter number of applicants: "))

applicants = []
for i in range(n):
    print("\n--- Applicant", i + 1, "---")
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    num_subj = int(input("Enter number of subjects: "))
    marks = []
    total_marks = 0.0
    for j in range(num_subj):
        m = float(input("  Enter mark for subject " + str(j + 1) + " (out of 100): "))
        marks.append(m)
        total_marks = total_marks + m
    aggregate = total_marks / num_subj if num_subj > 0 else 0.0
    attendance = float(input("Enter Attendance Percentage: "))
    income = float(input("Enter Annual Family Income (INR): "))
    applicants.append((roll, name, marks, aggregate, attendance, income))

# Eligibility Thresholds
MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARK = 50.0
MIN_ATTENDANCE = 80.0
MAX_INCOME = 500000.0

eligible = []
ineligible = []

for record in applicants:
    roll, name, marks, aggregate, attendance, income = record
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate " + str(round(aggregate, 2)) + "% < " + str(MIN_AGGREGATE) + "%")

    min_sub = marks[0] if len(marks) > 0 else 0.0
    failed_sub = False
    for m in marks:
        if m < min_sub:
            min_sub = m
        if m < MIN_SUBJECT_MARK:
            failed_sub = True
    if failed_sub:
        reasons.append("Subject mark below " + str(MIN_SUBJECT_MARK) + " (min=" + str(min_sub) + ")")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance " + str(round(attendance, 2)) + "% < " + str(MIN_ATTENDANCE) + "%")

    if income > MAX_INCOME:
        reasons.append("Family income " + str(round(income, 2)) + " > " + str(MAX_INCOME))

    if len(reasons) == 0:
        eligible.append((roll, name, round(aggregate, 2), round(attendance, 2), income, min_sub))
    else:
        ineligible.append((roll, name, reasons))

# Sort eligible applicants using predefined tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance percentage
# 3. Lower family income
# 4. Higher minimum subject score
# 5. Alphabetical order of name
count = len(eligible)
for i in range(count):
    for j in range(0, count - i - 1):
        r1, n1, a1, att1, inc1, ms1 = eligible[j]
        r2, n2, a2, att2, inc2, ms2 = eligible[j + 1]
        swap = False
        if a1 < a2:
            swap = True
        elif a1 == a2:
            if att1 < att2:
                swap = True
            elif att1 == att2:
                if inc1 > inc2:
                    swap = True
                elif inc1 == inc2:
                    if ms1 < ms2:
                        swap = True
                    elif ms1 == ms2 and n1.lower() > n2.lower():
                        swap = True
        if swap:
            temp = eligible[j]
            eligible[j] = eligible[j + 1]
            eligible[j + 1] = temp

print("\n" + "=" * 70)
print("RANKED ELIGIBLE SCHOLARSHIP CANDIDATES")
print("=" * 70)
if len(eligible) == 0:
    print("No applicants met all scholarship eligibility criteria.")
else:
    print(f"{'Rank':<6}{'Roll No':<12}{'Name':<18}{'Agg %':<9}{'Att %':<9}{'MinSub':<9}{'Income':<12}")
    print("-" * 70)
    rank = 1
    for candidate in eligible:
        roll, name, agg, att, inc, min_sub = candidate
        print(f"{rank:<6}{roll:<12}{name:<18}{agg:<9.2f}{att:<9.2f}{min_sub:<9.1f}{inc:<12.2f}")
        rank = rank + 1

print("\n" + "=" * 70)
print("INELIGIBLE APPLICANTS & REASONS")
print("=" * 70)
if len(ineligible) == 0:
    print("All applicants are eligible.")
else:
    for item in ineligible:
        roll, name, reasons = item
        print(f"- {roll} ({name}): " + "; ".join(reasons))
