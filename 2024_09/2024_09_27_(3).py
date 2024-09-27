# https://www.acmicpc.net/problem/1018


# 입력받기
n, m = map(int, input().split())
map_list = [list(map(str, input().rstrip())) for i in range(n)]


# 알고리즘 - 현 위치에서 칠해야하는 체크판 수 반환
def how_many_in_here(x,y,first) :
  
    cnt = 0
    for i in range(x,x+8,1) :
        for k in range(y,y+8,1) :
        
            now = (i-x) + (k-y) # 떨어진 거리
        
            # 같아야 하는 곳 : 짝수번 움직인 곳
            if (now % 2 == 0) :
                if (map_list[i][k] == first) :
                    pass
                else :
                    cnt += 1
        
            # 달라야 하는 곳 : 홀수번 움직인 곳
            else :
                if (map_list[i][k] != first) :
                    pass
                else :
                    cnt += 1
                    
    return cnt
                

# 수행하기 - 가능한 모든 값을 모서리(왼쪽 상단)로 제시후 min 값 구하기
answer = 65
for i in range(0,n-7,1) :
    for k in range(0,m-7,1) :
        
        temp_1 = how_many_in_here(i,k,'W')
        temp_2 = how_many_in_here(i,k,'B')
        
        if (answer >= temp_1) :
            answer = temp_1
        
        if (answer >= temp_2) :
            answer = temp_2
            
        if (answer == 0) : break
        
        
# 정답 출력하기
print(answer)
            