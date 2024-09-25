# 스택 알고리즘 공부 후 문제풀이!!

# 시간 체크 : 시작 (12시 26분) ~

# https://www.acmicpc.net/problem/9012



# 입력받기
t = int(input())

answer = [0 for i in range(t)]
stack = []
for k in range(t) :
    
    temp = input()
    for i in range(0, len(temp), 1) :
        
        if (temp[i] == '(') : # 열림
            stack.append(temp[i])
            answer[k] = "NO"
            
        else : # 닫힘 -> 항상 바로 앞의 것과 함께 나가야함. 처음에는 들어올 수 없음.
            if (len(stack) == 0) :
                answer[k] = "NO"
                break
            else : 
                stack.pop()
                if (len(stack) == 0) : answer[k] = "YES"
                else : answer[k] = "NO"
            
# 출력하기
print(answer)
           
    