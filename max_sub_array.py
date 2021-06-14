
arr = []
n = 0

def max_sub_array(arr):
    max = -99999999999999
    for i in range(n):
        # max_sub_array_i
        for j in range(i, -1, -1): 
            sum = 0
            for k in range(i, j - 1, -1):
                sum += arr[k]
            if max < sum:
                max = sum
    return max

if __name__ == "__main__":
    # input 
    n = int(input())
    for i in range(n):
        element = int(input())
        arr.append(element)
    print (arr)
    # computing
    result = max_sub_array(arr)
    
    # output
    print (result)
    
    
