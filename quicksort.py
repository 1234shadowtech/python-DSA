def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
a = [3, 6, 8, 10, 1, 2, 1]
print("Original array:", a)
sorted_arr = quick_sort(a)
print("Sorted array:", sorted_arr)
#explation
#consider a list l=[5,4,3,2,1]
#step 1 pivot =3
#left=[2,1]
#middle=[3]
#right=[5,4]

#step2 using recursion
#quick_sort([2,1]) -> [1,2]
#similarly
#quick_sort([5,4]) -> [4,5]
 #returns [1]+[2]+[3]+[4]+[5]
 #=[1,2,3,4,5]