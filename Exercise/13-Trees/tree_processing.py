# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

def is_leaf(tree):
    return not branches(tree)

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leave(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leave(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def count_paths(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])

t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])

print(count_paths(t, 3))