# https://www.acmicpc.net/problem/24267




# 알고리즘 
def MenOfPassion(n) :
    sum = 0
    for i in range(1, n-1, 1) :
        for j in range(1+i, n, 1) :
            sum += n-j

    return sum



 # 입력받기
n = int(input())


# 수행하기
print(MenOfPassion(n))
print("3")