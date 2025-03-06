def digit_counter(func, num):
    """Return the number of digits when func(num) is true
    >>> digit_counter( is_even , 22 )
    2
    >>> digit_counter( is_even , 222 )
    3
    >>> digit_counter( is_even , 3 )
    0
    """
    counter = 0

    while num > 0:
        # print( f" DEBUG: num at start of while iteration {num} ")
        if func( num % 10 ):
            # print( f"DEBUG: num when checking against given func { num % 10 }")
            counter += 1
        num = num // 10
        # print( f"DEBUG: new num { num }")

    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0

def main():
    digit_counter( is_even , 33 )

if __name__ == "__main__":
    main()
