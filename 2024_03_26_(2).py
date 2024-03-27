# 입력받기
ori = int(input())
num = ori - 1


cnt = 0
while(1) :

    # 종료조건
    if num <= 0 :
        break
    
    cnt += 1
    num -= cnt*6


# 결과 출력
if ori == 1 :
    print('1')
else :
    print(cnt + 1)
