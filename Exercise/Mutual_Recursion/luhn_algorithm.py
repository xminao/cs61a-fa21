
# split the number n into two part(all but last and last)
def split(n):
    return n // 10, n % 10

# plus all digit of number n
def sum_digit(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digit(all_but_last) + last

def sum_luhn(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_luhn_double(all_but_last) + last 

def sum_luhn_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digit(2*last)
    if n < 10:
        return luhn_digit
    else:
        all_but_last, last = split(n)
        return sum_luhn(all_but_last) + luhn_digit

print(sum_luhn(32))