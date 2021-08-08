class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        ac = [A, C]
        db = [B, D]

        eg = [E, G]
        hf = [F, H]

        xs = [ac, eg]
        ys = [db, hf]

        xs.sort(key=lambda x: x[0])
        ys.sort(key=lambda x: x[0])


        start = xs[0][0]
        x_overlap = []
        if xs[1][0] < xs[0][1]:
            x_overlap.append(xs[1][0])
            x_overlap.append(min(xs[0][1],xs[1][1]))

        y_overlap = []
        if ys[1][0] < ys[0][1]:
            y_overlap.append(ys[1][0])
            y_overlap.append(min(ys[0][1], ys[1][1]))

        overlap_area = 0
        if x_overlap and y_overlap:
            overlap_area = (x_overlap[1] - x_overlap[0]) * (y_overlap[1]-y_overlap[0])

        return area1 + area2 - overlap_area


Solution().computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2)
Solution().computeArea(A = -2, B = -2, C = 2, D = 2, E = -2, F = -2, G = 2, H = 2)
