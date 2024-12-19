## Exercises from Grokkiing Algorithms

### Chapter 1 Introduction

1.1 Suppose you have a list of 128 items, what is is maximun number of steps it would take using binary search? 
    7

1.2 If you double this list to 256, what is the maximum number of steps?
    8

Give the runtime for the following scenarios in Big O notation
1.3 You have a name and want to find the persons phone number
    O(log n)

1.4 You have a phone number and want to find a persons name
    O(n)

1.5 You want to read the numbers of every person in the book
    O(n)

1.6 You want to read the numbers of just the A's
    O(n)

### Chapter 2 Selection Sort

2.1 If you are building an app to track your finances (lots of inserts with few reads), should you use an array or list?
    Linked List: Arrays have fast reads with slow inserts, so because we will mainly be inserting the Linked list is best. Also, when reading we will read all inserts which is the same operations as an array.

2.2 If you are builing an app for a restaurant to insert orders by teh server and remove orders by the chef once they are made, would you use an array or linked list?
    Linked List

2.3 To find if a username is valid for Facebook using binary search, would you implement the usernames using an array or linked list?
    Array: Specifically, a sorted Array

2.4 What are the downsides for array inserts when using it as a database of usernames that need to be sorted?
    It causes O(n) operations with each insertion: Array insertion is slow, plus it would need to be sorted every insertion if binary search is neccesary.

2.5 Suppose a hybrid stlye, an array of linked lists, would this be quick or slower for search and inserting?
    For searching it would be slower than an array, and inserting it would be slightly faster or the same as a linked list. 

## Chapter 3 Recursion

3.1 How to define the stack (bottom to top): 
    greet2(name)
    name = maggie
    greet(name)
    name = maggie

    Greet function is called with name = maggie, but is suspended because 
    greet2 fucntion is called withi greet function with the same variable 
    name = maggie

3.2 What happens to the stack when a recursive function runs forever?
    The stack continues to grow until the program errors out due to a stack overflow

## Chapter 4 Quicksort

4.1 Write out the sum function:
    def sum(a,b):
        return a + b

4.2 Write a recursive function to count the number of items on a list
    def count_items(list, count):
        count = 0
        if (list.pop())
            count + 1
            count = count_items(list.pop, count)
        return count
        
4.3 Find the maximum number in a list