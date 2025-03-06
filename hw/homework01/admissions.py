def convert_to_float( row ):
    """
    :param row: a list whose elements need to be floats
    :return: a list of floats
    """
    return [ row[ i ] if i == 0 else float( row[ i ] ) for i in range( len( row ) ) ]


def check_row_types( row ):
    """
    This function checks to ensure that a list is of length
    8 and that each element is type float

    Parameters:
    row - a list to check
    :return: True if the length of row is 8 and all elements are floats
    """
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


def calculate_score( score_row ):
    """
    :param score_row: list[ float ] - student's SAT, GPA, demonstrated interest, and HS quality
    :return: weighted score

    >>> calculate_score( [1300.0 , 3.61 , 10.0 , 7.0 ] )
    7.7255
    """
    return ((score_row[ 0 ] / 160) * 0.3) + ((score_row[ 1 ] * 2) * 0.4) + (score_row[ 2 ] * 0.1) + (score_row[ 3 ] * 0.2)


def is_outlier( score_row ):
    """
    :param score_row: row containing GPA and interest scores
    :return: True if score_row is outlier, otherwise False
    """
    return ( score_row[ 2 ] == 0 ) or ( ( score_row[ 1 ] * 2 ) - ( score_row[ 0 ] / 160 ) > 2 )


def calculate_score_improved( score_row ):
    """
    :param score_row: list[ float ] - student's SAT, GPA, demonstrated interest, and HS quality
    :return: weighted score and True if outlier, False if not
    """
    score = calculate_score( score_row )
    if score > 6.0 or is_outlier( score_row ):
        return True
    return False


def grade_outlier( grade_row ):
    """
    :param grade_row: row containing any number of grades
    :return: True if exactly one number is more than 20 points lower than all other numbers
    >>> grade_outlier( [ 99 , 94 , 87 , 89 , 56 , 78 , 89 ] )
    True
    """
    return sorted( grade_row )[ 1 ] - sorted( grade_row  )[ 0 ] > 20


def grade_improvement( grade_row ):
    """
    :param grade_row: row containing semester grades
    :return: True if each semester score is >= previous score, False if otherwise
    >>> grade_improvement( [ 50 , 50 , 60 , 70 , 80 ] )
    True
    >>> grade_improvement( [ 50 , 40 ] )
    False
    """
    return all( [ ( grade_row[ i ] >= grade_row[ i - 1 ] ) for i in range( 1 , len( grade_row ) ) ] )


def main():
    filename = "admission_algorithms_dataset.csv"
    print("Processing " + filename + "...")

    with open( filename , "r" ) as input_file:
        headers = input_file.readline()
        content = input_file.readlines()

    content = [ convert_to_float( row.split( "," ) ) for row in content ]

    if all( [ check_row_types( row[ 1 :] ) for row in content ] ) :

        names = [ row[ 0 ] for row in content ]
        summary_scores = [ row[ 1 : 5 ] for row in content ]
        semester_grades = [ row[ 5 : ] for row in content ]
        calculated_scores = [ calculate_score( summary_scores[ i ] ) for i in range( len( summary_scores ) ) ]

        print("done!")

        with open( "student_scores.csv" , "a" ) as output_file:
            [ output_file.write( f"{ names[ i ] },{ calculated_scores[ i ]:.2f}\n" ) for i in range( len( content ) ) ]

        with open( "chosen_students.csv" , "a" ) as output_file:
            [ output_file.write( f"{ names[ i ] }\n" ) for i in range( len( content ) ) if calculated_scores[ i ] >= 6.0 ]

        with open( "outliers.csv" , "a" ) as output_file:
            [ output_file.write( f"{ names[ i ] }\n" ) for i in range( len( content ) ) if is_outlier( summary_scores[ i ] ) ]

        with open( "chosen_improved.csv" , "a" ) as output_file:
            [ output_file.write( f"{ names[ i ] }\n" ) for i in range( len( content) )
              if ( ( calculated_scores[ i ] > 6.0 ) or ( ( calculated_scores[ i ] > 5.0 ) and ( is_outlier( summary_scores[ i ] ) ) ) ) ]

        with open( "better_improved.csv" , "a" ) as output_file:
            [ output_file.write( f"{ names[ i ] },{ summary_scores[ i ][ 0 ] },{ summary_scores[ i ][ 1 ] },{ summary_scores[ i ][ 2 ] },{ summary_scores[ i ][ 3 ] }\n" )
              for i in range( len( content ) ) if calculate_score_improved( summary_scores[ i ] ) ]

        with open( "composite_chosen.csv" , "a" ) as output_file:
            [ output_file.write( f"{ names[ i ] }\n" ) for i in range( len( content ) ) if calculated_scores[ i ] >= 6.0 or
              ( calculated_scores[ i ] >= 5.0 and ( ( is_outlier( summary_scores[ i ] ) ) or ( grade_outlier( semester_grades[ i ] ) ) or ( grade_improvement( semester_grades[ i ] ) ) ) ) ]

    else:
        print( "Error: type issue!" )


if __name__ == "__main__":
    main()
