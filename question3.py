def countX(list, x):
    count = 0
    for ele in list:
        if (ele == x):
            count = count + 1
    return count


# Driver Code
list=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
x = 1
print('{} has occurred {} times'.format(x, countX(list, x)))