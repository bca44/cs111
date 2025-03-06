from byuimage import Image


def flipped( filename ):
    original_image = Image( filename )
    new_image = Image.blank( original_image.width , original_image.height )

    for j in range( original_image.height ):
        for i in range( original_image.width ):
            original_pixel = original_image.get_pixel( i , j )
            new_pixel = new_image.get_pixel( i , new_image.height - j - 1 )

            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue

    return new_image


def make_borders( filename , border_thickness , border_r_value , border_g_value , border_b_value ):
    original_image = Image( filename )
    new_image = Image.blank(
        original_image.width + border_thickness * 2 ,
        original_image.height + border_thickness * 2 )

    # set whole image to border color
    for j in range( new_image.height ):
        for i in range( new_image.width ):
            pixel = new_image.get_pixel( i , j )
            pixel.color = ( border_r_value , border_g_value , border_b_value )

    # copy original image to middle
    for j in range( original_image.height ):
        for i in range( original_image.width ):
            original_pixel = original_image.get_pixel( i , j )
            new_pixel = new_image.get_pixel( i + border_thickness , j + border_thickness )
            new_pixel.color = original_pixel.color

    return new_image


if __name__ == '__main__':
    # flamingo_flipped = flipped( 'test_files/flamingo-float.png' )
    # flamingo_flipped.show()
    # landscape_border = make_borders( 'test_files/landscape.png' , 30 , 0 , 255 , 0 )
    # landscape_border.show()
    pass

