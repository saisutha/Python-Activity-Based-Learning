# Pseudocode — Case Study 35: Text Compression Using Character Runs

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT n
    INPUT n strings INTO samples
    SET results = []
    FOR EACH text IN samples DO
        orig_len = LENGTH(text)
        IF orig_len == 0 THEN
            APPEND ("", 0, "", 0, 0.0, "EMPTY STRING") TO results
        ELSE
            encoded = ""
            current_char = text[0], run_count = 1
            FOR i = 1 TO orig_len - 1 DO
                IF text[i] == current_char THEN
                    run_count = run_count + 1
                ELSE
                    encoded = encoded + current_char + STR(run_count)
                    current_char = text[i]
                    run_count = 1
                END IF
            END FOR
            encoded = encoded + current_char + STR(run_count)
            enc_len = LENGTH(encoded)
            Compute savings_pct and classification
            APPEND (text, orig_len, encoded, enc_len, savings_pct, verdict) TO results
        END IF
    END FOR
    Unpack results and PRINT comparison report
END
```
