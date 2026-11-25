# Pseudocode — Case Study 2: Progressive Electricity Billing

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT num_months
    SET monthly_records = [], total_units = 0, total_bill = 0
    FOR i = 1 TO num_months DO
        INPUT month_name, units
        WHILE units < 0 DO
            INPUT units
        END WHILE
        Compute energy_charge using progressive slabs (2.0, 3.5, 5.0, 7.0)
        IF units > 300 THEN surcharge = 0.10 * energy_charge ELSE surcharge = 0
        subtotal = energy_charge + 100 + surcharge
        IF units <= 100 THEN rebate = 0.05 * subtotal ELSE rebate = 0
        net_bill = subtotal - rebate
        APPEND (month_name, units, energy_charge, 100, surcharge, rebate, net_bill) TO monthly_records
        total_units = total_units + units
        total_bill = total_bill + net_bill
    END FOR
    avg_units = total_units / num_months
    PRINT monthly billing table
    FOR idx = 0 TO num_months - 1 DO
        Check >= 30% increase over previous month OR >= 1.5 * avg_units
        IF anomaly THEN PRINT alert
    END FOR
END
```
