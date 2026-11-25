# Case Study 50: Tuple-Based Route Distance Analysis
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, tuple operations, unpacking

print("=" * 72)
print("TUPLE-BASED ROUTE DISTANCE ANALYSIS")
print("=" * 72)

n = int(input("Enter number of route waypoints (minimum 2): "))
while n < 2:
    print("[ERROR] At least 2 waypoints are required to form a route.")
    n = int(input("Enter number of route waypoints (minimum 2): "))

waypoints = []
for i in range(n):
    print("\n--- Waypoint", i + 1, "---")
    label = input("Enter Location Name: ").strip()
    x = float(input("Enter X coordinate (km): "))
    y = float(input("Enter Y coordinate (km): "))
    waypoints.append((label, x, y))

segments = []
total_distance = 0.0

for i in range(len(waypoints) - 1):
    # Tuple unpacking for successive waypoints
    name1, x1, y1 = waypoints[i]
    name2, x2, y2 = waypoints[i + 1]

    # Euclidean distance formula without external imports
    dx = x2 - x1
    dy = y2 - y1
    dist = ((dx * dx) + (dy * dy)) ** 0.5
    total_distance = total_distance + dist

    # Tuple concatenation to create segment summary tuple
    seg = (i + 1, name1, name2) + ((x1, y1), (x2, y2), round(dist, 2))
    segments.append(seg)

longest_seg = segments[0]
shortest_seg = segments[0]
for seg in segments:
    if seg[5] > longest_seg[5]:
        longest_seg = seg
    if seg[5] < shortest_seg[5]:
        shortest_seg = seg

avg_distance = total_distance / len(segments)

# Direct straight-line displacement between start and end waypoints using tuple slicing/indexing
start_name, sx, sy = waypoints[0]
end_name, ex, ey = waypoints[-1]
direct_displacement = (((ex - sx) ** 2) + ((ey - sy) ** 2)) ** 0.5

print("\n" + "=" * 72)
print("ROUTE SEGMENT BREAKDOWN")
print("=" * 72)
print(f"{'Seg':<5}{'From':<16}{'To':<16}{'Coordinates':<22}{'Distance (km)'}")
print("-" * 72)
for seg in segments:
    idx, f_name, t_name, p1, p2, d = seg
    coord_str = f"({p1[0]:.1f},{p1[1]:.1f})->({p2[0]:.1f},{p2[1]:.1f})"
    print(f"{idx:<5}{f_name:<16}{t_name:<16}{coord_str:<22}{d:>10.2f}")

print("-" * 72)
print(f"Total Route Distance      : {total_distance:.2f} km")
print(f"Average Segment Distance  : {avg_distance:.2f} km")
print(f"Direct Displacement       : {direct_displacement:.2f} km ({start_name} -> {end_name})")
print(f"Longest Route Segment     : Seg {longest_seg[0]} ({longest_seg[1]} -> {longest_seg[2]}) = {longest_seg[5]:.2f} km")
print(f"Shortest Route Segment    : Seg {shortest_seg[0]} ({shortest_seg[1]} -> {shortest_seg[2]}) = {shortest_seg[5]:.2f} km")
