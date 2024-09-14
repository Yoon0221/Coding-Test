# https://www.acmicpc.net/problem/5073



# 입력받기
temp = []
answer = []
while(1) :
    temp = list(map(int, input().split()))
    if (temp == [0,0,0]) : break
    
    a = temp[0]
    b = temp[1]
    c = temp[2]
    max_n = max(temp)
    rest = [i for i in temp if i != max_n]
    if (len(rest) == 0) : 
        rest.append(max_n)
        rest.append(max_n)
    elif (len(rest) == 1) :
        rest.append(max_n)
    
    if (max_n >= rest[0] + rest[1]) : answer.append("Invalid")
    elif (a == b == c) : answer.append("Equilateral")
    elif (a==b or a==c or b==c) : answer.append("Isosceles")
    else : answer.append("Scalene")
    
for i in range(0, len(answer), 1) :
    print(answer[i])

    
