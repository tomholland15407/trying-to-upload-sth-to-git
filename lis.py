def lis(arr,i,memo={}):
    if i==0:
        memo[0]=1
    if i not in memo:
        prev=[lis(arr,j, memo) for j in range(i) if arr(j)>arr(i)]
