# Algorithm — Case Study 48: Tuple-Based Employee Shift Conflict Detection

- **Student Roll Number:** `26000639`

1. **Start** and read `n` shift assignments.
2. For each shift `i`:
   - Read `emp_id`, `emp_name`, `day`, `start_hr`, `end_hr`.
   - Validate `0 <= start_hr <= 23` and `start_hr < end_hr <= 24` in a `while` loop.
   - Store `shift_tuple = (emp_id, emp_name, day, start_hr, end_hr)` in `shifts`.
3. Print the formatted registered shift schedule by unpacking each tuple.
4. Use nested loops `i = 0..len(shifts)-1` and `j = i+1..len(shifts)-1`:
   - Unpack `shifts[i]` and `shifts[j]`.
   - If `id1 == id2` and `day1.lower() == day2.lower()` and `s1 < e2 and s2 < e1`:
     - Compute `overlap_start = max(s1, s2)` and `overlap_end = min(e1, e2)`.
     - Construct `conflict_rec` using tuple concatenation `+` and append to `conflicts`; track unique `(id1, name1)` pairs in `conflicted_employees`.
5. Display all conflict pairs with exact overlap windows and unique conflicted employees.
6. **Stop**.
