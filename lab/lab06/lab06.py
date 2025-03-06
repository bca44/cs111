from operator import add, mul

def product(input_value):
    return_value = 1
    if isinstance( input_value , int ) and input_value >= 1:
        while input_value > 0:
            return_value *= input_value
            input_value -= 1
        return return_value
    raise ValueError( "Input must be an integer greater than or equal to 1." )


def summation( input_value ):
    return_value = 0
    if isinstance( input_value , int ) and input_value > 0:
        while input_value > 0:
            return_value += input_value
            input_value -= 1
        return return_value
    raise ValueError( "Input must be an integer greater than or equal to 1." )


square = lambda x: x * x


sqrt = lambda x: x ** 0.5 # x^0.5 == √x


def mean( numbers ):
    assert isinstance( numbers , list ) , "Must be list"
    assert len( numbers ) > 0 , "Must contain numbers"
    
    total = 0
    for num in numbers:
        total += num

    return total / len( numbers )


def median( numbers ):
    assert isinstance( numbers , list ) , "Must be list"
    assert len( numbers ) > 0 , "Must contain numbers"

    numbers = sorted( numbers )

    if len( numbers ) % 2 == 0:
        right_mid = len( numbers ) // 2
        left_mid = right_mid - 1
        return mean( [ numbers[ left_mid ] , numbers [ right_mid] ] )

    else:
        middle = ( len( numbers ) // 2 )
        return numbers[ middle ]


def mode( numbers ):
    assert isinstance( numbers , list ) , "Must be list"
    assert len( numbers ) > 0 , "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[ running_high_num ] = 0
    for num in numbers:
        if num not in counts:
            counts[ num ] = 1
        else:
            counts[ num ] += 1
        
        if counts[ num ] > counts[ running_high_num ]:
            running_high_num = num

    return running_high_num


def std_dev( numbers ):
    assert isinstance( numbers , list ) , "Must be list"
    assert len( numbers ) > 0, "Must contain numbers"

    avg = mean( numbers )
    total_dist = 0
    for num in numbers:
        total_dist += square( num - avg )

    return sqrt( total_dist / len( numbers ) )


def stat_analysis( numbers ):
    assert isinstance( numbers , list ) , "Must be list"
    assert len( numbers ) > 0 , "Must contain numbers"

    info = { "mean" : mean( numbers ) ,
            "median" : median( numbers ) ,
            "mode" : mode( numbers ) ,
            "std_dev" : std_dev( numbers ) }
    return info

