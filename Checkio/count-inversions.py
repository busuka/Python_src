def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    loop_cnt = 0
    inv_cnt = 0
    list_sequence = list(sequence)
    while loop_cnt < len(list_sequence):
        i = 0
        while i < len(list_sequence) - 1:
            if list_sequence[i] > list_sequence[i+1]:
                list_sequence[i], list_sequence[i+1] = list_sequence[i+1], list_sequence[i]
                inv_cnt += 1
            i += 1
        loop_cnt += 1
    return inv_cnt


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
