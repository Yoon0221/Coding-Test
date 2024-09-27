# https://www.acmicpc.net/problem/2231


# 입력받기
n = int(input())


# 뺄 수 있는 가장 큰 수 : 모든 자리가 9 / 뺄 수 있는 가장 작은 수 : 1
str_n = str(n)
max = len(str_n) * 9
min = 1


# 수행하기
answer = 0
for i in range(max, min, -1) :
    
    temp = n - i # 임시 생성자
    
    if(temp<0) : temp *= -1
    
    str_temp = str(temp)
    
    cnt = 0
    for k in range(0,len(str_temp),1) :
        cnt += int(str_temp[k])
        
    if (cnt+temp == n) :
        answer = temp
        break
    
    
print(answer)
    

            