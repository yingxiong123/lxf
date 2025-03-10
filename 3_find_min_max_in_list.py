def findMinAndMax(mylist):
    if not mylist:
        return tuple()
    
    min_val = max_val = mylist[0]

    for num in mylist:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val,max_val)
        
mylist = [10,5,58,9]

result = findMinAndMax(mylist)
print(result)
