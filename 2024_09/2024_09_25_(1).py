# 스택 알고리즘 공부 후 문제풀이!!

# https://www.acmicpc.net/problem/28278



# 입력받기 & 스택 연산
n = int(input())

stack = []
answer = []
for i in range(n) :
    
    temp = str(input())
    if (temp[0] == '1' and temp[1] == ' ') : # 1이 나왔을때
        
        x, y = map(int, temp.split())
        stack.append(y) # 1번
    
    elif (temp[0] == '2') : # 2가 나왔을때
        
        if (len(stack) != 0) : answer.append(stack.pop()) # 2번 
        else : answer.append(-1) 
        
    elif (temp[0] == '3') : # 3이 나왔을때
        
        answer.append(len(stack)) # 3번
        
    elif (temp[0] == '4') : # 4가 나왔을때
        
        if (len(stack) == 0) : answer.append(1) # 4번 
        else : answer.append(0) 
        
    else : # 5가 나왔을때
        
        if (len(stack) != 0) : answer.append(stack[-1]) # 5번 
        else : answer.append(-1) 
        
        
    
# 출력하기
for i in range(0,len(answer),1) :
     print(answer[i])
