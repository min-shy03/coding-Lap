# 옹알이

def solution(babbling):
    answer = 0
    
    possible = ["aya","ye","woo","ma"]
    
    for idx,val in enumerate(babbling) :
        for char in possible :
            if char in val :
                babbling[idx] = babbling[idx].replace(char, " ")
    
    babbling = [char.replace(" ","") for char in babbling]
    
    return len([i for i in babbling if not i])

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))