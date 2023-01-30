def find_max(list: list) -> int:
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max