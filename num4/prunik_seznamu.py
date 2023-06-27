def prunik (s, p):
    index1, index2= 0
    prunikseznam = []
    while index1<len(s) and index2<len(p):
       if s[index1] == p[index2]:
            prunikseznamu.append(s[index1])
            index1+= 1
            index2 +=1
        elif s[index1] < p[index2]:
            index1 += 1
        else:
            index2 += 1
            
    return prunikseznamu
