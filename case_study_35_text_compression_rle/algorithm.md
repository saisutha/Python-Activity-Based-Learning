# Algorithm — Case Study 35: Text Compression Using Character Runs

- **Student Roll Number:** `26000639`

1. **Start** and read `n` sample strings into `samples`.
2. For each `text` in `samples`:
   - Set `orig_len = len(text)`.
   - If `orig_len == 0`, set `encoded = ""`, `enc_len = 0`, `verdict = "EMPTY STRING"`.
   - Else:
     - Initialize `encoded = ""`, `current_char = text[0]`, `run_count = 1`.
     - Loop `i` from `1` to `orig_len - 1`: if `text[i] == current_char`, increment `run_count`; else append `current_char + str(run_count)` to `encoded`, reset `current_char = text[i]` and `run_count = 1`.
     - Append the final run `current_char + str(run_count)` to `encoded`.
     - Compute `enc_len = len(encoded)` and `savings_pct`.
     - Classify as `BENEFICIAL` (`enc_len < orig_len`), `NEUTRAL` (`enc_len == orig_len`), or `NOT BENEFICIAL` (`enc_len > orig_len`).
   - Store `(text, orig_len, encoded, enc_len, round(savings_pct, 2), verdict)` in `results`.
3. Unpack `results` and print the formatted comparison report.
4. **Stop**.
