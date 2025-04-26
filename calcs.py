

def get_type(user_in):
    """
    Given a user-inputted integer, returns if the input was a binary, decimal, or hexadecimal number.

    Args:
        user_in: str, the user's inputted integer

    Ret:
        str, "binary", "hexadecimal", "decimal", or "INVALID"
    """

    assert isinstance(user_in, str), AssertionError("Input must be a string.")

    try:

        if(len(user_in) == 0): 
            return "INVALID"

        temp = user_in 
        if(len(user_in) > 2 and (user_in[:2] == "0b" or user_in[:2] == "0x")):
            temp = user_in[2:]

        if user_in[:2] == "0b":
            for char in temp:
                if char not in "01":
                    return "INVALID"

            return "binary"

        elif user_in[:2] == "0x":
            for char in temp:
                if char not in "0123456789abcdef":
                    return "INVALID"

            return "hexadecimal"

        else: 
            for char in temp:
                if char not in "0123456789":
                    return "INVALID"
                
            return "decimal"

    except:
        return "INVALID"


########################################
# Conversion Functions #
########################################


def bin_to_dec(num):
    """
    Convert from binary to decimal.

    Args:
        num: str, represents a binary number

    Ret:
        ret: int, represents a decimal number
    """

    assert get_type(num) == "binary", AssertionError("Not a valid binary integer!")
    num = int(num[2:])

    ret = 0

    i = 0
    while(num > 0):
        ret += (2 ** i) * (num % 10)
        i += 1
        num //= 10

    return str(ret) 



def dec_to_bin(num):
    """
    Convert from decimal to binary.

    Args:
        num: str, represents a decimal number

    Ret:
        ret: int, represents a binary number
    """

    assert get_type(num) == "decimal", AssertionError("Not a valid decimal integer!")
    num = int(num)

    ret = 0
    i = 0

    while num > 0:
        ret += (num & 1) * (10 ** i)
        num = num >> 1 
        i += 1

    return "0b" + str(ret)



def hex_to_dec(num):
    pass



def dec_to_hex(num):
    pass




def hex_to_bin(num):
    pass




def bin_to_hex(num):
    pass



if __name__ == "__main__":
    print(dec_to_bin("1"))