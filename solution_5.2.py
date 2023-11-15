import heapq


def merge_k_sorted(arrs: list) -> list:
    heap = []
    for i, arr in enumerate(arrs):
        if arr:
            heap.append((arr[0], i, 0))
    heapq.heapify(heap)
    merged = []
    while heap:
        val, arr_idx, idx = heapq.heappop(heap)
        merged.append(val)
        if idx + 1 < len(arrs[arr_idx]):
            heapq.heappush(heap, (arrs[arr_idx][idx + 1], arr_idx, idx + 1))
    return merged


def solution():
    arrs = read_multiline_input() # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))

solution()