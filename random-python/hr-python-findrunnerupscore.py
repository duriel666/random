if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]
    arr.sort()
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < arr[len(arr)-1]:
            print(arr[i])
            break
