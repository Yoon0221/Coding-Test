# 입력받기
num = int(input())


num_list = []
while(1) :
    
    # 종료조건
    if num == 1 :
        break

    # 현재 값을 나누어 떨어지게하는 i를 리스트에 저장
    for i in range(2,num+1,1) :
        if num % i == 0 :
            num_list.append(i)
            num = num//i
            break


# 결과 출력하기
for i in range(len(num_list)) :
    print(num_list[i])
