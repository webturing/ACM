class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

    @staticmethod
    def cross(r1, r2):
        return abs((r1.x1 + r1.x2) / 2 - (r2.x1 + r2.x2) / 2) < ((r1.x2 + r2.x2 - r1.x1 - r2.x1) / 2) and abs(
            (r1.y1 + r1.y2) / 2 - (r2.y1 + r2.y2) / 2) < ((r1.y2 + r2.y2 - r1.y1 - r2.y1) / 2)

    @staticmethod
    def crossArea(r1, r2):
        if not Rect.cross(r1, r2):
            return 0
        else:
            minx = max(r1.x1, r2.x1)
            miny = max(r1.y1, r2.y1)
            maxx = min(r1.x2, r2.x2)
            maxy = min(r1.y2, r2.y2)
            return abs((maxx - minx) * (maxy - miny))


x0, y0, x1, y1 = map(float, raw_input().strip().split())
x2, y2, x3, y3 = map(float, raw_input().strip().split())
r1, r2 = Rect(x0, y0, x1, y1), Rect(x2, y2, x3, y3)
print '%.2f' % Rect.crossArea(r1, r2)
