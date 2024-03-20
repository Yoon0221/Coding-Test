
# 입력받기
T = int(input())

C = [0] * T
for i in range(T) :
    C[i] = int(input())

    
# 테스트의 갯수만큼 for문 실행 & answer에 답 저장
answer = [[0] * 4 for i in range(T)] # 리스트 컴프리헨션으로 2차원 배열 생성
for i in range(T) :

    # 현재 거슬러줘야할 돈이 0이 될 때까지 반복문 수행
    num_Q, num_D, num_N, num_P = 0,0,0,0
    now = C[i]
    while(1) :

        if now // 25 > 0 :
            num_Q += 1
            now -= 25
            continue

        elif now // 10 > 0 :
            num_D += 1
            now -= 10
            continue

        elif now // 5 > 0 :
            num_N += 1
            now -= 5
            continue

        else :
            num_P = now
            now -= now

        if now == 0 :
            break

    answer[i][0] = num_Q
    answer[i][1] = num_D
    answer[i][2] = num_N
    answer[i][3] = num_P


# 형식에 맞게 결과 출력
for i in range(T) :
    for k in range(4) :
        print(answer[i][k], end=" ")
    print()
    
