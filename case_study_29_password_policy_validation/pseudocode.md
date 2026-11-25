# Pseudocode — Case Study 29: Password Policy Validation Engine

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT n
    INPUT n strings INTO passwords
    SET results = [], passed_count = 0
    FOR EACH pwd IN passwords DO
        SET failures = []
        IF LENGTH(pwd) < 8 THEN APPEND length failure TO failures
        Scan characters for upper, lower, digit, special, space
        APPEND failures for any missing category or space found
        FOR i = 0 TO LENGTH(pwd) - 3 DO
            IF pwd[i] == pwd[i+1] AND pwd[i+1] == pwd[i+2] THEN
                APPEND repetition failure TO failures
                BREAK
            END IF
        END FOR
        Check each banned word IN LOWER(pwd)
        IF LENGTH(failures) == 0 THEN
            passed_count = passed_count + 1
            APPEND (pwd, "PASS", failures) TO results
        ELSE
            APPEND (pwd, "FAIL", failures) TO results
        END IF
    END FOR
    PRINT validation report and summary
END
```
