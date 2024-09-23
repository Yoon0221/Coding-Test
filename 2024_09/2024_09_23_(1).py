# https://www.acmicpc.net/problem/1934


# 두 수의 최소공배수를 출력하는 알고리즘
import math
def LCM(a,b) :
    print(math.lcm(a,b))


# 입력받기
T = int(input())
a_list, b_list = [], []
for i in range(T) :
    temp_a_list, temp_b_list = map(int, input().split())
    a_list.append(temp_a_list)
    b_list.append(temp_b_list)


# 수행하기
for i in range(0,T,1) :
    LCM(a_list[i], b_list[i])