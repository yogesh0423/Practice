class Solution:
    def largestTriangleArea(self, points):
        num = len(points)
        result = 0.0

        for i in range(num):
            x1, y1 = points[i]
            for j in range(i + 1, num):
                x2, y2 = points[j]
                for k in range(j + 1, num):
                    x3, y3 = points[k]

                    area = abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    ) / 2.0

                    result = max(result, area)

        return result
