#"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.
#You should write a function that will receive a positive integer and return:
#"Fizz Buzz" if the number is divisible by 3 and by 5;
#"Fizz" if the number is divisible by 3;
#"Buzz" if the number is divisible by 5; 
#The number as a string for other cases.


def checkio(number):
    if (number % 3 == 0 and number % 5 == 0):
        message= ("Fizz Buzz")
    elif number % 3 == 0:
        message= ("Fizz")
    elif number % 5 == 0:
        message= ("Buzz")
    else:
        message= "%s" %(number)
    return message
    