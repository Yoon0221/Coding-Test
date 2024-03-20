
# 0 0 전까지 계속 반복
first = -1
second = -1
while(1) :

    # 입력받기
    first, second = map(int, input().split())

    # 종료조건
    if first == 0 and second == 0 :
        break

    # 3가지 케이스 실행
    if second % first == 0 :
        print("factor")
        continue
    elif first % second == 0 :
        print("multiple")
        continue
    else :
        print("neither")
        continue

