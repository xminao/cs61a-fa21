
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 0:
        return 0
    else:
        if pos % 10 == 8:
            return 1 + num_eights(pos // 10)
        else:
            return num_eights(pos // 10)

def pingpong(n):
    flag = 1
    index = 1
    value = 1
    while index < n:
        value = value + flag
        index += 1
        if num_eights(index) > 0 or index % 8 == 0:
            flag = 0 - flag
    return value

print(pingpong(30))