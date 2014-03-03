#Let's teach the Robots to distinguish words and numbers.
#You are given a string with words and numbers separated by whitespaces (one space). 
#The words contains only letters. You should check is the string contains three words in succession.
def checkio(words):
# words = sentence to check
    words = words.split()
    count = 0
    for x in words:
        if x.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

