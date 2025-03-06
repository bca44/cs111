from byuimage import Image

def iron_puzzle(filename):
    iron_image = Image( filename )

    for pixel in iron_image:
        pixel.red = 0
        pixel.green = 0
        pixel.blue *= 10

    return iron_image


# iron_solution = iron_puzzle( "test_files/iron.png" )
# iron_solution.show()


def west_puzzle(filename):
    west_image = Image(filename)
    for pixel in west_image:
        if pixel.blue < 16:
            pixel.color = ( 0 , 0 , pixel.blue * 16 )
        else:
            pixel.color = ( 0 , 0 , 0 )
    return west_image


# west_solution = west_puzzle( "test_files/west.png" )
# west_solution.show()


def darken(filename, percent):
    image = Image( filename )
    for pixel in image:
        pixel.red = pixel.red * ( 1 - percent )
        pixel.green = pixel.green * ( 1 - percent )
        pixel.blue = pixel.blue * ( 1 - percent )
    return image


# darkened_cougar = darken( "test_files/cougar.png" , 0.8 )
# darkened_cougar.show()


def grayscale(filename):
    image = Image( filename )
    for pixel in image:
        average = ( pixel.red + pixel.green + pixel.blue ) / 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    return image


def sepia(filename):
    image = Image( filename )
    for pixel in image:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue

        pixel.red = true_red if true_red < 255 else 255
        pixel.green = true_green if true_green < 255 else 255
        pixel.blue = true_blue if true_blue < 255 else 255

    return image


def create_left_border(filename, weight):
    original_image = Image( filename )
    # create new image of proper size
    new_image = Image.blank( original_image.width + weight , original_image.height )

    # make all pixels from ( 0 , 0 ) to ( weight , image.height ) pure blue
    for i in range( weight ):
        for j in range( new_image.height ):
            pixel = new_image.get_pixel( i , j )
            pixel.color = ( 0 , 0 , 255 )

    # copy over original image from ( weight , image.height ) to ( image.width , image.height )
    for i in range( original_image.width ):
        for j in range( original_image.height ):
            pixel = new_image.get_pixel( i + weight , j )
            pixel.color = original_image.get_pixel( i , j ).color

    return new_image


# cougar_with_border = create_left_border( "test_files/cougar.png" , 30 )
# cougar_with_border.show()


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    original_image = Image( filename )
    new_image = Image.blank( original_image.width + 50 ,
                             original_image.height + 25 )

    for i in range( new_image.width ):
        for j in range( new_image.height ):
            pixel = new_image.get_pixel( i , j )
            if j % 2 == 0:
                pixel.color = ( 0 , 255 , 0 )
            elif i % 2 == 1:
                pixel.color = ( 0 , 0 , 255 )
            else:
                pixel.color = ( 255 , 0 , 0 )

    return new_image

# cougar_with_stripes = create_stripes( "test_files/cougar.png" )
# cougar_with_stripes.show()


def copper_puzzle(filename):
    image = Image( filename )

    for j in range( image.height ):
        for i in range( image.width ):
            pixel = image.get_pixel( i , j )
            pixel.red = 0
            pixel.green *= 20
            pixel.blue *= 20

    return image


# copper_solution = copper_puzzle( "test_files/copper.png" )
# copper_solution.show()
