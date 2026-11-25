# Algorithm — Case Study 29: Password Policy Validation Engine

- **Student Roll Number:** `26000639`

1. **Start** and input `n` sample passwords into list `passwords`.
2. For each `pwd` in `passwords`:
   - Initialize `failures = []` and boolean flags `has_upper`, `has_lower`, `has_digit`, `has_special`, `has_space`.
   - Check `len(pwd) < 8`; if true, append failure reason.
   - Loop through each character `ch` in `pwd` to update the five boolean flags; append reasons for any unmet character requirement or whitespace.
   - Loop `i` from `0` to `len(pwd) - 3` to detect `pwd[i] == pwd[i+1] == pwd[i+2]`; if found, append repetition failure.
   - Check each banned word in `PROHIBITED_SUBSTRINGS` against `pwd.lower()`; if matched, append prohibited substring failure.
   - Store `(pwd, status, failures)` tuple in `results`.
3. Loop through `results`, unpack each tuple, print pass/fail status with all unmet rules, and print the overall pass/fail summary.
4. **Stop**.
