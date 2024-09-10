# https://www.acmicpc.net/problem/2563


# 한 색종이에 의해 색칠되는 모든 좌표들 반환
def check_all (x, y, num) :
    check_list = []
    n_x, n_y = 0,0
    for i in range (1, num) :
        n_x = x+i
        for k in range (1, num) :
            n_y = y+k
            if (n_x >= 0 and n_y >= 0 and n_x <= 100 and n_y <= 100) : check_list.append((n_x,n_y))
    
    return check_list
        
            

n = int(input())  # n을 입력받음
spot_list = []
for _ in range(n):
    x, y = map(int, input().split())  # 각 좌표 쌍을 입력받음
    spot_list.append(x)  
    spot_list.append(y)
paper = 10


# 색종이가 포함된 좌표를 기억 -> 겹치는 부분을 모음
check_list = []
un_list = []
all_list = []
answer = 0

for i in range(0, len(spot_list), 2): # 2개씩 나누어 진행
    check_list = check_all(spot_list[i], spot_list[i + 1], paper+1) # 현재 색종이가 있는 영역
    
    for k in check_list :
        if k not in all_list :
            all_list.append(k)
        else :
            un_list.append(k)
            answer += 1
    

print(n*100 - answer)
