def average_temperature(temps):
    """
    Given a list of temperatures, TEMPS, compute the average
    temperature and return it to the user
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> average_temperature(temp_data)
    75.15
    """
    return round( sum( i for i in temps ) / len( temps ) , 2 )

def hot_days(temps):
    """
    Given a list of temperatures, TEMPS, count the number of days
    more than five degrees above the average.  Print the number of
    days and the average and return the number of days.
    >>> temp_data = [72.2, 68.7, 67.4, 77.3, 81.6, 83.7]
    >>> hot_days(temp_data)
    There were 2 day(s) more than 5 degrees above the average of 75.2.
    2
    """
    average_temp = average_temperature( temps )
    num_hot_days = 0
    for i in temps:
        if ( i - average_temp ) > 5:
            num_hot_days += 1

    print( f"There were { num_hot_days } day(s) "
           f"more than 5 degrees above the average of { round( average_temp , 1 ) }." )
    return num_hot_days

def is_palindrome(word):
    """
    Given a single word, WORD, determine if it is a palindrome or not.
    Print a message that includes the word stating it is or is not a
    palindrome and return True if it is and False otherwise
    >>> is_palindrome('rotator')
    rotator is a palindrome.
    True
    >>> is_palindrome('apple')
    apple is not a palindrome.
    False
    """
    letters = [ i for i in word ]
    for i in range( 1 , len( word ) + 1 ):
        if letters[ i - 1 ] != letters[ -i ]:
            print( f"{ word } is not a palindrome.")
            return False
    print( f"{ word } is a palindrome.")
    return True

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [ i * s[ i ] for i in range( len( s ) ) if i % 2 == 0 ]

# def main():
#     is_palindrome( input( "lab03 "))

# if __name__ == "__main__":
#     main()
