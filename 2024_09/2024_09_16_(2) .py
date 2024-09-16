# https://www.acmicpc.net/problem/24263



# 알고리즘 
def MenOfPassion (n) :
    sum = 0
    check = 0

    for i in range(1,n+1,1) :
        sum += i # 코드 1
        check += 1 # 시간복잡도 체크
        
    return check


# 입력받기
n = int(input())


# 수행
print(MenOfPassion(n))
print("1") # n