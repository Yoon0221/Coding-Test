# https://www.acmicpc.net/problem/24264



# 알고리즘 
def MenOfPassio(n) :
    sum = 0
    check = 0
    for i in range(1,n+1,1) :
        for k in range(1,n+1,1) :
            # 코드 1
            # sum += A[i] * A[k]  
            check += 1 
    return check


# 입력받기 
n = int(input())

# 수행하기
print(n*n)
print("2")