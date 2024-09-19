# https://www.acmicpc.net/problem/10989



# 알고리즘
def print_sort_list (my_list) :
    for i in range(Num) :
        if (my_list[i] == 0) :
            pass
        elif (my_list[i] == 1) :
            print(i+1)
        else :
            for k in range(my_list[i]) :
                print(i+1)


# import & define
import sys
Num = 10000


# 입력받기
n = int(input())

first_list = [0 for i in range(Num)]
for i in range(n) :
    first_list[int(sys.stdin.readline())-1] += 1
    
    
# 수행하기
print_sort_list (first_list)