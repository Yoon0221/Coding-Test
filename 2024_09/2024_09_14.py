# https://www.acmicpc.net/problem/2581                     **** 진행중



# 소수 판별 함수 (제곱근까지만 확인)
import math
def isDecimal(num) :
    
    if (num == 1) : # 예외 : 1은 소수가 아님
        return 1
    
    if (math.ceil(math.sqrt(num)) == math.sqrt(num)) : # 제곱근이 정수이면 소수가 아님
        return 1
    
    if (num%2 == 0 and num != 2) : # 2가 아닌 짝수는 소수가 아님
        return 1
    
    num_list = [i for i in range(2, num)] # 1과 자기자신 제외
    
    check_num = 0
    while(len(num_list) != 0) :
        
        now_use = num_list[0]  # 현재 숫자
        
        if (now_use > math.sqrt(num)) : # 제곱근까지만 확인
            return check_num
        
        if (num%now_use == 0) :
            check_num = 1
            return check_num
            
        use_list = [x for x in range(now_use, num) if(x%now_use == 0)] # 현재 숫자의 배수들
        num_list = [num_list[y] for y in range(0, len(num_list), 1) if (num_list[y] not in use_list)]
        
    return check_num


# 입력받기
m = int(input())
n = int(input())


# 소수 중 최소, 최대 구하기
min = n
max = m
all = 0
for i in range(m, n+1, 1) :
    
    if (isDecimal(i) == 0) : # 소수이면
        
        if (min >= i) : # 최소이면
            min = i
            
        if (max <= i) : # 최대이면
            max = i
            
        all += i
            
        
if (min == n and max == m) : # 소수가 없을 경우
    print("-1")
else :
    print(all)
    print(min)
            
            