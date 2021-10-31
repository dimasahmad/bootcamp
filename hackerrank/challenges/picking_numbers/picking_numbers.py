# picking numbers
# https://www.hackerrank.com/challenges/picking-numbers/problem

def picking_numbers(numbers: list[int]) -> int:
    """Find the longest subarray where the absolute difference
    between any two elements is `<= 1`.

    Args:
        numbers (list[int]): an array of integers
        
    Returns:
        int: the length of the longest subarray that meets the criterion
    """

    subs: list[list[int]] = []
    subs_len: list[int] = []

    for i in range(len(numbers)):
        sub_n: list[int] = [numbers[i]] # -1
        sub_p: list[int] = [numbers[i]] # +1

        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] == 1:
                sub_n.append(numbers[j])
            elif numbers[i] - numbers[j] == -1:
                sub_p.append(numbers[j])
            elif numbers[i] - numbers[j] == 0:
                sub_n.append(numbers[j])
                sub_p.append(numbers[j])

        subs.append(sub_n)
        subs_len.append(len(sub_n))
        subs.append(sub_p)
        subs_len.append(len(sub_p))

    return max(subs_len)
