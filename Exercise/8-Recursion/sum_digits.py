def split(n):
    """Split positive n to all but last and last digit"""
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

print(sum_digits(2022))