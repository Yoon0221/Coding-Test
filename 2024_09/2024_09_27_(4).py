# https://www.acmicpc.net/problem/19532


# 브론즈 2문제! 5분안에 풀기 목표!! 
# 시작 시간 : 11시 41분 -> 11시 57분 종료
# 16분 걸림...ㅋ


a,b,c,d,e,f = map(int, input().split()) 

if (a == 0) :
    y = c/b # a,b 동시에 0은 불가능
    x = (f - (e*y)) / d # a,d 동시에 0은 불가능
    
else :    
    y = ((d*c) - (f*a)) / ((d*b) - (e*a)) # (d*b) == (e*a) 불가능
    x = (c - b*y) / a


# 정답
print(int(x),int(y))




