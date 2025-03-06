if __name__ == "__main__":

    # grab input and correct typing

    an_int = int(input("Enter an integer divisible by 20 => "))

    if an_int % 20 == 0:

        a_float = float(input("Enter a floating point number => "))

        family_name = input("Enter a family relationship (mother, grandfather, cousin, etc.) => ")

        noun = input("Enter a noun => ")

        adj = input("Enter an adjective => ")

        # print madlib

        print(f"{an_int//20} score and {a_float:.3f} years ago, our fore{family_name}s brought forth upon this {noun} a {adj} nation.")

    else:
        print(f"{an_int} is not divisible by 20!")
