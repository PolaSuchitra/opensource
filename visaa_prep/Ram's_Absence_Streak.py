N = int(input())
arr = list(map(int, input().split()))

cnt = 0
cnt1 = 0

for i in range(N):
    if arr[i] == 0:
        cnt += 1
        if i == N-1 or arr[i+1] != 0:
            cnt1 = max(cnt1, cnt)
    else:
        cnt = 0  

print(cnt1)
