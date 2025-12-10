def lis(arr, i, d):
    print('step0', arr, i ,d)
    if i in d:
        print('step1', i, d[i])
        return d[i]
    else:
        res = 1
        for j in range(0, i):
            if arr[i] > arr[j]:
                print('step2', arr[i], arr[j])
                res = max(res,1+lis(arr,j,d))
        d[i] = res
        print('step3', i, d[i])
        return res

def lis_ans(arr):
    ans = 0
    d = {0:1}
    for i in range(len(arr)):
        ans = max(ans, lis(arr, i, d))
        print(ans)
    return ans
print('the number of elements in the longest increasing subsequence is: ', lis_ans([1,2,0]))
