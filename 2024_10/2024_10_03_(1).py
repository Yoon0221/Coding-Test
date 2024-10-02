# https://www.acmicpc.net/problem/2581



# 소수 판별 알고리즘 (아~~의 체) -> 0은 소수, 1은 소수가 아님
import math
def isDecimal (x) :
    
    if (x == 1) : # 1이면 소수가 아님
        return 1
    
    if (x == 2) : # 2이면 소수임
        return 0
    
    if (x == 3) : # 3이면 소수임
        return 0
    
    if (x == 5) : # 5이면 소수임
        return 0
    
    if (x%2 == 0) : # 2가 아닌 짝수이면 소수가 아님
        return 1
    
    # 3부터 자기 자신의 1/3 까지 (올림)
    end = math.ceil(x/3)
    for k in range(3, end+1, 1) :
        if (math.ceil(x/k) == math.floor(x/k)) :
            return 1
    
    return 0
        


# 입력받기
m = int(input())
n = int(input())


# 수행하기
sum = 0
min = n+1
for i in range(m, n+1, 1) :
    if(isDecimal(i) == 0) : # i가 소수이면 
        sum += i
        
        if (i < min) : # 현재 i가 최소이면
            min = i
            

# 결과 출력하기  
if (sum == 0) : print("-1")
else :
    print(sum)
    print(min)
         