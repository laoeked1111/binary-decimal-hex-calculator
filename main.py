
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
        
        elif(int_type == "decimal"):
            print(f"Decimal: {user_in}")
            print(f"Binary: {calcs.dec_to_bin(user_in)}")
            print(f"Hexadecimal: {calcs.dec_to_hex(user_in)}")
            user_in = input(input_msg)

        elif(int_type == "binary"):
            user_in = calcs.bin_to_dec(user_in)
            print(f"Decimal: {user_in}")
            print(f"Binary: {calcs.dec_to_bin(user_in)}")
            print(f"Hexadecimal: {calcs.dec_to_hex(user_in)}")
            user_in = input(input_msg)

        elif(int_type == "hexadecimal"):
            user_in = calcs.hex_to_dec(user_in)
            print(f"Decimal: {user_in}")
            print(f"Binary: {calcs.dec_to_bin(user_in)}")
            print(f"Hexadecimal: {calcs.dec_to_hex(user_in)}")
            user_in = input(input_msg)