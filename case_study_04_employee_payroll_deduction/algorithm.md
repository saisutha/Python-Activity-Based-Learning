# Algorithm — Case Study 4: Employee Payroll and Deduction Analysis

- **Student Roll Number:** `26000639`

1. **Start** and input `num_employees`.
2. For each employee `i` from `1` to `num_employees`:
   - Read `emp_id`, `emp_name`, `basic_pay`, `overtime_hrs`, `overtime_rate`, and `rating`.
   - Compute `hra`, `da`, `medical`, `overtime_pay`, and `incentive`, then sum them with `basic_pay` to get `gross_salary`.
   - Compute `pf = basic_pay * 0.12`, `prof_tax`, and slab-wise `income_tax`.
   - Compute `total_deductions` and `net_salary = gross_salary - total_deductions`.
   - Append the 14-field employee tuple to `payroll_records`.
3. Iterate over `payroll_records`, unpack each tuple, accumulate batch totals, and print the formatted side-by-side Earnings/Deductions salary slip.
4. Print batch payroll totals and **Stop**.
