# https://www.acmicpc.net/problem/9063


# 입력받기
num = int(input())
x_list = []
y_list = []
for i in range(num) :
    temp = list(map(int,input().split()))
    x_list.append(temp[0])
    y_list.append(temp[1])
    

# 가로 (가장 왼쪽 ~ 가장 오른쪽)
line_1 = max(x_list) - min(x_list)

# 세로 (가장 밑 ~ 가장 위)
line_2 = max(y_list) - min(y_list)


print(line_1 * line_2)
