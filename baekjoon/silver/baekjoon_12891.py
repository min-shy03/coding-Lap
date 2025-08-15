# DNA 비밀번호

s, p = map(int, input().split())

dna = input()

a, c, g, t = map(int, input().split())

i = 0
j = p-1

result = 0
count = {
    "A" : 0,
    "C" : 0,
    "G" : 0,
    "T" : 0
}

for init in range(p) :
    count[dna[init]] += 1

while j < s-1 :
    if (count["A"] >= a) and (count["C"] >= c) and (count["G"] >= g) and (count["T"] >= t) :
        result += 1
    
    count[dna[i]] -= 1
    i += 1
    j += 1
    count[dna[j]] += 1

if (count["A"] >= a) and (count["C"] >= c) and (count["G"] >= g) and (count["T"] >= t) :
        result += 1

print(result)