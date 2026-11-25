# Algorithm — Case Study 13: ATM Transaction Sequence Simulation

- **Student Roll Number:** `26000639`

1. **Start** and input `balance`, `single_limit`, and `daily_limit`.
2. Initialize `daily_withdrawn = 0.0`, `transactions = []`, and `tx_no = 1`.
3. Repeat in a `while True` loop:
   - Read and normalize `choice`.
   - If `choice == "Q"`, break out of loop.
   - If `choice == "B"`, display current balance and remaining daily limit; append log tuple.
   - If `choice == "D"`, validate `amt > 0` and `amt % 100 == 0`; update `balance` if valid, else reject; append log tuple.
   - If `choice == "W"`, validate `amt > 0`, `amt % 100 == 0`, `amt <= single_limit`, `daily_withdrawn + amt <= daily_limit`, and `amt <= balance`; deduct and update `daily_withdrawn` if valid, else reject; append log tuple.
   - Otherwise, report `[INVALID]` command and append log tuple.
4. Loop over `transactions`, unpack each tuple, print the formatted log table, and compute summary totals.
5. **Stop**.
