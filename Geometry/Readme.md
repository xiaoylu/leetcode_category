## Geometry
1. Check if two intervals `[x,y]` and `[a,b]` intersects: `x < b and a < y`
2. The slope of a line: `(x1 - x2) / (y1 - y2)`
3. Overlapping length of two intervals: `overlap = max(min(y,b)-max(x,a), 0)` (return 0 if none)
4. Overlapping area of two rectangles: `overlap = max(min(x2,a2)-max(x1,a1), 0)*max(min(y2,b2)-max(y1,b1), 0)`
5. Projection from a point to a line

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Linalg_projection_4.png/254px-Linalg_projection_4.png)

The parameter c is `(v * s) / (s * s)` where `*` denotes the dot product. 

You can check that `v - [(v * s) / (s * s)]  s ` is orthogonal to `s` because their dot product is ZERO.

[A line defined by `ax+by+c = 0`](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line)

> `|a x0 + b y0 + c |`
> `------------------`
> `sqrt(a * a + b * b)`

6. Angle between two 2D vectors

> `|a - b|^2 = |a|^2 + |b|^2 - 2 |a| |b| cos(theta) `
where `||` denotes the L2 (Euclidean) norm `|(x ,y)| = sqrt(x*x + y*y)`

so we can calculate the `theta` by this equation.

> `cross(a, b) = | a | | b | sin(theta) n`
where `cross()` denotes the cross product, and the unit vector `n` can be found by the right-hand rule.

![Right hand rule](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Right_hand_rule_cross_product.svg/220px-Right_hand_rule_cross_product.svg.png) 


