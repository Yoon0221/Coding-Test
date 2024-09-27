# https://www.acmicpc.net/problem/2798


# 입력받기
n, m = map(int, input().split())
num_list = list(map(int, input().split()))


# 수행하기
max = 0
for i in range(n) :
    for k in range(n) :
        for j in range(n) :
            
            if (i < k < j) : 
                temp = num_list[i]+num_list[k]+num_list[j]
                
                if (temp >= max and temp <= m) :
                    max = temp
                    
print(max)
    
            