# This is the real Master file
# Here there are changes made

F_Num = 1  # value of Fibonacci number
F_old_1 = 0  # latest old value of stored
F_old_2 = 0  # oldest value of stored
N = 3  # order of Fibonacci number
i = 0

while i < N:

    if N == 1:
        print(F_Num)
        F_Num = F_old_1
    else:
        F_old_2 = F_old_1
        F_old_1 = F_Num
        F_Num = F_old_1 + F_old_2
    i += 1
print(F_Num)
if N <= 0:
    print("Can only apply positive integers")