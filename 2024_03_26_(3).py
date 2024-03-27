# 입력받기
n,k = map(int, input().split())
num_list = list(map(int, input().split()))


# 역순정렬
num_list.sort(reverse = True)


# 커트라인 찾아서 출력하기
print(num_list[k-1])
