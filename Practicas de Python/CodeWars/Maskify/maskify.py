def maskify(cc):
    new_cc= list(cc)
    if(len(new_cc) > 4):
        for i in range(len(new_cc)):
            new_cc[i]="#"
            if i == len(new_cc)-5:
                break
        
    new_cc="".join(new_cc)
    print(new_cc)
    return new_cc
    
cc="12342345634665756756988756756 765734543"
maskify(cc)