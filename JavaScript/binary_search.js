let item_list = [1,2,3,4,5,6,7,8,9]
item = 8

function binary_search (list, item) {
    low = 0;
    high = item_list.length - 1;
    while (low <= high) {
        mid = Math.floor((high + low) / 2);
        guess = item_list[mid];
        if (guess == item) {
            return mid;
        } else if (item < guess){
            high = mid - 1;
        } else {
            low = mid + 1
        }
    }
    return null;
}

info = binary_search(item_list, item);
console.log(info);