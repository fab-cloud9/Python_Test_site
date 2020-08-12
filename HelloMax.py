# Test code:

number = int(input("Input a number: "))

diff = number % 2 # if odd = 1, if even = 0 (no remainder)
if (diff == 1):
    print("The number " + str(number) + " is odd")
else:
    print("The number " + str(number) + " is even")


