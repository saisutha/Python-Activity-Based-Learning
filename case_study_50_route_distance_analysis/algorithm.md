# Algorithm — Case Study 50: Tuple-Based Route Distance Analysis

- **Student Roll Number:** `26000639`

1. **Start** and read `n`; re-prompt while `n < 2`.
2. Loop `i` from `1` to `n` to read `label`, `x`, `y` and append `(label, x, y)` to `waypoints`.
3. Initialize `segments = []` and `total_distance = 0.0`.
4. Loop `i` from `0` to `len(waypoints) - 2`:
   - Unpack `waypoints[i]` into `name1, x1, y1` and `waypoints[i + 1]` into `name2, x2, y2`.
   - Compute `dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5` and add to `total_distance`.
   - Build `seg = (i + 1, name1, name2) + ((x1, y1), (x2, y2), round(dist, 2))` and append to `segments`.
5. Scan `segments` to locate `longest_seg` and `shortest_seg`; compute `avg_distance = total_distance / len(segments)`.
6. Unpack `waypoints[0]` and `waypoints[-1]` to calculate `direct_displacement`.
7. Display the segment breakdown table and route summary statistics.
8. **Stop**.
