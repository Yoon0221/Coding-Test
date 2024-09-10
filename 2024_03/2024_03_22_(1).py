while(1) :

    now = int(input())

    # 종료 조건 : -1을 만나면 반복문 탈출
    if now == -1 :
        break

    # 모든 약수들을 더해서 plus에 저장 & plus_list에 저장
    plus = 0
    plus_list = []
    for i in range(1,now,1) :
        
        # 약수이면
        if now%i == 0:
            plus += i
            plus_list.append(i)

    # 완전수이면
    if now == plus :
        print(f"{now} =", end = "")
        for k in range(len(plus_list)) :
            print(" ", end="")
            print(plus_list[k], end="")

            if k != len(plus_list) - 1 :
                print(" +", end ="")
            else :
                print("")

    else :
        print(f"{now} is NOT perfect.")
