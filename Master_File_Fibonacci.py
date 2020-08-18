# This is the real Master file


# ------------------ WHILE LOOP (ITERATIVE) Version -----------------------------------------
# Create a While Loop
# Iterate through the N
# Fibonacci Numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.....]
# Fib_(N) = Fib_(N-1) + Fib_(N-2)
# Print the response to the Nth number

# F_New = 1  # new value of Fibonacci number
# F_old_1 = 1  # latest old value of stored
# F_old_2 = 0  # oldest value of stored
# N = 5  # order of Fibonacci number
# i = 0  # iterations
#
# while i < (N-2):
#     i += 1
#     if N == 1: # print the result of the 1st Fibonacci Number
#         F_New = F_old_1
#     else:
#         F_old_2 = F_old_1
#         F_old_1 = F_New
#         F_New = F_old_1 + F_old_2 # Calculate the upcoming value for next iteration
#
#
# if N <= 0:
#     print("Can only apply positive integers")
# elif N == 1: # The Nth number is the latest old value
#     F_Num = F_old_2
#     print(F_Num)
# else:
#     F_Num = F_old_1
#     print(F_Num)

# -------------- FOR LOOP (ITERATIVE) Version ---------------------------------------------
# Create a function with input N
# Iterate through the N
# Fibonacci Numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.....]
# Fib_(N) = Fib_(N-1) + Fib_(N-2)
# Print the response to the Nth number


# def getfib(n):
#
#     fib_old_2 = 0  # 1st initial oldest value of stored Fibonacci Number
#     fib_old_1 = 1  # 2nd initial latest old value of stored Fibonacci Number
#     fib_for = 1    # 3rd initial fib number 2
#
#     for number in list(range(n-3)):  # 3 initial variables --> if N <= 3 use initial variables without iteration
#         fib_old_2 = fib_old_1
#         fib_old_1 = fib_for
#         fib_for = fib_old_1 + fib_old_2
#     if n == 1:
#         return fib_old_2
#     elif n == 2:
#         return fib_old_1
#     else:
#         return fib_for
#
#
# print(getfib(N))


# ---------------------------- RECURSIVE Version ------------------------------------------------------------

#  Create a function that has correct conditions
N = 4
def getFibboNumb(nn, fibbo_rec):
    fibbo_old_2 = 0  # 1st initial oldest value of stored Fibonacci Number
    fibbo_old_1 = 1  # 2nd initial latest old value of stored Fibonacci Number


    if nn == 1:
        return fibbo_old_2
    elif nn == 2:
        return fibbo_old_1
    else:
        return getFibboNumb(nn-1, fibbo_rec + fibbo_old_1 + fibbo_old_2)
        fibbo_old_2 = fibbo_old_1
        fibbo_old_1 = fibbo_rec

print(getFibboNumb(N,0))