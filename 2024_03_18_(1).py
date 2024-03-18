# 문자열을 저장할 2차원 배열 선언하기
all_str = [["#"]*15 for i in range(5)]


# 문자열 저장하기 & 가장 긴 단어의 길이 찾기
big_len = 0
for i in range(5) :
    
    str = input()
    
    if big_len < len(str) :
        big_len = len(str)

    for k in range(len(str)) :
        all_str[i][k] = str[k]



# 문자열 세로로 출력하기
for i in range(big_len) :
    for k in range(5) :
        if all_str[k][i] != "#" :
            print(all_str[k][i], end= "")
        else :
            pass
