N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]
arr1=[[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
for i in arr1:
    print(' '.join(map(str,i)))
