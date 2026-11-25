# Pseudocode — Case Study 50: Tuple-Based Route Distance Analysis

- **Student Roll Number:** `26000639`

```text
BEGIN
    INPUT n
    WHILE n < 2 DO
        PRINT error and INPUT n
    END WHILE
    SET waypoints = []
    FOR i = 1 TO n DO
        INPUT label, x, y
        APPEND (label, x, y) TO waypoints
    END FOR
    SET segments = [], total_distance = 0
    FOR i = 0 TO LENGTH(waypoints) - 2 DO
        (name1, x1, y1) = waypoints[i]
        (name2, x2, y2) = waypoints[i + 1]
        dist = ((x2 - x1)^2 + (y2 - y1)^2) ^ 0.5
        total_distance = total_distance + dist
        seg = (i + 1, name1, name2) + ((x1, y1), (x2, y2), ROUND(dist, 2))
        APPEND seg TO segments
    END FOR
    Find longest_seg, shortest_seg, avg_distance, and direct_displacement (waypoints[0] to waypoints[-1])
    PRINT segment table and summary
END
```
