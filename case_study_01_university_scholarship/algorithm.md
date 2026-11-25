# Algorithm — Case Study 1: University Scholarship Allocation

- **Student Roll Number:** `26000639`

1. **Start** and read the number of applicants `n`.
2. For each applicant `i` from `1` to `n`:
   - Read `roll`, `name`, `num_subj`, individual subject marks into list `marks`, `attendance`, and `income`.
   - Calculate `aggregate = total_marks / num_subj`.
   - Store `(roll, name, marks, aggregate, attendance, income)` in `applicants`.
3. Initialize empty lists `eligible` and `ineligible`.
4. For each tuple in `applicants`:
   - Unpack `(roll, name, marks, aggregate, attendance, income)` and initialize `reasons = []`.
   - Check `aggregate < 75.0`, any mark `< 50.0`, `attendance < 80.0`, and `income > 500000.0`; append any violated conditions to `reasons`.
   - If `reasons` is empty, append `(roll, name, round(aggregate, 2), round(attendance, 2), income, min_sub)` to `eligible`; otherwise append `(roll, name, reasons)` to `ineligible`.
5. Sort `eligible` using nested loops (bubble sort) comparing the 5 tie-breaking fields via tuple unpacking.
6. Print the ranked table of eligible scholarship candidates and the detailed list of ineligible applicants with reasons.
7. **Stop**.
