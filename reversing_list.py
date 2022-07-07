def reversing_list(*args):
    result=args[::-1]
    return result

li=[5,2,7,1,6,9,13,31,43,34,23,11,55,23,12,11,5]

print(reversing_list(*li))
print(reversing_list(2,3,4,5,6))