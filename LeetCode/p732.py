import bisect

class MyCalendarThree:

    def __init__(self):
        self.ss = []
        self.ee = []
        
        self.k_max = 0

    def book(self, s: int, e: int) -> int:
        bisect.insort_left(self.ss, s)
        bisect.insort_left(self.ee, e)
        
        opened = bisect.bisect_right(self.ss, s)
        closed = bisect.bisect_right(self.ee, s)
        k_cur = opened - closed
        self.k_max = max(self.k_max, k_cur)

        while True:
            
            if opened >= len(self.ss): break
            if self.ss[opened] >= e  : break
            
            if self.ss[opened] < self.ee[closed]:
                opened += 1
            else:
                closed += 1
            
            k_cur = opened - closed        
            self.k_max = max(self.k_max, k_cur)

        return self.k_max