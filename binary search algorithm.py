def bin(l,item):
    ls.sort()
    low = 0
    high = len(l) - 1
    while item in l:
        mid = (low + high) // 2
        if item == l[mid]:
            return mid
        elif item < l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "item is not found"

ls = [1,2,33,24,56,78,9,10,12,44,19,20,22]
print(ls)
print(bin(ls,56))





