def binary_search(ls, num):
    first_idx = 0
    second_idx = len(ls)
    while True:
        if ls[(second_idx - first_idx) // 2 + first_idx] < num:
            first_idx = (second_idx - first_idx) // 2 + first_idx
        elif ls[(second_idx - first_idx) // 2 + first_idx] > num:
            second_idx = (second_idx - first_idx) // 2 + first_idx
        else:
            return (second_idx - first_idx) // 2 + first_idx


sorted_array = [1, 3, 4, 5, 7, 8, 12, 13, 14, 18, 30, 32, 41, 55]

print(binary_search(sorted_array, 13))
