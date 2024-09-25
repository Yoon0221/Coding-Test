# 스택 알고리즘 공부 후 문제풀이!!

# 시간 체크 : 시작 (12시 19분) ~ 끝 (12시 25분) : 6분 

# https://www.acmicpc.net/problem/10773



# 입력받기
k = int(input())

stack = []
answer = 0
for i in range(k) :
    
    # 0은 삭제단축키 (보장됨)
    temp = int(input())
    if temp == 0 :
        delete = stack.pop()
        answer -= delete
    else :
        stack.append(temp)
        answer += temp
        
# 수행하기
print(answer)