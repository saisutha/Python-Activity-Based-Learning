# Case Study 48: Tuple-Based Employee Shift Conflict Detection
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, tuple operations, unpacking

print("=" * 74)
print("TUPLE-BASED EMPLOYEE SHIFT CONFLICT DETECTION")
print("=" * 74)

n = int(input("Enter number of shift assignments: "))
shifts = []

for i in range(n):
    print("\n--- Shift Assignment", i + 1, "---")
    emp_id = input("Enter Employee ID: ").strip()
    emp_name = input("Enter Employee Name: ").strip()
    day = input("Enter Day (e.g., Mon, Tue, Wed): ").strip().capitalize()
    start_hr = int(input("Enter Start Hour (0-23): "))
    end_hr = int(input("Enter End Hour (1-24): "))

    while start_hr < 0 or start_hr > 23 or end_hr <= start_hr or end_hr > 24:
        print("[ERROR] Invalid shift hours! Ensure 0 <= start < end <= 24.")
        start_hr = int(input("Enter Start Hour (0-23): "))
        end_hr = int(input("Enter End Hour (1-24): "))

    # Represent shift as a tuple and append to list
    shift_tuple = (emp_id, emp_name, day, start_hr, end_hr)
    shifts.append(shift_tuple)

print("\n" + "=" * 74)
print("REGISTERED SHIFT SCHEDULE")
print("=" * 74)
print(f"{'#':<4}{'Emp ID':<10}{'Name':<16}{'Day':<8}{'Interval':<12}{'Duration'}")
print("-" * 74)
for idx in range(len(shifts)):
    emp_id, emp_name, day, start_hr, end_hr = shifts[idx]
    duration = end_hr - start_hr
    interval = f"{start_hr:02d}:00-{end_hr:02d}:00"
    print(f"{idx + 1:<4}{emp_id:<10}{emp_name:<16}{day:<8}{interval:<12}{duration} hrs")

# Pairwise conflict detection using tuple unpacking
conflicts = []
conflicted_employees = []

for i in range(len(shifts)):
    id1, name1, day1, s1, e1 = shifts[i]
    for j in range(i + 1, len(shifts)):
        id2, name2, day2, s2, e2 = shifts[j]
        if id1 == id2 and day1.lower() == day2.lower():
            # Two intervals [s1, e1) and [s2, e2) overlap iff s1 < e2 and s2 < e1
            if s1 < e2 and s2 < e1:
                overlap_start = s1 if s1 > s2 else s2
                overlap_end = e1 if e1 < e2 else e2
                overlap_hours = overlap_end - overlap_start
                # Tuple concatenation operation to build conflict record
                conflict_rec = (id1, name1, day1) + ((s1, e1), (s2, e2), overlap_start, overlap_end, overlap_hours)
                conflicts.append(conflict_rec)
                emp_pair = (id1, name1)
                if emp_pair not in conflicted_employees:
                    conflicted_employees.append(emp_pair)

print("\n" + "=" * 74)
print("CONFLICT DETECTION RESULTS")
print("=" * 74)
if len(conflicts) == 0:
    print("No overlapping shift conflicts detected.")
else:
    print(f"Total Conflicts Found: {len(conflicts)}")
    for c_idx in range(len(conflicts)):
        cid, cname, cday, iv1, iv2, o_start, o_end, o_hrs = conflicts[c_idx]
        print(
            f"  {c_idx + 1}. {cid} ({cname}) on {cday}: "
            f"[{iv1[0]:02d}:00-{iv1[1]:02d}:00] overlaps [{iv2[0]:02d}:00-{iv2[1]:02d}:00] "
            f"-> Overlap {o_start:02d}:00-{o_end:02d}:00 ({o_hrs} hr)"
        )

    print("\nEmployees with Conflicting Schedules:")
    for eid, ename in conflicted_employees:
        print(f"  - {eid}: {ename}")
