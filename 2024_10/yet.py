# https://www.acmicpc.net/problem/4949


# 시간 체크 
# 시작 : 09시 08분



# 문장 체크 알고리즘
def IsBalenceing(temp) :
    
    stack_big = []
    stack_small = []
    stack_sequence = []
    num_big = 0
    num_small = 0
    check_big = 0
    check_small = 0

    temp_len = len(temp)
    
    for i in range(0, temp_len, 1) :
        if (temp[i] == '[') :
            stack_big.append(temp[i])
            check_big += 1
            stack_sequence.append('[')
            
        elif (temp[i] == ']') :
            if (len(stack_big) == 0) : return 1
            
            if (stack_sequence.peek() != 0) : return 1 
            
            stack_big.pop()
            num_big += 1
            
        if (temp[i] == '(') :
            stack_small.append(temp[i])
            check_small += 1
            stack_sequence.append('(')
            
        elif (temp[i] == ')') :
            if (len(stack_small) == 0) : return 1
            
            if (stack_sequence != 1) : return 1 
            
            stack_small.pop()
            num_small += 1
    
    if ((check_big*2 == num_big*2) and (check_small*2 == num_small*2)) : return 0
    else : return 1
    


answer = []
# 입력받기
while(1) :
    
    temp = input()
    
    # 종료조건
    if (temp == ".") : 
        break
    
    # 수행하기
    if (IsBalenceing(temp) == 0) : # 균형 있는 문장이면
        answer.append("yes")
    else : # 균형 없는 문장이면
        answer.append("no")
        

# 출력하기
for i in range(0, len(answer), 1) :
    print(answer[i])
    
    

