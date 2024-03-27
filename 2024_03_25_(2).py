# 입력받기
n = int(input())


# n번째의 k를 찾을 때까지 반복문 수행
before_k = 2
check = 0
while(1) :

    # 종료 조건
    if check == n :
        break

    now_k = before_k * 2 -1
    before_k = now_k
    check += 1


# 결과 출력 : k의 제곱
print(now_k **2)
