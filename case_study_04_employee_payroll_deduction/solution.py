# Case Study 4: Employee Payroll and Deduction Analysis
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, unpacking

print("=" * 68)
print("EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS SYSTEM")
print("=" * 68)

num_employees = int(input("Enter number of employees: "))
payroll_records = []

for i in range(num_employees):
    print("\n--- Employee", i + 1, "---")
    emp_id = input("Enter Employee ID: ").strip()
    emp_name = input("Enter Employee Name: ").strip()
    basic_pay = float(input("Enter Basic Pay (INR): "))
    overtime_hrs = float(input("Enter Overtime Hours: "))
    overtime_rate = float(input("Enter Overtime Rate per Hour (INR): "))
    rating = int(input("Enter Performance Rating (1 to 5): "))

    # Allowances
    hra = basic_pay * 0.20
    da = basic_pay * 0.15
    medical = 1500.0

    # Overtime & Incentive
    overtime_pay = overtime_hrs * overtime_rate
    if rating == 5:
        incentive = basic_pay * 0.15
    elif rating == 4:
        incentive = basic_pay * 0.10
    elif rating == 3:
        incentive = basic_pay * 0.05
    else:
        incentive = 0.0

    gross_salary = basic_pay + hra + da + medical + overtime_pay + incentive

    # Progressive Deductions
    pf = basic_pay * 0.12
    if gross_salary <= 15000.0:
        prof_tax = 0.0
    elif gross_salary <= 30000.0:
        prof_tax = 150.0
    else:
        prof_tax = 200.0

    # Progressive Income Tax Slabs on Monthly Gross
    if gross_salary <= 25000.0:
        income_tax = 0.0
    elif gross_salary <= 50000.0:
        income_tax = (gross_salary - 25000.0) * 0.05
    elif gross_salary <= 80000.0:
        income_tax = (25000.0 * 0.05) + ((gross_salary - 50000.0) * 0.10)
    else:
        income_tax = (25000.0 * 0.05) + (30000.0 * 0.10) + ((gross_salary - 80000.0) * 0.20)

    total_deductions = pf + prof_tax + income_tax
    net_salary = gross_salary - total_deductions

    payroll_records.append((
        emp_id, emp_name, basic_pay, hra, da, medical,
        overtime_pay, incentive, gross_salary,
        pf, prof_tax, income_tax, total_deductions, net_salary
    ))

# Display formatted salary statement for each employee
total_gross_payout = 0.0
total_net_payout = 0.0
total_tax_collected = 0.0

for rec in payroll_records:
    (emp_id, emp_name, basic_pay, hra, da, medical,
     overtime_pay, incentive, gross_salary,
     pf, prof_tax, income_tax, total_deductions, net_salary) = rec

    total_gross_payout = total_gross_payout + gross_salary
    total_net_payout = total_net_payout + net_salary
    total_tax_collected = total_tax_collected + income_tax

    print("\n" + "=" * 68)
    print(f"SALARY STATEMENT | ID: {emp_id} | Name: {emp_name}")
    print("=" * 68)
    print(f"{'EARNINGS':<32} | {'DEDUCTIONS':<32}")
    print("-" * 68)
    print(f"{'Basic Pay':<20}{basic_pay:>12.2f} | {'Provident Fund':<20}{pf:>12.2f}")
    print(f"{'HRA (20%)':<20}{hra:>12.2f} | {'Professional Tax':<20}{prof_tax:>12.2f}")
    print(f"{'DA (15%)':<20}{da:>12.2f} | {'Income Tax':<20}{income_tax:>12.2f}")
    print(f"{'Medical Allow.':<20}{medical:>12.2f} | {'':<32}")
    print(f"{'Overtime Pay':<20}{overtime_pay:>12.2f} | {'':<32}")
    print(f"{'Incentive':<20}{incentive:>12.2f} | {'':<32}")
    print("-" * 68)
    print(f"{'Gross Salary':<20}{gross_salary:>12.2f} | {'Total Deductions':<20}{total_deductions:>12.2f}")
    print("-" * 68)
    print(f"NET SALARY PAYABLE: INR {net_salary:,.2f}")
    print("=" * 68)

print("\nPAYROLL BATCH TOTALS")
print(f"Employees Processed : {len(payroll_records)}")
print(f"Total Gross Payout  : INR {total_gross_payout:,.2f}")
print(f"Total Income Tax    : INR {total_tax_collected:,.2f}")
print(f"Total Net Payout    : INR {total_net_payout:,.2f}")
