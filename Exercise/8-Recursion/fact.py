def fact(n):
    """The recursion case"""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def fact_iter(n):
    """The iteration case"""
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

print(fact(3))
print(fact_iter(3))