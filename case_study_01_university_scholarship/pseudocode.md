# Pseudocode — Case Study 1: University Scholarship Allocation

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT n
    SET applicants = []
    FOR i = 1 TO n DO
        INPUT roll, name, num_subj
        SET marks = [], total = 0
        FOR j = 1 TO num_subj DO
            INPUT m
            APPEND m TO marks
            total = total + m
        END FOR
        aggregate = total / num_subj
        INPUT attendance, income
        APPEND (roll, name, marks, aggregate, attendance, income) TO applicants
    END FOR

    SET eligible = [], ineligible = []
    FOR EACH (roll, name, marks, aggregate, attendance, income) IN applicants DO
        SET reasons = []
        Find min_sub across marks
        IF aggregate < 75.0 THEN APPEND "Low aggregate" TO reasons
        IF min_sub < 50.0 THEN APPEND "Subject below 50" TO reasons
        IF attendance < 80.0 THEN APPEND "Low attendance" TO reasons
        IF income > 500000.0 THEN APPEND "Income exceeds limit" TO reasons
        IF LENGTH(reasons) == 0 THEN
            APPEND (roll, name, aggregate, attendance, income, min_sub) TO eligible
        ELSE
            APPEND (roll, name, reasons) TO ineligible
        END IF
    END FOR

    SORT eligible BY (aggregate DESC, attendance DESC, income ASC, min_sub DESC, name ASC)
    PRINT eligible, ineligible
END
```
