import sys

def is_valid_flag(arg_list):
    if arg_list[ 1 ] in [ "-p" , "-i" , "-h" , "-w" , "-r" ]:
        return True
    return False


def print_args(arg_list):
    for arg in arg_list:
        print( arg )


def write_file( arg_list ):
    # arg_list ex: "python3 lab09.py -w output.txt Hello World"
    # will look like ["lab09" , "-w" , "output.txt" , "Hello" , "World" ]
    if len( arg_list ) > 3:
        with open( arg_list[ 2 ] , "w" ) as output_file:
            for line in arg_list[ 3: ]:
                output_file.write( line + "\n" )
    else:
        print( "No Content Provided" )


def help_message():
    print("Valid flags:\n" +
          "-p : prints out all the command line arguments after the -p\n" +
          "-i : prints \"Hello World\"\n" +
          "-h : prints out a help command")


def read_file( arg_list ):
    with open( arg_list[ 2 ] , "r" ) as input_file:
        lines = input_file.readlines()
        [ print( line.strip() ) for line in lines ]


def flags(arg_list):
    flag = arg_list[ 1 ]

    if flag == "-p":
        print_args( arg_list[ 2: ] )

    elif flag == "-i":
        print( "Hello World" )

    elif flag == "-w":
        write_file( arg_list )

    elif flag == "-h":
        help_message()

    elif flag == "-r":
        read_file( arg_list )


def main( arg_list ):
    if is_valid_flag( arg_list ):
        flags( arg_list )
    else:
        print_args( arg_list )


if __name__ == "__main__":
    # main( [ "lab09" , "-w" , "lab/lab09/output_file.txt" , "Hello" , "World" ] )
    # main( ["filename" , "-r" , "output_file.txt" ] )
    main( sys.argv )
