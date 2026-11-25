# Case Study 2: Progressive Electricity Billing
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, unpacking

print("=" * 75)
print("PROGRESSIVE ELECTRICITY BILLING & MULTI-MONTH ANOMALY ANALYZER")
print("=" * 75)

num_months = int(input("Enter number of months to process: "))

FIXED_CHARGE = 100.0
monthly_records = []
total_units_all = 0
total_bill_all = 0.0

for i in range(num_months):
    print("\n--- Month", i + 1, "---")
    month_name = input("Enter Month Name (e.g., Jan-2026): ").strip()
    units = int(input("Enter Electricity Units Consumed: "))
    while units < 0:
        print("Units cannot be negative. Please re-enter.")
        units = int(input("Enter Electricity Units Consumed: "))

    # Progressive slab calculation:
    # 0-100: 2.00/unit | 101-200: 3.50/unit | 201-400: 5.00/unit | >400: 7.00/unit
    energy_charge = 0.0
    if units <= 100:
        energy_charge = units * 2.00
    elif units <= 200:
        energy_charge = (100 * 2.00) + ((units - 100) * 3.50)
    elif units <= 400:
        energy_charge = (100 * 2.00) + (100 * 3.50) + ((units - 200) * 5.00)
    else:
        energy_charge = (100 * 2.00) + (100 * 3.50) + (200 * 5.00) + ((units - 400) * 7.00)

    # Surcharge: 10% of energy charge if consumption > 300 units
    surcharge = 0.0
    if units > 300:
        surcharge = energy_charge * 0.10

    subtotal = energy_charge + FIXED_CHARGE + surcharge

    # Rebate: 5% on subtotal for low-consumption households (<= 100 units)
    rebate = 0.0
    if units <= 100:
        rebate = subtotal * 0.05

    net_bill = round(subtotal - rebate, 2)
    monthly_records.append((month_name, units, round(energy_charge, 2), FIXED_CHARGE, round(surcharge, 2), round(rebate, 2), net_bill))
    total_units_all = total_units_all + units
    total_bill_all = total_bill_all + net_bill

avg_units = total_units_all / num_months if num_months > 0 else 0.0
avg_bill = total_bill_all / num_months if num_months > 0 else 0.0

print("\n" + "=" * 75)
print("MONTHLY BILLING SUMMARY")
print("=" * 75)
print(f"{'Month':<12}{'Units':<8}{'Energy':<10}{'Fixed':<8}{'Surchg':<10}{'Rebate':<9}{'Net Bill':<10}")
print("-" * 75)
for rec in monthly_records:
    m_name, u, ec, fc, sc, rb, nb = rec
    print(f"{m_name:<12}{u:<8}{ec:<10.2f}{fc:<8.2f}{sc:<10.2f}{rb:<9.2f}{nb:<10.2f}")

print("-" * 75)
print(f"Total Units: {total_units_all} | Average Units: {avg_units:.2f}")
print(f"Total Billed: INR {total_bill_all:.2f} | Average Bill: INR {avg_bill:.2f}")

# Compare bills across months and identify unusual increases
print("\n" + "=" * 75)
print("CONSUMPTION COMPARISON & UNUSUAL INCREASE ALERTS")
print("=" * 75)
alerts_found = False
for idx in range(len(monthly_records)):
    m_name, u, ec, fc, sc, rb, nb = monthly_records[idx]
    reasons = []
    if idx > 0:
        prev_name, prev_u, _, _, _, _, prev_nb = monthly_records[idx - 1]
        if prev_u > 0:
            pct_change = ((u - prev_u) / prev_u) * 100.0
            if pct_change >= 30.0:
                reasons.append(f"+{pct_change:.1f}% spike vs {prev_name} ({prev_u} -> {u} units)")
        elif u > 0:
            reasons.append(f"Jump from 0 units in {prev_name} to {u} units")
    if avg_units > 0 and u >= 1.5 * avg_units:
        reasons.append(f"Exceeds 1.5x multi-month average ({avg_units:.1f} units)")

    if len(reasons) > 0:
        alerts_found = True
        print(f"[ALERT] {m_name} ({u} units, INR {nb:.2f}): " + "; ".join(reasons))

if not alerts_found:
    print("No unusual consumption increases detected across the recorded months.")
