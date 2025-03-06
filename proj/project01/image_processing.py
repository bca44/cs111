import sys
from filters import *

def validate_command(arg_list):
    flag = arg_list[1]

    flag_length_dict = {
        # keys = valid command flags
        # values = min length a command with that flag must have
        "-d": 3,
        "-k": 5,
        "-s": 3,
        "-g": 3,
        "-b": 7,
        "-f": 4,
        "-m": 4,
        "-c": 8,
        "-y": 7
    }

    return len(arg_list) >= flag_length_dict[flag] if flag in flag_length_dict else False


def execute_command(arg_list):
    flag = arg_list[1]

    flag_function_dict = {
        # keys = command flags
        # values = corresponding func to make desired change to image
        "-d": display,
        "-k": darken,
        "-s": sepia,
        "-g": grayscale,
        "-b": make_borders,
        "-f": flip,
        "-m": mirror,
        "-c": collage,
        "-y": greenscreen
    }

    flag_function_dict[flag](arg_list)


def help_message():
    print("Invalid command!\nHere is a list of valid commands:\n" +
          "Display: -d <image file> : displays the image\n" +
          "Darken: -k <input file> <output file> <percent> : darkens the image by the specified percent\n" +
          "Sepia: -s <input file> <output file> : converts the image to sepia\n" +
          "Grayscale: -g <input file> <output file> : converts the image to grayscale\n" +
          "Border: -b <input file> <output file> <thickness> <red> <green> <blue> : creates a border around the image\n" +
          "Flip: -f <input file> <output file> : flips the image horizontally\n" +
          "Mirror: -m <input file> <output file> : mirrors the image vertically\n"
          )


if __name__ == '__main__':

    if validate_command( sys.argv ):
        print( "Executing command..." )
        execute_command( sys.argv )

    else:
        help_message()
