def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


def multiply(m, n):
    """ Takes two positive integers (including zero) and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 0: # base case: nothing else (0) needs to be added
        return 0
    else:
        return m + multiply(m, n - 1) # recursive case: add m


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def is_prime_helper(factor):
        # base case: if we've reached 1 to check as our factor, then n must be prime
        # recursive case 1: if n % factor == 0, then n not prime
        # recursive case 2: n % factor != 0, try n - 1
        if factor == 1:
            return True
        else:
            if n % factor == 0:
                return False
            else:
                return is_prime_helper(factor - 1)

    return is_prime_helper(n - 1)


# if __name__ == '__main__':
#     is_prime(3)

