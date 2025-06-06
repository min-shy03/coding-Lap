# 로그인 성공?

def solution(id_pw, db):
    answer = ''

    id_lst = [id[0] for id in db]
    pw_lst = [pw[1] for pw in db]
    
    # id가 리스트에 있을 때
    if id_pw[0] in id_lst :
        if id_pw[1] == pw_lst[id_lst.index(id_pw[0])] :
            return "login"
        else :
            return "wrong pw"
    else : 
        return "fail"

# 딕셔너리 혹은 for 문을 써서 깔끔하게 풀 수 있다 나중에 다시 한 번 풀어서 복습하기

print(solution(["meosseugi", "1234"],	[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))