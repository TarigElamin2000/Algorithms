# mearge sort has tow functions that can be used one is Divied and then mearge which mearge the arrays and sort them 

# Time Complexity : O(nlogn)
# Speaces Complexity : O(n)

def sort(leftArr, rightArr):
    leftPointer = 0
    rightPointer = 0
    result = []
    while leftPointer < len(leftArr) and rightPointer < len(rightArr):
        if leftArr[leftPointer] < rightArr[rightPointer]:
            result.append(leftArr[leftPointer])
            leftPointer += 1
        else:
            result.append(rightArr[rightPointer])
            rightPointer += 1

    if leftPointer < len(leftArr):
        result += leftArr[leftPointer:]
    else:
        result += rightArr[rightPointer:]

    return result

def mearge(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    left = mearge(arr[m:])
    right = mearge(arr[:m])
    return sort(left,right)


example_one = [3,4,6,2,3,7,2]
print(mearge(example_one))