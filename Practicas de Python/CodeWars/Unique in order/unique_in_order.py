def unique_in_order(iterable):
    copy=list(iterable)    
    i=0
    #copy.append("@")
    while i <= len(copy):
        if i == len(copy)-1:
            copy.pop(i)
            break
        elif copy[i] == copy[i+1]:
            copy.pop(i+1)
        else:
            i= i+ 1
    if type(copy) is str:
        copy = "".join(copy)    
        return copy
    else:
        return copy
    
    

print(unique_in_order('ABBCcAD')) 
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([3,1,2,2,3,3]))