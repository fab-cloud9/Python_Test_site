# This is the real Master file

N = int(input("Which order of Fibonacci number are you interested in: ")) - 1  # order Fibonacci starts with 0th order
answer = input("In what way do you want to find your Fibonacci Number, While Loop = w, For Loop = f or Recursice = r: ")

if N <= 0:
    print("ERROR: You must enter a positive integer")
elif answer == "w":
    # ------------------ WHILE LOOP (ITERATIVE) Version -----------------------------------------
    # Create a While Loop
    # Iterate through the N
    # Fibonacci Numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.....]
    # Fib_(N) = Fib_(N-1) + Fib_(N-2)
    # Print the response to the Nth number

    F_old_1 = 1  # latest old value of stored
    F_old_2 = 0  # oldest value of stored
    i = 0  # iterations

    while i < (N - 1):

        if N == 1:  # print the result of the 1st Fibonacci Number
            F_Num = F_old_1
        else:
            F_Num = F_old_1 + F_old_2  # Calculate the upcoming value for next iteration
            F_old_2 = F_old_1
            F_old_1 = F_Num
        i += 1
    if N == 0:  # The first Fibonacci Number is already defined
        F_Num = F_old_2
        print(F_Num)

    elif N == 1:  # The second Fibonacci Number is already defined
        F_Num = F_old_1
        print(F_Num)
    else:
        # F_Num = F_New
        print(F_Num)

elif answer == "f":
    # -------------- FOR LOOP (ITERATIVE) Version ---------------------------------------------
    # Create a function with input N
    # Iterate through the N
    # Fibonacci Numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,.....]
    # Fib_(N) = Fib_(N-1) + Fib_(N-2)
    # Print the response to the Nth number

    def getfib(n):

        fib_old_2 = 0  # 1st initial oldest value of stored Fibonacci Number
        fib_old_1 = 1  # 2nd initial latest old value of stored Fibonacci Number
        fib_for = 1  # 3rd initial fib number 2

        for number in list(range(n - 2)):  # 3 initial variables --> if N <= 2 use initial variables without iteration
            fib_old_2 = fib_old_1
            fib_old_1 = fib_for
            fib_for = fib_old_1 + fib_old_2
        if n == 0:
            return fib_old_2
        elif n == 1:
            return fib_old_1
        else:
            return fib_for


    print(getfib(N))

else:
    # ---------------------------- RECURSIVE Version ------------------------------------------------------------
    #  Create a function that has correct conditions
    #  The recursive function will go down to the bottom (nn = 0) of the fibo_rec-tree
    #  and find initial values fibo:old_2 & fibo_old_1
    #  Then work its' way up the tree to the top

    fibo_old_2 = 0  # 1st initial oldest value of stored Fibonacci Number
    fibo_old_1 = 1  # 2nd initial latest old value of stored Fibonacci Number


    def fibo_rec(nn):

        if nn == 0:
            return fibo_old_2
        elif nn == 1:
            return fibo_old_1
        else:
            return fibo_rec(nn - 1) + fibo_rec(nn - 2)


    print(fibo_rec(N))
