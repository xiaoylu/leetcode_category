## Geometry
1. Check if two intervals `[x,y]` and `[a,b]` intersects: `x < b and a < y`
2. The slope of a line: `(x1 - x2) / (y1 - y2)`
3. Overlapping length of two intervals: `overlap = max(min(y,b)-max(x,a), 0)` (return 0 if none)
4. Overlapping area of two rectangles: `overlap = max(min(x2,a2)-max(x1,a1), 0)*max(min(y2,b2)-max(y1,b1), 0)`
