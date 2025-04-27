

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
            int(user_in) # Check if it is a valid decimal integer
            return "decimal"

    except:
        return "INVALID"


########################################
# Unsigned Conversion Functions #
########################################


def unsigned_bin_to_dec(num):
    """
    Convert from unsigned binary to decimal.

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



def unsigned_dec_to_bin(num):
    """
    Convert from decimal to unsigned binary.

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



def unsigned_hex_to_dec(num):
    """
    Convert from unsigned hexadecimal to decimal.

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
            ret += (16 ** i) * int(num[-1])

        i += 1
        num = num[:-1]

    return str(ret)



def unsigned_dec_to_hex(num):
    """
    Convert from decimal to unsigned hexadecimal.

    Args:
        num: str, represents a decimal number

    Ret:
        ret: int, represents a hexadecimal number
    """

    assert get_type(num) == "decimal", AssertionError("Not a valid decimal integer!")
    num = int(num)

    CONVERT = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    ret = ""

    if num == 0:
        return "0x0"

    while num > 0:
        if num % 16 in CONVERT:
            ret += CONVERT[num % 16]
        else:
            ret += str(num % 16)

        num //= 16

    return "0x" + ret[::-1]



def unsigned_hex_to_bin(num):
    """
    Convert from unsigned hexadecimal to unsigned binary.

    Args:
        num: str, represents a hexadecimal number

    Ret:
        ret: int, represents a binary number
    """

    assert get_type(num) == "hexadecimal", AssertionError("Not a valid hexadecimal integer!")
    num = unsigned_hex_to_dec(num)

    return unsigned_dec_to_bin(num)



def unsigned_bin_to_hex(num):
    """
    Convert from unsigned binary to unsigned hexadecimal.

    Args:
        num: str, represents a binary number

    Ret:
        ret: int, represents a hexadecimal number
    """

    assert get_type(num) == "binary", AssertionError("Not a valid binary integer!")
    num = unsigned_bin_to_dec(num)

    return unsigned_dec_to_hex(num)




########################################
# Signed Conversion Functions #
########################################


def sign_flip(num, carry=1):
    """
    Flip the sign of a binary number using two's complement.

    Args:
        num: str, represents a binary number
        carry: int, 0 or 1, represents a carry bit

    Ret:
        ret: str, represents a binary number
    """

    def bit_flip(bit):
        if bit == "0":
            return "1"
        else:
            return "0"


    assert get_type(num) == "binary", AssertionError("Not a valid binary integer!")
    assert carry in [0, 1], AssertionError("Carry must be either 0 or 1.")


    ret = ""

    temp = num[2:]
    while len(temp) > 0:

        # if we are on the last bit, we need to check if we need to add a carry
        if len(temp) == 1:
            if bit_flip(temp[-1]) == "0":
                if carry == 0:
                    ret = "0" + ret
                else:
                    ret = "1" + ret
            
            else:
                if carry == 0:
                    ret = "1" + ret
                else:
                    ret = "10" + ret
            
            break

        if bit_flip(temp[-1]) == "0":
            if carry == 0:
                ret = "0" + ret
            else:
                ret = "1" + ret
            
            carry = 0
        
        else:
            if carry == 0:
                ret = "1" + ret
                carry = 0
            else:
                ret = "0" + ret
        
        temp = temp[:-1]

    # make sure that the sign is correct at the end
    if num[2] == "1" and ret[0] != "0":
        ret = "0" + ret
    elif num[2] == "0" and ret[0] != "1":
        ret = "1" + ret

    return "0b" + ret



def signed_bin_to_dec(num):
    """
    Convert from signed binary to decimal.

    Args:
        num: str, represents a binary number

    Ret:
        ret: int, represents a decimal number
    """

    assert get_type(num) == "binary", AssertionError("Not a valid binary integer!")

    if num[2:] == "0":
        return "0"
    elif num[2:] == "1":
        return "1'"

    temp = -1 * int(num[2]) * (2 ** (len(num) - 3))
    temp += int(unsigned_bin_to_dec("0b" + num[3:]))
    return str(temp)


def signed_dec_to_bin(num):
    """
    Convert from decimal to signed binary.

    Args:
        num: str, represents a decimal number

    Ret:
        ret: int, represents a binary number
    """

    assert get_type(num) == "decimal", AssertionError("Not a valid decimal integer!")

    if int(num) < 0:
        ret = unsigned_dec_to_bin(num[1:])[2:]
        if ret[0] == "1": ret = "0" + ret
        return sign_flip("0b" + ret)
    else:
        ret = unsigned_dec_to_bin(num)[2:]
        return "0b0" + ret



def signed_hex_to_bin(num):
    """
    Convert from signed hexadecimal to signed binary.

    Args:
        num: str, represents a hexadecimal number

    Ret:
        ret: int, represents a binary number
    """

    assert get_type(num) == "hexadecimal", AssertionError("Not a valid hexadecimal integer!")

    CONVERT = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
             '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
             'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

    ret = "0b"    
    for digit in num[2:]:
        ret += CONVERT[digit]

    return ret



def signed_bin_to_hex(num):
    """
    Convert from signed binary to signed hexadecimal.

    Args:
        num: str, represents a binary number

    Ret:
        ret: int, represents a hexadecimal number
    """

    assert get_type(num) == "binary", AssertionError("Not a valid binary integer!")

    CONVERT = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
             '0100': '4', '0101': '5', '0110': '6', '0111': '7',
             '1000': '8', '1001': '9', '1010': 'a', '1011': 'b',
             '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    
    ret = ""

    num = num[2:]
    while len(num) > 0:
        if len(num) < 4:
            num = num[0] * (4 - len(num)) + num
            continue

        ret = CONVERT[num[-4:]] + ret
        num = num[:-4]
    
    return "0x" + ret


def signed_hex_to_dec(num):
    """
    Convert from signed hexadecimal to decimal.

    Args:
        num: str, represents a hexadecimal number

    Ret:
        ret: int, represents a decimal number
    """

    return signed_bin_to_dec(signed_hex_to_bin(num))


def signed_dec_to_hex(num):
    """
    Convert from decimal to signed hexadecimal.

    Args:
        num: str, represents a decimal number

    Ret:
        ret: int, represents a hexadecimal number
    """

    return signed_bin_to_hex(signed_dec_to_bin(num))


if __name__ == "__main__":
    pass