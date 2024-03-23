# 입력받기
a,b,c = map(int,input().split())

answer = a+b+c
# 삼각형의 조건 확인 -> 두 변의 길이 합이 나머지 한 변의 길이보다 커야한다.
while(1) :

    check = 0
    c1,c2,c3 = 0,0,0

    if a+b > c :
        check += 1
    else :
        c = a+b-1  # c가 너무 큰 경우
        
    if a+c > b :
        check += 1
    else :
        b = a+c-1  # b가 너무 큰 경우
        
    if b+c > a :
        check += 1
    else :
        a = b+c-1  # a가 너무 큰 경우


    # 종료 조건 : 모든 쌍이 ok이면 종료
    if check == 3 :
        answer = a+b+c
        break

print(answer)
