
import calcs

if __name__ == "__main__":
    print('Welcome to this binary/decimal/hex calculator! Enter Q to quit anytime.')

    input_msg = "Enter a positive integer. Use the prefix 0b for binary, 0x for hexadecimal, and no prefix for decimal: "
    user_in = input(input_msg)

    while(user_in not in ["q", "Q"]):
        int_type = calcs.get_type(user_in)
        print(f"Your input was {user_in}. This is a {int_type} integer.")

        if(int_type == "INVALID"):
            user_in = input(input_msg)
            continue


        