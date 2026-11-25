# Pseudocode — Case Study 48: Tuple-Based Employee Shift Conflict Detection

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT n
    SET shifts = []
    FOR i = 1 TO n DO
        INPUT emp_id, emp_name, day, start_hr, end_hr
        WHILE start_hr < 0 OR start_hr > 23 OR end_hr <= start_hr OR end_hr > 24 DO
            PRINT error and re-input start_hr, end_hr
        END WHILE
        APPEND (emp_id, emp_name, day, start_hr, end_hr) TO shifts
    END FOR
    SET conflicts = [], conflicted_employees = []
    FOR i = 0 TO LENGTH(shifts) - 1 DO
        (id1, name1, day1, s1, e1) = shifts[i]
        FOR j = i + 1 TO LENGTH(shifts) - 1 DO
            (id2, name2, day2, s2, e2) = shifts[j]
            IF id1 == id2 AND LOWER(day1) == LOWER(day2) AND s1 < e2 AND s2 < e1 THEN
                overlap_start = MAX(s1, s2), overlap_end = MIN(e1, e2)
                APPEND (id1, name1, day1) + ((s1, e1), (s2, e2), overlap_start, overlap_end, overlap_end - overlap_start) TO conflicts
                IF (id1, name1) NOT IN conflicted_employees THEN APPEND (id1, name1) TO conflicted_employees
            END IF
        END FOR
    END FOR
    PRINT schedule, conflicts, conflicted_employees
END
```
