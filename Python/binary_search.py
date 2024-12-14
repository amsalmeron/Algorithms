itemList = [1,2,3,4,5,6,7,8,9,10]
item = 2

def binary_search (itemList, item):
    low = 0
    high = len(itemList) - 1
    
    while (low <= high):
        mid = (low + high) // 2
        guess = itemList[mid]
        if (guess == item):
            return mid
        elif (guess > item):
            high = mid - 1
        else:
            low = mid + 1
    return None

info = binary_search(itemList, item)
print(info)