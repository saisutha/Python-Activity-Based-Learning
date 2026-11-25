# Pseudocode — Case Study 4: Employee Payroll and Deduction Analysis

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT num_employees
    SET payroll_records = []
    FOR i = 1 TO num_employees DO
        INPUT emp_id, emp_name, basic_pay, ot_hrs, ot_rate, rating
        hra = 0.20 * basic_pay
        da = 0.15 * basic_pay
        medical = 1500
        ot_pay = ot_hrs * ot_rate
        Determine incentive from rating (5->15%, 4->10%, 3->5%, else 0%)
        gross = basic_pay + hra + da + medical + ot_pay + incentive
        pf = 0.12 * basic_pay
        Determine prof_tax and progressive income_tax from gross
        deductions = pf + prof_tax + income_tax
        net = gross - deductions
        APPEND (emp_id, emp_name, ..., net) TO payroll_records
    END FOR
    FOR EACH record IN payroll_records DO
        Unpack record and PRINT formatted salary slip
        Accumulate batch gross, tax, and net totals
    END FOR
    PRINT batch totals
END
```
