# 입력받기
n,k = map(int,input().split())

# 작은 순서대로 약수인지 판별, k번째이면 반복문 탈출
num = 0
answer = 0
for i in range(1,n+1,1) :
    if n%i == 0 :
        num += 1

    if num == k :
        answer = i
        break

# 결과 출력
print(answer)
