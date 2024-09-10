N = int(input())

# 배열에 순서대로 입력받기
num_list = []
for i in range(N) :
    num_list.append(int(input()))

# 오름차순 정렬
num_list.sort()

# 결과 출력
for i in range(N) :
    print(num_list[i])
