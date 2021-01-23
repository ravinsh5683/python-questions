list1 = [10, 20, 30, 40, 50]
# creating sum_list function
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
sum = sumOfList(list1, len(list1))
print("Sum of all elements in given list: ", sum)