# https://www.acmicpc.net/problem/2798


# 입력받기
n, m = map(int, input().split())
card_list = [i for i in list(map(int, input().split()))]


# 알고리즘 : 버블 정렬
def sort_card_list (n, card_list) :
    
    check = -1
    while(1) : 
        if (check == 0) :
            break
        # n-1 번 반복 진행
        check = 0
        for i in range(0, n-1, 1) :
            if card_list[i] < card_list[i+1] :
                pass
            else :
                temp = card_list[i]
                card_list[i] = card_list[i+1]
                card_list[i+1] = temp
                check += 1
            
        
        

# 수행하기
sort_card_list(n, card_list)
print(card_list)
     
