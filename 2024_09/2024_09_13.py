# https://www.acmicpc.net/problem/1978



# 소수 판별 함수 (제곱근까지만 확인)
import math
def isDecimal(num) :
    
    if (num == 1) : # 예외 : 1은 소수가 아님
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
num = int(input())
num_list = list(map(int, input().split()))


# 함수 호출
answer = 0
for i in range(0, num, 1) :
    if (isDecimal(num_list[i]) == 0) : #소수이면
        answer += 1
        

# 정답
print(answer)

