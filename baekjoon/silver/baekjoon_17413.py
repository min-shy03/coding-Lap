# 단어 뒤집기 2

s = input()

stack = []
word = ""

flag = False

# 10만번 반복
for i in s :
    if i == "<" :
        if word :
            stack.append(word)
            word = ""
        flag = True
        word += i
        continue
    elif i == ">" :
        flag = False
        word += i
        stack.append(word)
        word = ""
        continue
    
    if flag :
        word += i
    else :
        if i == " " :
            if word :
                stack.append(word)
                word = ""
            stack.append(i)
        else :
            word += i

if word :
    stack.append(word)

for i in range(len(stack)) :
    if stack[i][0] != " " and stack[i][0] != "<" :
        w = list(stack[i])
        stack[i] = "".join(reversed(w))
print("".join(stack))