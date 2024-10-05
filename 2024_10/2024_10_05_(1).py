# https://www.acmicpc.net/problem/9012



# vps 판별 알고리즘
def IsVps(temp) :
    
    temp_len = len(temp)
    
    stack = []
    check = 0
    for i in range(0,temp_len,1) :
        if (temp[i] == '(') :
            stack.append(temp[i])
            
        else :
            if (i == 0) : return 0 # vps 가 아님
            
            else : 
                if (len(stack) == 0) : return 0 # vps 가 아님
            
                stack.pop()
                check += 1
        
    if (check*2 == temp_len) : return 1 # vps 가 맞음
    else : return 0 # vps 가 아님



# 입력받기
n = int(input())


# 수행하기
answer = []
for i in range(n) :
    temp =input()
    
    if (IsVps(temp) == 1) : # vps 가 맞으면
        answer.append("YES")
    
    else : # vps 가 아니면
        answer.append("NO")
        

# 출력하기
for i in range(0,n,1) :
    print(answer[i])

