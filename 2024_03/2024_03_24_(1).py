# 수 입력받고 리스트에 저장하기
num_list = []
sum = 0
for i in range(5) :
    now = int(input())
    sum += now
    num_list.append(now)

# 평균 출력하기
print(int(sum/5))

# 리스트 정렬하기
num_list.sort()

# 중앙값 출력하기
print(num_list[2])
