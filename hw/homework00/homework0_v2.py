## CONSTANTS SHOULD GO BELOW THIS COMMENT ##

PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1

LARGE_PRICE = 14.68
MEDIUM_PRICE = 11.48
SMALL_PRICE = 7.28

LARGE_DIAMETER = 20
MEDIUM_DIAMETER = 16
SMALL_DIAMETER = 12

PI = 3.14159265

def main():
    num_guests = int( input( "Please enter how many guests to order for: " ) )

    def calc_num_pizzas( how_many_people , people_per_large = PEOPLE_PER_LARGE ,
                         people_per_medium = PEOPLE_PER_MEDIUM ,
                         people_per_small = PEOPLE_PER_SMALL ):

        num_large = num_guests // people_per_large
        num_medium = (num_guests % people_per_large) // people_per_medium
        num_small = ((num_guests % people_per_large) % people_per_medium) // people_per_small

        return num_large , num_medium , num_small

    num_large_needed , num_medium_needed , num_small_needed = calc_num_pizzas( num_guests )
    print( f"{ num_large_needed } large pizzas, { num_medium_needed } medium pizzas,"
          f" and { num_small_needed } small pizzas will be needed." )

    def calc_total_area(num_l, num_m, num_s, diameter_l = LARGE_DIAMETER,
                        diameter_m = MEDIUM_DIAMETER, diameter_s = SMALL_DIAMETER, pi = PI):

        return ( pi / 4 ) * ((diameter_l ** 2) + (diameter_m ** 2) + (diameter_s ** 2))

    total_area = calc_total_area( num_large_needed , num_medium_needed , num_small_needed )
    print( f"A total of {total_area:.2f} square inches of pizza will be ordered"
           f" ({( total_area / num_guests ):.2f} per guest)." )

    raw_tip = int( input( "Please enter the tip as a percentage (i.e. 10 means 10%): " ) )
    tip_percentage = 1 + ( raw_tip / 100 )

    def calc_total_cost( num_large , num_medium , num_small ,
                         price_l = LARGE_PRICE , price_m = MEDIUM_PRICE , price_s = SMALL_PRICE ):

        return ( num_large * price_l ) + ( num_medium + price_m ) + ( num_small + price_s )

    total_cost = calc_total_cost( num_large_needed , num_medium_needed , num_small_needed )
    print( f"The total cost of the event will be: ${total_cost:.2f})" )

if __name__ == "__main__":
    main()
