# 그룹 단어 체커

# 연속된 단어를 찾아라
word_count = int(input())

answer = 0 

word_lst = []
for i in range(word_count) :
    word_lst.append(input())

for word in word_lst :
    check = True
    for idx, val in enumerate(word) :
        if val != word[idx-1] and val in word[:idx] :
            check = False
            
    if check :
        answer += 1
        
print(answer)