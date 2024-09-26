tup = ([7,8], [9,1], [10, 7])
print("The original tuple is : " + str(tup))
res = sum(list(map(sum, list(tup))))
print("The summation of tuple elements are : " + str(res))
