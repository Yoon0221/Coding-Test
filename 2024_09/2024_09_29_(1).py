# https://www.acmicpc.net/problem/10815


# 6시 시작


# 입력받기
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))


# 순회하기
n_set = set(n_list)  # 집합으로 변환하여 탐색 속도 개선
answer = [1 if i in n_set else 0 for i in m_list]


# 출력하기
for i in answer :
    print(i, end = " ")

