def max_div3_sum(arr: list) -> int:
    total_sum = sum(arr)
    if total_sum % 3 == 0:
        return total_sum
    best_sum = 0
    arr.sort()  # inplace, or: arr sorted(arr)
    mod_1_elems = [x for x in arr if x % 3 == 1]
    mod_2_elems = [x for x in arr if x % 3 == 2]
    if total_sum % 3 == 2:
        # Тогда обратный случай, просто поменяем местами массивы
        mod_1_elems, mod_2_elems = mod_2_elems, mod_1_elems
    if len(mod_1_elems) > 0:
        best_sum = max(best_sum, total_sum - mod_1_elems[0])
    if len(mod_2_elems) > 1:
        best_sum = max(best_sum, total_sum - mod_2_elems[0] - mod_2_elems[1])
    return best_sum


def solution():
    arr = [int(x) for x in input().split()]
    result = max_div3_sum(arr)
    print(result)

solution()
