# Algorithm — Case Study 27: Advanced Numeric Pattern Generator

- **Student Roll Number:** `26000639`

1. **Start** and display the pattern menu (`1`: Hollow Diamond, `2`: Palindromic Diamond, `3`: Both).
2. Read `choice`; loop while `choice` is not `"1"`, `"2"`, or `"3"`.
3. Read `raw_n`; loop while `raw_n` is not digits or `int(raw_n) < 2` or `int(raw_n) > 9`, then set `n = int(raw_n)`.
4. If `choice` is `"1"` or `"3"`:
   - Loop `i` from `1` to `n` (upper half) and `n - 1` down to `1` (lower half):
     - Append `n - i` double spaces, then print `i` only at boundary positions (`j == 1` or `j == 2*i - 1`) and spaces inside.
5. If `choice` is `"2"` or `"3"`:
   - Loop `i` from `1` to `n` and `n - 1` down to `1`:
     - Append `n - i` double spaces, ascending digits `1..i`, and descending digits `i-1..1`.
6. **Stop**.
