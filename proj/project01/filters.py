from byuimage import Image

def display( arg_list ):
    Image( arg_list[ 2 ] ).show( )


def darken( arg_list ):
    in_filename = arg_list[ 2 ]
    out_filename = arg_list[ 3 ]
    percent = float( arg_list[ 4 ] )
    image = Image( in_filename )

    for pixel in image:
        pixel.red = pixel.red * ( 1 - percent )
        pixel.green = pixel.green * ( 1 - percent )
        pixel.blue = pixel.blue * ( 1 - percent )

    image.save( out_filename )


def sepia( arg_list ):
    in_filename = arg_list[ 2 ]
    out_filename = arg_list[ 3 ]
    image = Image( in_filename )

    for pixel in image:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue

        pixel.red = true_red if true_red < 255 else 255
        pixel.green = true_green if true_green < 255 else 255
        pixel.blue = true_blue if true_blue < 255 else 255

    image.save( out_filename )


def grayscale( arg_list ):
    in_filename = arg_list[ 2 ]
    out_filename = arg_list[ 3 ]
    image = Image( in_filename )

    for pixel in image:
        average = ( pixel.red + pixel.green + pixel.blue ) / 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average

    image.save( out_filename )


def make_borders( arg_list ):
    in_filename = arg_list[ 2 ]
    out_filename = arg_list[ 3 ]
    border_thickness = int( arg_list[ 4 ] )
    r_value = int( arg_list[ 5 ] )
    g_value = int( arg_list[ 6 ] )
    b_value = int( arg_list[ 7 ] )

    original_image = Image( in_filename )
    bordered_image = Image.blank(
        original_image.width + border_thickness * 2 ,
        original_image.height + border_thickness * 2 )

    # set whole image to border color
    for j in range( bordered_image.height ):
        for i in range( bordered_image.width ):
            pixel = bordered_image.get_pixel( i , j )
            pixel.color = ( r_value , g_value , b_value )

    # copy original image to middle
    for j in range( original_image.height ):
        for i in range( original_image.width ):
            original_pixel = original_image.get_pixel( i , j )
            new_pixel = bordered_image.get_pixel( i + border_thickness , j + border_thickness )
            new_pixel.color = original_pixel.color

    bordered_image.save( out_filename )


def flip(arg_list):
    in_filename = arg_list[ 2 ]
    out_filename = arg_list[ 3 ]
    original_image = Image(in_filename)
    new_image = Image.blank( original_image.width , original_image.height )

    for j in range( original_image.height ):
        for i in range( original_image.width ):
            original_pixel = original_image.get_pixel( i , j )
            new_pixel = new_image.get_pixel( i , new_image.height - j - 1 )

            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue

    new_image.save( out_filename )


def mirror( arg_list ):
    in_filename = arg_list[ 2 ]
    out_filename = arg_list[ 3 ]
    original_image = Image( in_filename )
    new_image = Image.blank( original_image.width , original_image.height )

    for j in range( original_image.height ):
        for i in range( original_image.width ):
            original_pixel = original_image.get_pixel( i , j )
            new_pixel = new_image.get_pixel( new_image.width - i - 1 , j )

            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue

    new_image.save( out_filename )


def collage( arg_list ):
    image_1 = Image( arg_list[ 2 ] )
    image_2 = Image( arg_list[ 3 ] )
    image_3 = Image( arg_list[ 4 ] )
    image_4 = Image( arg_list[ 5 ] )
    out_filename = arg_list[ 6 ]
    border_thickness = int( arg_list[ 7 ] )

    # idea -> just call make_borders on each image, and then combine the new images into one - nah, same as make_borders
    # blank canvas the right size
    collage_image = Image.blank( image_1.width * 2 + border_thickness * 3 , image_1.height * 2 + border_thickness * 3 )

    # set whole canvas to black
    for j in range( collage_image.height ):
        for i in range( collage_image.width ):
            collage_pixel = collage_image.get_pixel( i , j )
            collage_pixel.color = ( 0 , 0 , 0 )

    # copy images in right spots
    def copy_image(original_image, new_image, i_difference, j_difference):
        for j in range( original_image.height ):
            for i in range( original_image.width ):
                original_pixel = original_image.get_pixel( i , j )
                new_pixel = new_image.get_pixel( i + i_difference , j + j_difference )

                new_pixel.color = original_pixel.color

    copy_image( image_1 , collage_image , border_thickness , border_thickness )
    copy_image( image_2 , collage_image , image_2.width + border_thickness * 2 , border_thickness )
    copy_image( image_3 , collage_image , border_thickness, image_3.height + border_thickness * 2 )
    copy_image( image_4 , collage_image , image_4.width + border_thickness * 2 , image_4.height + border_thickness * 2 )

    collage_image.save( out_filename )


def greenscreen( arg_list ):
    front_image = Image( arg_list[ 2 ] )
    back_image = Image( arg_list[ 3 ] )
    out_filename = arg_list[ 4 ]
    green_threshold = int( arg_list[ 5 ] )
    green_factor = float( arg_list[ 6 ] )

    def detect_green( pixel , threshold=green_threshold , factor=green_factor ):
        average = ( pixel.red + pixel.green + pixel.blue ) / 3
        return ( pixel.green >= average * factor ) and ( pixel.green > threshold )

    new_image = Image.blank( back_image.width , back_image.height )
    for j in range( new_image.height ):
        for i in range( new_image.width ):
            back_pixel = back_image.get_pixel( i , j )
            front_pixel = front_image.get_pixel( i , j )
            new_pixel = new_image.get_pixel( i , j )

            if detect_green( front_pixel ):
                new_pixel.color = back_pixel.color
            else:
                new_pixel.color = front_pixel.color

    new_image.save( out_filename )

