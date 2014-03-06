#You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
#For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).


def checkio(number):
    list1= list(str(number))
    list1= map(int, list1)
    new_list = [x for x in list1 if x != 0]
    sum = 1
    for item in new_list:
       sum *= item
    return sum
        
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
