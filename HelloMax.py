# ----------- Code 1: Sort a list of numbers -------
# 1 Get the list of numbers
# 2. Sort them in ascending order
# 3. display old and new sorting

start_list = [55, 3, 16, 77, 5]
sort_list = []
element = 0
number = 0

# Fill up the list of numbers
start_list = []
n = int(input("Enter number of elements : "))

# Iterating till the range
for i in range(0, n):
    x = int(input())
    start_list.append(x)  # add element x

print(start_list)
lowest = start_list[0]

# For the whole list until it is empty
while len(start_list) > 0:
    number = start_list[element]
# Find the lowest number in list and place first
    if number < lowest:
        lowest = start_list[element]
    element += 1
# Determine if whole list have been walked through, remove/add lowest number to sorted list
    if element == len(start_list):
        sort_list.append(lowest)
        start_list.remove(lowest)
# As long as there is a list to pick from
        if len(start_list) > 0:
            lowest = start_list[0]
        element = 0

print(sort_list)
