
from itertools import count


def count_partitions(n, m):
    if m == 0:
        return 0
    elif n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        with_n = count_partitions(n, m - 1)
        return with_m + with_n

print(count_partitions(5, 1))