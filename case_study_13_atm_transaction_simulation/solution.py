# Case Study 13: ATM Transaction Sequence Simulation
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, unpacking

print("=" * 72)
print("ATM TRANSACTION SEQUENCE SIMULATION")
print("=" * 72)

balance = float(input("Enter Initial Account Balance (INR): "))
single_limit = float(input("Enter Single Withdrawal Limit (INR): "))
daily_limit = float(input("Enter Daily Withdrawal Limit (INR): "))

daily_withdrawn = 0.0
transactions = []
tx_no = 1

print("\nCommands: D = Deposit | W = Withdraw | B = Balance Inquiry | Q = Quit & Summary")

while True:
    choice = input("\nEnter transaction type (D/W/B/Q): ").strip().upper()

    if choice == "Q":
        print("Ending ATM session...")
        break

    elif choice == "B":
        print(f"Current Available Balance: INR {balance:.2f}")
        print(f"Remaining Daily Withdrawal Limit: INR {daily_limit - daily_withdrawn:.2f}")
        transactions.append((tx_no, "BALANCE", 0.0, "SUCCESS", balance, "Balance inquiry"))
        tx_no = tx_no + 1

    elif choice == "D":
        amt = float(input("Enter deposit amount (INR): "))
        if amt <= 0:
            print("[REJECTED] Deposit amount must be greater than zero.")
            transactions.append((tx_no, "DEPOSIT", amt, "REJECTED", balance, "Non-positive amount"))
        elif amt % 100 != 0:
            print("[REJECTED] Deposit amount must be a multiple of INR 100.")
            transactions.append((tx_no, "DEPOSIT", amt, "REJECTED", balance, "Not a multiple of 100"))
        else:
            balance = balance + amt
            print(f"[ACCEPTED] Deposited INR {amt:.2f}. New Balance: INR {balance:.2f}")
            transactions.append((tx_no, "DEPOSIT", amt, "ACCEPTED", balance, "Cash deposited"))
        tx_no = tx_no + 1

    elif choice == "W":
        amt = float(input("Enter withdrawal amount (INR): "))
        if amt <= 0:
            print("[REJECTED] Withdrawal amount must be positive.")
            transactions.append((tx_no, "WITHDRAW", amt, "REJECTED", balance, "Non-positive amount"))
        elif amt % 100 != 0:
            print("[REJECTED] ATM dispenses only multiples of INR 100.")
            transactions.append((tx_no, "WITHDRAW", amt, "REJECTED", balance, "Not a multiple of 100"))
        elif amt > single_limit:
            print(f"[REJECTED] Exceeds single withdrawal limit of INR {single_limit:.2f}.")
            transactions.append((tx_no, "WITHDRAW", amt, "REJECTED", balance, "Exceeds single limit"))
        elif daily_withdrawn + amt > daily_limit:
            print(f"[REJECTED] Exceeds daily withdrawal limit of INR {daily_limit:.2f}.")
            transactions.append((tx_no, "WITHDRAW", amt, "REJECTED", balance, "Exceeds daily limit"))
        elif amt > balance:
            print(f"[REJECTED] Insufficient balance (Available: INR {balance:.2f}).")
            transactions.append((tx_no, "WITHDRAW", amt, "REJECTED", balance, "Insufficient balance"))
        else:
            balance = balance - amt
            daily_withdrawn = daily_withdrawn + amt
            print(f"[ACCEPTED] Withdrawn INR {amt:.2f}. Remaining Balance: INR {balance:.2f}")
            transactions.append((tx_no, "WITHDRAW", amt, "ACCEPTED", balance, "Cash dispensed"))
        tx_no = tx_no + 1

    else:
        print("[INVALID] Unknown command. Use D, W, B, or Q.")
        transactions.append((tx_no, choice, 0.0, "INVALID", balance, "Unknown operation"))
        tx_no = tx_no + 1

# Transaction Summary using tuple unpacking
total_deposited = 0.0
total_withdrawn = 0.0
accepted_count = 0
rejected_count = 0

print("\n" + "=" * 72)
print("ATM TRANSACTION SUMMARY LOG")
print("=" * 72)
print(f"{'#':<4}{'Type':<10}{'Amount':<12}{'Status':<10}{'Balance':<12}{'Remark'}")
print("-" * 72)

for record in transactions:
    num, t_type, amount, status, bal_after, remark = record
    print(f"{num:<4}{t_type:<10}{amount:<12.2f}{status:<10}{bal_after:<12.2f}{remark}")
    if status == "ACCEPTED":
        accepted_count = accepted_count + 1
        if t_type == "DEPOSIT":
            total_deposited = total_deposited + amount
        elif t_type == "WITHDRAW":
            total_withdrawn = total_withdrawn + amount
    elif status == "REJECTED" or status == "INVALID":
        rejected_count = rejected_count + 1

print("-" * 72)
print(f"Total Operations Logged : {len(transactions)}")
print(f"Accepted Monetary Txns  : {accepted_count}")
print(f"Rejected/Invalid Txns   : {rejected_count}")
print(f"Total Deposited         : INR {total_deposited:.2f}")
print(f"Total Withdrawn         : INR {total_withdrawn:.2f}")
print(f"Closing Account Balance : INR {balance:.2f}")
