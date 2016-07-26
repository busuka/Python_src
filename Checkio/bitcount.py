x = "10 2"
v = list(map(int,x.split()))
n = v[0]
m = v[1]
cnt = 0
for x in range(0,n+1):
    tmp = bin(x)
    oneCnt = str(tmp).count("1")
    if oneCnt == m:
        cnt += 1

print(cnt)
