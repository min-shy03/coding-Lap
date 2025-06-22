# 단어 정렬

count = int(input())

lst = []
for _ in range(count) :
    word = input()
    if word not in lst :
        lst.append(word)

# 단어를 길이 순으로 정렬 후에 사전 순으로 정렬하게 하는 방법 key 를 잘 활용할 줄 알자!
lst = sorted(lst,key=lambda x : (len(x), x))

for i in lst :
    print(i)