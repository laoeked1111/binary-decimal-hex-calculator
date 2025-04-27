
import calcs

if __name__ == "__main__":
    print('Welcome to this binary/decimal/hex calculator! Enter Q to quit anytime.')

    input_msg = "------------------------\nEnter an integer. Use the prefix 0b for binary, 0x for hexadecimal, and no prefix for decimal: "
    user_in = input(input_msg)

    while(user_in not in ["q", "Q"]):
        int_type = calcs.get_type(user_in)
        print(f"Your input was {user_in}. This is a {int_type} integer.")

        if(int_type == "INVALID"):
            user_in = input(input_msg)
            continue
        
        elif(int_type == "decimal"):

            isSigned = input("Unsigned or signed? (u/s): ")

            if isSigned == "s" or isSigned == "S":
                print(f"\nDecimal: {user_in}")
                print(f"Signed binary: {calcs.signed_dec_to_bin(user_in)}")
                print(f"Signed hexadecimal: {calcs.signed_dec_to_hex(user_in)}")
                user_in = input(input_msg)
                continue
            elif isSigned == "u" or isSigned == "U":

                if(int(user_in) < 0):
                    print("Unsigned integers must be non-negative.")
                    user_in = input(input_msg)
                    continue

                print(f"\nDecimal: {user_in}")
                print(f"Unsigned binary: {calcs.unsigned_dec_to_bin(user_in)}")
                print(f"Unsigned hexadecimal: {calcs.unsigned_dec_to_hex(user_in)}")
                user_in = input(input_msg)
                continue
            else:
                print("Invalid input.")
                user_in = input(input_msg)
                continue

        elif(int_type == "binary"):

            isSigned = input("Unsigned or signed? (u/s): ")

            if isSigned == "s" or isSigned == "S":
                print(f"\nDecimal: {calcs.signed_bin_to_dec(user_in)}")
                print(f"Signed binary: {user_in}")
                print(f"Signed hexadecimal: {calcs.signed_bin_to_hex(user_in)}")
                user_in = input(input_msg)
                continue
            elif isSigned == "u" or isSigned == "U":
                temp = calcs.unsigned_bin_to_dec(user_in)
                print(f"\nDecimal: {temp}")
                print(f"Unsigned binary: {user_in}")
                print(f"Unsigned hexadecimal: {calcs.unsigned_bin_to_hex(user_in)}")
                user_in = input(input_msg)
                continue
            else:
                print("Invalid input.")
                user_in = input(input_msg)
                continue

        elif(int_type == "hexadecimal"):

            isSigned = input("Unsigned or signed? (u/s): ")

            if isSigned == "s" or isSigned == "S":
                temp = calcs.signed_hex_to_dec(user_in)
                print(f"\nDecimal: {temp}")
                print(f"Signed binary: {calcs.signed_hex_to_bin(user_in)}")
                print(f"Signed hexadecimal: {user_in}")
                user_in = input(input_msg)
                continue
            elif isSigned == "u" or isSigned == "U":
                temp = calcs.unsigned_hex_to_dec(user_in)
                print(f"\nDecimal: {temp}")
                print(f"Unsigned binary: {calcs.unsigned_hex_to_bin(user_in)}")
                print(f"Unsigned hexadecimal: {user_in}")
                user_in = input(input_msg)
                continue
            else:
                print("Invalid input.")
                user_in = input(input_msg)
                continue

