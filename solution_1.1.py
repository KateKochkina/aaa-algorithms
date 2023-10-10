def max_even_sum(arr: list) -> int:
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return total_sum
    best_sum = 0
    arr.sort()  # inplace, or: arr sorted(arr)
    mod_1_elems = [x for x in arr if x % 2 == 1]
    if len(mod_1_elems) > 0:
        best_sum = max(best_sum, total_sum - mod_1_elems[0])
    return best_sum

def solution():
    arr = [int(x) for x in input().split()]
    result = max_even_sum(arr)
    print(result)

solution()