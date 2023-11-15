import heapq

class StreamMedian:
    def __init__(self):
        self.lower_half = []  # max-heap
        self.higher_half = []  # min-heap

        
    def add_num(self, num: int) -> None:
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.higher_half, num)
            
        if len(self.lower_half) > len(self.higher_half) + 1:
            heapq.heappush(self.higher_half, -heapq.heappop(self.lower_half))
        elif len(self.higher_half) > len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappop(self.higher_half))

            
    def find_median(self) -> float:
        if len(self.lower_half) == len(self.higher_half):
            return (-self.lower_half[0] + self.higher_half[0]) / 2
        else:
            return -self.lower_half[0]


def solution():
    n = int(input())
    stream = StreamMedian()
    for i in range(n):
        line = input().split()
        command = line[0]
        if command == "ADD":
            stream.add_num(int(line[1]))
        elif command == "FIND_MEDIAN":
            print(f'{stream.find_median():.1f}')


solution()