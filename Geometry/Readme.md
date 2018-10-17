## Geometry
1. Check if two intervals `[x,y]` and `[a,b]` intersects: `x < b and a < y`
2. The slope of a line: `(x1 - x2) / (y1 - y2)`
3. Overlapping length of two intervals: `overlap = max(min(y,b)-max(x,a), 0)` (return 0 if none)
4. Overlapping area of two rectangles: `overlap = max(min(x2,a2)-max(x1,a1), 0)*max(min(y2,b2)-max(y1,b1), 0)`
5. Projection from a point to a line

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Linalg_projection_4.png/254px-Linalg_projection_4.png)

The parameter c is `(v * s) / (s * s)` where `*` denotes the dot product. 

You can check that `v - [(v * s) / (s * s)]  s ` is orthogonal to `s` because their dot product is ZERO.

[The distance from `(x0, y0)` to a line defined by `ax+by+c = 0`](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line)

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

Note that if `cross(a, b)` is positive then the `b` is at the anti-crosswise direction of `a` within 180 degree. (right-hand rule)



**LC 469. Convex Polygon**
---
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex.

Every boundary edge should turn towards the same direction, either all clockwise or all counter-clockwise.
Use right-hand rule (cross product) to check that.

```
    def isConvex(self, points):
        N = len(points)
        clock, aclock = 0, 0
        for i in range(N):
            j = (i + 1) % N
            k = (i + 2) % N
            ax, ay = points[j][0] - points[i][0], points[j][1] - points[i][1]
            bx, by = points[k][0] - points[j][0], points[k][1] - points[j][1]
            if ax * by - bx * ay < 0:
                aclock += 1
            if ax * by - bx * ay > 0:
                clock += 1
                
        if aclock > 0 and clock > 0: return False
        return True
```

**LC 587. Erect the Fence**
---
Find convex hull given a set of points. 

Monotone Chain Algorithm (sort the points by `(x, -y)`).
```
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if not points: return []
        
        p = sorted([(_.x, _.y) for _ in points], key=lambda x: (x[0], -x[1]))
        n = len(points)
        
        def cross(a, b, x, y):
            #print(a, b, x, y)
            return a * y - b * x
        
        L = []
        for i in range(n):
            while len(L) > 1 and \
                cross(L[-1][0] - L[-2][0], L[-1][1] - L[-2][1], p[i][0] - L[-2][0], p[i][1] - L[-2][1]) < 0:
                    L.pop()
            L.append(p[i])
       
        H = []
        for i in range(n-1, -1, -1):
            while len(H) > 1 and \
                cross(H[-1][0] - H[-2][0], H[-1][1] - H[-2][1], p[i][0] - H[-2][0], p[i][1] - H[-2][1]) < 0:
                    H.pop()
            H.append(p[i])
        
        return [Point(x, y) for x, y in set(L + H)]
 ```

