# Case Study 42: Student Marks Matrix Analysis
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, nested lists, tuples, unpacking

print("=" * 74)
print("STUDENT MARKS MATRIX ANALYSIS SYSTEM")
print("=" * 74)

num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

subject_names = []
for j in range(num_subjects):
    sname = input("Enter name of Subject " + str(j + 1) + ": ").strip()
    subject_names.append(sname)

student_names = []
marks_matrix = []

for i in range(num_students):
    print("\n--- Student", i + 1, "---")
    st_name = input("Enter student name: ").strip()
    student_names.append(st_name)
    row = []
    for j in range(num_subjects):
        score = float(input("  Enter mark in " + subject_names[j] + " (0-100): "))
        row.append(score)
    marks_matrix.append(row)

PASS_MARK = 40.0
LOW_AVG_THRESHOLD = 60.0

# Row-wise statistics (Per Student)
student_stats = []
highest_avg = -1.0

for i in range(num_students):
    row = marks_matrix[i]
    row_sum = 0.0
    row_min = row[0]
    row_max = row[0]
    passed_all = True
    for val in row:
        row_sum = row_sum + val
        if val < row_min:
            row_min = val
        if val > row_max:
            row_max = val
        if val < PASS_MARK:
            passed_all = False
    row_avg = row_sum / num_subjects
    if row_avg > highest_avg:
        highest_avg = row_avg
    student_stats.append((student_names[i], row_sum, row_avg, row_min, row_max, passed_all))

# Column-wise statistics (Per Subject)
subject_stats = []
low_avg_subjects = []

for j in range(num_subjects):
    col_sum = 0.0
    col_min = marks_matrix[0][j]
    col_max = marks_matrix[0][j]
    pass_count = 0
    for i in range(num_students):
        val = marks_matrix[i][j]
        col_sum = col_sum + val
        if val < col_min:
            col_min = val
        if val > col_max:
            col_max = val
        if val >= PASS_MARK:
            pass_count = pass_count + 1
    col_avg = col_sum / num_students
    subject_stats.append((subject_names[j], col_avg, col_min, col_max, pass_count))
    if col_avg < LOW_AVG_THRESHOLD:
        low_avg_subjects.append((subject_names[j], col_avg))

print("\n" + "=" * 74)
print("ROW-WISE STUDENT STATISTICS")
print("=" * 74)
print(f"{'Student':<18}{'Total':<10}{'Average':<10}{'Min':<8}{'Max':<8}{'Status'}")
print("-" * 74)
top_performers = []
for st in student_stats:
    name, total, avg, mn, mx, passed = st
    status = "PASS" if passed else "FAIL"
    print(f"{name:<18}{total:<10.1f}{avg:<10.2f}{mn:<8.1f}{mx:<8.1f}{status}")
    if avg == highest_avg:
        top_performers.append((name, avg, total))

print("\n" + "=" * 74)
print("COLUMN-WISE SUBJECT STATISTICS")
print("=" * 74)
print(f"{'Subject':<18}{'Average':<10}{'Min':<8}{'Max':<8}{'Pass Count'}")
print("-" * 74)
for sb in subject_stats:
    sname, avg, mn, mx, p_cnt = sb
    print(f"{sname:<18}{avg:<10.2f}{mn:<8.1f}{mx:<8.1f}{p_cnt}/{num_students}")

print("\n" + "=" * 74)
print("KEY INSIGHTS")
print("=" * 74)
print("Top Performer(s):")
for name, avg, total in top_performers:
    print(f"  * {name} (Average: {avg:.2f}%, Total: {total:.1f})")

print(f"\nSubjects with Low Average Performance (< {LOW_AVG_THRESHOLD}%):")
if len(low_avg_subjects) == 0:
    print("  None — all subjects meet or exceed the average threshold.")
else:
    for sname, avg in low_avg_subjects:
        print(f"  * {sname}: Average {avg:.2f}%")
