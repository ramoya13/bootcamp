#code to implement a binary
#search
#it returns location in a given array arr
#if present, else returns -1

def findvalue(arr,low,high,n):
    

    while low<= high:
        mid= (low+high)//2

        #Check if n is present at mid
        if arr[mid]==n:
            return mid
        #if n is greater, ignore left half
        elif arr [mid]<n:
            return findvalue(arr,mid+1, high, n)
        #if n is smaller, ignore right half
        else:
            return findvalue(arr, mid-1, high, n)

        #if we reach here then the element was not present
    else:
            return -1 
#test array
arr=[7,9,14,22,34]
n=8
#function call
final = findvalue(arr,0,len(arr)-1,n)

if final !=-1:
    print("Element is present at index", str(final))
else:
    print("Element is not present")
