def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    # return_list = [ ]
    # for i in range( len( s ) ) :
    #     if i % 2 == 0:
    #         i *= s[ i ]
    #         return_list.append( i )
    # return return_list
    return [ i * s[ i ] for i in range( len( s ) ) if i % 2 == 0 ]

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    # return_list = [ ]
    # for i in range( len( s ) ):
    #     return_list.append( [ s[ i ] , t[ i ] ] )
    # return return_list
    return [ [ s[ i ], t[ i ] ] for i in range( len( s ) ) ]

def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    with open( input_filename ) as input_file:
        copy_this = input_file.readlines()
    with open( output_filename , "w" ) as output_file:
        output_file.writelines( [f"{ i + 1 }: { copy_this[ i ] }" for i in range( len( copy_this ) ) ])

########################################################
# OPTIONAL QUESTIONS

def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    # Write your code here
