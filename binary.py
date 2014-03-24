You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1) are in it.

def checkio(number):
    number= bin(number)
    return number.count('1')
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9