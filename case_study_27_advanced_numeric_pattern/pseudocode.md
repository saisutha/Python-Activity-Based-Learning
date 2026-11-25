# Pseudocode — Case Study 27: Advanced Numeric Pattern Generator

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT choice
    WHILE choice NOT IN ("1", "2", "3") DO
        PRINT "Invalid option"
        INPUT choice
    END WHILE
    INPUT raw_n
    WHILE NOT ISDIGIT(raw_n) OR INT(raw_n) < 2 OR INT(raw_n) > 9 DO
        PRINT "Invalid dimension"
        INPUT raw_n
    END WHILE
    n = INT(raw_n)
    IF choice == "1" OR choice == "3" THEN
        FOR i = 1 TO n AND n-1 DOWNTO 1 DO
            Print (n - i) * "  " + hollow row with i at ends
        END FOR
    END IF
    IF choice == "2" OR choice == "3" THEN
        FOR i = 1 TO n AND n-1 DOWNTO 1 DO
            Print (n - i) * "  " + "1..i..1"
        END FOR
    END IF
END
```
