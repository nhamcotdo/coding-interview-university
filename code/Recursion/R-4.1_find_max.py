def find_max(arr, n):
    def max(i):
        if i == n - 1:
            return arr[i]
        _max = max(i + 1)
        return arr[i] if arr[i] > _max else _max 
    
    return max(0)


if __name__ == "__main__":
    arr = [1,2,6,32,3,1,34,2,3,123,231,3,213,214,142,215,235,43,5,345,34,543,5,435,43,534,5,345,4]

    print(find_max(arr, len(arr)))
