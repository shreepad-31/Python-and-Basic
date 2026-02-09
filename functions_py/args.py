#  Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    return sum(args)
total = (1,2,3,4,7,55,0,6)
print(sum_all(total))