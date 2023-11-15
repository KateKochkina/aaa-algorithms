import heapq


def get_kth_element(arr: list, k: int):
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
    kth_smallest = None
    for j in range(k + 1):
        kth_smallest = heapq.heappop(heap)
    return kth_smallest


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))

solution()
