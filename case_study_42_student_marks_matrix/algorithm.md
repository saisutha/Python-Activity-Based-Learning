# Algorithm — Case Study 42: Student Marks Matrix Analysis

- **Student Roll Number:** `26000639`

1. **Start** and read `num_students`, `num_subjects`, and `subject_names`.
2. Loop `i` from `0` to `num_students - 1` to input each student's name and a nested list `row` of `num_subjects` marks; append `row` to `marks_matrix`.
3. **Row-wise analysis:** For each student `i`, compute `row_sum`, `row_avg`, `row_min`, `row_max`, and `passed_all`; track `highest_avg`; store student summary tuple in `student_stats`.
4. **Column-wise analysis:** For each subject `j`, loop across rows `0..num_students-1` to compute `col_avg`, `col_min`, `col_max`, and `pass_count`; append subject tuple to `subject_stats` and flag subjects with `col_avg < 60.0` into `low_avg_subjects`.
5. Collect all students whose `avg == highest_avg` into `top_performers`.
6. Print formatted Row-wise table, Column-wise table, Top Performer(s), and Low-Average Subjects.
7. **Stop**.
