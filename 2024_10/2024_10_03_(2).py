# https://www.acmicpc.net/problem/14425



# 입력받기
n, m = map(int,input().split())
check_set = set([input() for i in range(n)])

cnt = 0
for i in range(m) :
    temp = input()
    if (temp in check_set) :
        cnt += 1
        
print(cnt)
