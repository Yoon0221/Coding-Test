# 입력받기
num_list1 = []
num_list2 = []
for i in range(3) :
    n,m = map(int, input().split())
    num_list1.append(n)
    num_list2.append(m)

# 없는 수 찾기 - x
if num_list1[0] == num_list1[1] :
    find_x = num_list1[2]
elif num_list1[0] == num_list1[2] :
    find_x = num_list1[1]
else :
    find_x = num_list1[0]

# 없는 수 찾기 - y
if num_list2[0] == num_list2[1] :
    find_y = num_list2[2]
elif num_list2[0] == num_list2[2] :
    find_y = num_list2[1]
else :
    find_y = num_list2[0]

# 결과 출력
print(find_x, find_y)
        
