def wordPattern(pattern:str, s:str) -> bool:
    s_list = s.split()
    s_rep = {}
    num = ''
    p_num = ''
    a = 0
    for i in s_list:
        if i not in list(s_rep.keys()): 
            a += 1
            s_rep[i] = a
            num += str(a)
        else:
            num += str(s_rep[i])
    a = 0
    for i in pattern:
        if i not in list(s_rep.keys()): 
            a += 1
            s_rep[i] = a
            p_num += str(a)
        else:
            p_num += str(s_rep[i])
        print(num, p_num)
    if p_num == num:
        return True
    else:
        return False
print(wordPattern('abc', 'b a c'))