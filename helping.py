import math


def binary(test_str="ARNAB"):

    res = ''
    for i in test_str:
        if(ord(i) > 255):
            continue
        s = ''.join(format(ord(i), 'b'))
        delta = "00000000"+s
        gamma = delta[-8:]
        res += (gamma)
    return(res)


def debinary(test_str="0100000101010010010011100100000101000010"):

    res = ''
    for i in range(int(len(test_str)/8)):
        bin = test_str[8*i:8*(i+1)]
        res += chr((int(bin, 2)))

    return(res)


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def decimalToBinarystring(n):
    res = ''
    for i in range(23, -1, -1):
        k = n >> i
        if (k & 1):
            res += "1"
        else:
            res += "0"
    return res


def change_val(image_sequence=None, x=0, y=0, channel=0, ch=0):
    val = image_sequence[y][x][channel]
    lsb = val & 1
    
    if(ch == '1'):
        if(lsb != 1):
            image_sequence[y][x][channel] += 1
    if(ch == '0'):
        if(lsb == 1):
            image_sequence[y][x][channel] -= 1
    return(image_sequence)


def BinaryStringtoDecimal(test_str="10101010"):
    length = len(test_str)
    final_val = 0
    for i in range(1, length+1):
        val = int(test_str[-i])
        final_val = final_val+(val*int(math.pow(2, i-1)))
    return(final_val)

