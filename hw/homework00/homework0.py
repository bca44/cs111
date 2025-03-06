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
    num_guests = int( input( "Please enter how many guests to order for: ") )

    num_large = num_guests // PEOPLE_PER_LARGE
    num_medium = ( num_guests % PEOPLE_PER_LARGE ) // PEOPLE_PER_MEDIUM
    # if remainder of small pizzas is >0, then add another pizza
    num_small = ( ( num_guests % PEOPLE_PER_LARGE ) % PEOPLE_PER_MEDIUM ) // PEOPLE_PER_SMALL
    if ( ( num_guests % PEOPLE_PER_LARGE ) % PEOPLE_PER_MEDIUM ) % PEOPLE_PER_SMALL > 0:
        num_small += 1

    large_area = PI * ( ( LARGE_DIAMETER / 2 ) ** 2 )
    medium_area = PI * ( ( MEDIUM_DIAMETER / 2 ) ** 2 )
    small_area = PI * ( ( SMALL_DIAMETER / 2 ) ** 2 )

    total_area = ( large_area * num_large ) + ( medium_area * num_medium ) + ( small_area * num_small )

    area_per_guest = total_area / num_guests

    print(f"{num_large} large pizzas, {num_medium} medium pizzas, and {num_small} "
          f"small pizzas will be needed.")
    print()

    print(f"A total of {total_area:.2f} square inches of pizza will be ordered ({area_per_guest:.2f} per guest).")
    print()

    tip_percent = int( input( "Please enter the tip as a percentage (i.e. 10 means 10%): " ) )
    tip_multiplier = 1 + ( tip_percent / 100 )

    pre_tip_cost = num_large * LARGE_PRICE + num_medium * MEDIUM_PRICE + num_small * SMALL_PRICE
    total_cost = pre_tip_cost * tip_multiplier

    print(f"The total cost of the event will be: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
