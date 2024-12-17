def quicksort(arr):
    if (len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        # less = []
        # for i in arr[1:]:
        #     if i > pivot:
        #         less.append(i)
        less = [i for i in arr[1:] if i <= pivot]
        
        # greater = []
        # for i in arr[1:]:
        #     if i > pivot:
        #         greater.append(i)
        greater = [i for i in arr[1:] if i > pivot]
        
        
        return quicksort(less) + [pivot] + quicksort(greater)
    
# Driver Code (execution trigger)
if __name__ == "__main__":
    print(quicksort([11,9,20,5,7]))