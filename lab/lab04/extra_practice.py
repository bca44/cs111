def largest_factor(n):
    """
    >>> largest_factor( 9 )
    3
    >>> largest_factor( 98 )
    49
    """
    if n == 0:
        return 0
    else:
        biggest_factor = 1
        i = 2
        while i <= n // 2:
            if n % i == 0:
                biggest_factor = i
            i += 1

        return biggest_factor

def missing_digits(n):
    """
    >>> missing_digits( 346 )
    1
    >>> missing_digits( 1278 )
    4
    """
    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        diff = last_digit - second_to_last_digit
        if diff > 1:
            counter += ( diff - 1 )
        n //= 10

    return counter
