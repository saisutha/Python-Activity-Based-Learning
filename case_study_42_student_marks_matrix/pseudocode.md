# Pseudocode — Case Study 42: Student Marks Matrix Analysis

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT num_students, num_subjects, subject_names
    SET student_names = [], marks_matrix = []
    FOR i = 0 TO num_students - 1 DO
        INPUT st_name, row[0..num_subjects-1]
        APPEND row TO marks_matrix
    END FOR
    SET highest_avg = -1, student_stats = []
    FOR i = 0 TO num_students - 1 DO
        Compute row_sum, row_avg, row_min, row_max, passed_all
        IF row_avg > highest_avg THEN highest_avg = row_avg
        APPEND (student_names[i], row_sum, row_avg, row_min, row_max, passed_all) TO student_stats
    END FOR
    SET subject_stats = [], low_avg_subjects = []
    FOR j = 0 TO num_subjects - 1 DO
        Compute col_avg, col_min, col_max, pass_count across rows
        APPEND (subject_names[j], col_avg, col_min, col_max, pass_count) TO subject_stats
        IF col_avg < 60.0 THEN APPEND (subject_names[j], col_avg) TO low_avg_subjects
    END FOR
    PRINT tables, top_performers (avg == highest_avg), low_avg_subjects
END
```
