

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
    """
    Convert from hexadecimal to decimal.

    Args:
        num: str, represents a hexadecimal number

    Ret:
        ret: int, represents a decimal number
    """

    assert get_type(num) == "hexadecimal", AssertionError("Not a valid hexadecimal integer!")
    num = num[2:]

    CONVERT = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    ret = 0
    i = 0

    while num != "":
        if num[-1] in CONVERT:
            ret += (16 ** i) * CONVERT[num[-1]]
        else:
            ret += (16 ** i) * int(num[-1], 16)

        i += 1
        num = num[:-1]

    return str(ret)



def dec_to_hex(num):
    """
    Convert from decimal to hexadecimal.

    Args:
        num: str, represents a decimal number

    Ret:
        ret: int, represents a hexadecimal number
    """

    assert get_type(num) == "decimal", AssertionError("Not a valid decimal integer!")
    num = int(num)

    CONVERT = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    ret = ""

    while num > 0:
        if num % 16 in CONVERT:
            ret += CONVERT[num % 16]
        else:
            ret += str(num % 16)

        num //= 16

    return "0x" + ret[::-1]



def hex_to_bin(num):
    """
    Convert from hexadecimal to binary.

    Args:
        num: str, represents a hexadecimal number

    Ret:
        ret: int, represents a binary number
    """

    assert get_type(num) == "hexadecimal", AssertionError("Not a valid hexadecimal integer!")
    num = hex_to_dec(num)

    return dec_to_bin(num)



def bin_to_hex(num):
    """
    Convert from binary to hexadecimal.

    Args:
        num: str, represents a binary number

    Ret:
        ret: int, represents a hexadecimal number
    """

    assert get_type(num) == "binary", AssertionError("Not a valid binary integer!")
    num = bin_to_dec(num)

    return dec_to_hex(num)


if __name__ == "__main__":
    pass