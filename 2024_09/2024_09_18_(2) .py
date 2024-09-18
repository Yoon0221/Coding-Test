# https://www.acmicpc.net/problem/24265



# 알고리즘 
def MenOfPassion(n) :
    sum = 0
    check = 0
    for i in range(1,n,1) :
        check += n-i
            
    return check


# 입력받기
n = int(input())


# 수행하기
print(MenOfPassion(n))
print("2")

