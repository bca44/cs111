POINTS_PER_LAB = 20
POINTS_PER_HW = 50
POINTS_PER_PROJ = 100
POINTS_PER_MIDTERM1 = 40
POINTS_PER_MIDTERM2 = 40
POINTS_PER_FINAL = 70

LAB_WEIGHT = .10
HW_WEIGHT = .15
PROJ_WEIGHT = .25
MIDTERM1_WEIGHT = .15
MIDTERM2_WEIGHT = .15
FINAL_WEIGHT = .20

def make_grade_lists( raw_data , category_name ):
    return [ int(i.split(",")[1].strip()) for i in [ line for line in raw_data if ( category_name in line.split( "," )[ 0 ] ) and
             not ( "#" in line.split( "," )[ 0 ] ) ] ]


def determine_max_points( grades_list , points_per ):
    return len( grades_list ) * points_per if len( grades_list ) > 0 else 0


def determine_letter_grade(class_grade):
    grade_cutoffs = [93 , 90 , 87 , 83 , 80 , 77 , 73 , 70 , 67 , 63 , 60 ]
    for i in range( len( grade_cutoffs ) ):
        if class_grade >= grade_cutoffs[ i ]:
            return [ "A" , "A-" , "B+" , "B" , "B-" , "C+" , "C" , "C-" , "D+" , "D" , "D-" ][ i ]
    return "F"


def determine_category_grade( grades_list , max_points ):
    return ( sum( grades_list ) / max_points ) * 100 if max_points > 0 else 0


def main( input_filename ):
    with open( input_filename ) as f:
        raw_data = f.readlines()

    lab_grades = make_grade_lists( raw_data , "Lab" )
    hw_grades = make_grade_lists( raw_data , "Homework" )
    proj_grades = make_grade_lists( raw_data , "Project" ) + make_grade_lists( raw_data , "FreeCoding" )
    midterm_1_grades = make_grade_lists( raw_data , "Midterm1" )
    midterm_2_grades = make_grade_lists( raw_data , "Midterm2" )
    final_grades = make_grade_lists( raw_data , "Final" )

    # drop lowest 2 labs and lowest 1 hw
    lab_grades.sort( ) , hw_grades.sort( )
    lab_grades = lab_grades[ 2 : ]
    hw_grades = hw_grades[ 1 : ]

    lab_points_max = determine_max_points( lab_grades , POINTS_PER_LAB )
    hw_points_max = determine_max_points( hw_grades , POINTS_PER_HW )
    proj_points_max = determine_max_points( proj_grades , POINTS_PER_PROJ )
    midterm_1_points_max = determine_max_points( midterm_1_grades , POINTS_PER_MIDTERM1 )
    midterm_2_points_max = determine_max_points( midterm_2_grades , POINTS_PER_MIDTERM2 )
    final_points_max = determine_max_points( final_grades , POINTS_PER_FINAL )

    # fix weights for case when not each category has a grade
    total_weight = sum( [ weight if len( grades_list ) > 0 else 0 for weight , grades_list in zip(
        [ LAB_WEIGHT , HW_WEIGHT , PROJ_WEIGHT , MIDTERM1_WEIGHT , MIDTERM2_WEIGHT , FINAL_WEIGHT ] ,
        [ lab_grades , hw_grades , proj_grades , midterm_1_grades , midterm_2_grades , final_grades ] ) ] )

    class_grade = sum( [ determine_category_grade( grades_list , max_points ) * ( weight / total_weight) for grades_list , max_points , weight in zip(
        [ lab_grades , hw_grades , proj_grades , midterm_1_grades , midterm_2_grades , final_grades ] ,
        [ lab_points_max , hw_points_max , proj_points_max , midterm_1_points_max , midterm_2_points_max , final_points_max ] ,
        [ LAB_WEIGHT , HW_WEIGHT , PROJ_WEIGHT , MIDTERM1_WEIGHT , MIDTERM2_WEIGHT , FINAL_WEIGHT ] ) ] )

    print( "\n\n" )
    [ print( f"{ category_name}:\t{ sum( grades_list ) }/{ max_points }\t{ determine_category_grade( grades_list, max_points ):.1f}%"
             ) for category_name , grades_list , max_points in zip(
        [ "Labs" , "Homework" , "Projects" , "Midterm 1" , "Midterm 2" , "Final" ] ,
        [ lab_grades , hw_grades , proj_grades , midterm_1_grades , midterm_2_grades , final_grades ] ,
        [ lab_points_max , hw_points_max , proj_points_max , midterm_1_points_max , midterm_2_points_max , final_points_max ]
    ) if len( grades_list ) > 0 ]

    print( f"\nThe overall grade in the class is: { determine_letter_grade( class_grade )} ({ class_grade:.2f}%)")


if __name__ == "__main__":
    main( input( ) )
    # main( "test_files/grades1.test.dat" )
    # main( "test_files/grades2.test.dat" )

