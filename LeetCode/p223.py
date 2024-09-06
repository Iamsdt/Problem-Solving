class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        coxl, coyl=max(ax1,bx1), max(ay1,by1)
        coxr, coyr =min(ax2,bx2), min(ay2,by2)
        dx=coxr-coxl
        dy=coyr-coyl
        overlap = 0
        if dx>0 and dy>0:
            overlap=dx*dy
        a=abs(ax2-ax1)*abs(ay2-ay1)
        b=abs(bx2-bx1)*abs(by2-by1)
        area=a+b-overlap
        return area


if __name__ == "__main__":
    print(Solution().computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))