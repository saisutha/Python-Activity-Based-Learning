# Pseudocode — Case Study 13: ATM Transaction Sequence Simulation

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT balance, single_limit, daily_limit
    SET daily_withdrawn = 0, transactions = [], tx_no = 1
    WHILE TRUE DO
        INPUT choice (uppercase)
        IF choice == "Q" THEN BREAK
        ELSE IF choice == "B" THEN
            PRINT balance, daily_limit - daily_withdrawn
            APPEND (tx_no, "BALANCE", 0, "SUCCESS", balance, "Balance inquiry") TO transactions
        ELSE IF choice == "D" THEN
            INPUT amt
            IF amt > 0 AND amt MOD 100 == 0 THEN
                balance = balance + amt
                APPEND (tx_no, "DEPOSIT", amt, "ACCEPTED", balance, "Cash deposited") TO transactions
            ELSE
                APPEND (tx_no, "DEPOSIT", amt, "REJECTED", balance, reason) TO transactions
            END IF
        ELSE IF choice == "W" THEN
            INPUT amt
            Validate > 0, multiple of 100, <= single_limit, daily_withdrawn + amt <= daily_limit, <= balance
            Update balance and daily_withdrawn if valid; log ACCEPTED or REJECTED
        ELSE
            APPEND (tx_no, choice, 0, "INVALID", balance, "Unknown operation") TO transactions
        END IF
        tx_no = tx_no + 1
    END WHILE
    Unpack transactions and PRINT summary table and totals
END
```
