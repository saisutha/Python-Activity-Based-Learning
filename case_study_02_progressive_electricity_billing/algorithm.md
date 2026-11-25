# Algorithm — Case Study 2: Progressive Electricity Billing

- **Student Roll Number:** `26000639`

1. **Start** and read the number of months `num_months`.
2. Initialize `monthly_records = []`, `total_units_all = 0`, and `total_bill_all = 0.0`.
3. Loop `i` from `1` to `num_months`:
   - Input `month_name` and `units`; re-prompt while `units < 0`.
   - Compute `energy_charge` using progressive `if/elif/else` slabs.
   - Compute `surcharge = energy_charge * 0.10` if `units > 300`, else `0.0`.
   - Compute `subtotal = energy_charge + 100.0 + surcharge`.
   - Compute `rebate = subtotal * 0.05` if `units <= 100`, else `0.0`.
   - Compute `net_bill = round(subtotal - rebate, 2)` and append monthly tuple to `monthly_records`.
4. Compute `avg_units` and `avg_bill` across all months.
5. Unpack each tuple to display the formatted billing summary table.
6. Loop through `monthly_records` to compare consecutive months and against `1.5 * avg_units`, printing `[ALERT]` for anomalies.
7. **Stop**.
