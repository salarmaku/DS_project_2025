arr = [1, 2, 3, 4, 5]
index = 2
def delete(arr, index):
    if index < 0 or index > len(arr):
        return None
    else:
        obj = arr[index]
        arr[index] = 0
        return obj

delete(arr , 2)
print(arr)
