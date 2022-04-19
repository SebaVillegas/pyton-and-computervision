def solution(roman):

    indice = 0
    sum = 0
    while indice < (len(roman)):
        if indice+2 < len(roman) and roman[indice] == 'I' and roman[indice+1] == 'I' and roman[indice+2] == 'I':
            sum += 3
        elif indice+1 < len(roman) and roman[indice] == 'I' and roman[indice+1] == 'I' and roman[indice-1] != 'I':
            sum += 2
        elif indice+1 < len(roman) and roman[indice] == 'I' and roman[indice + 1] == 'X':
            sum += 9
        elif indice+1 < len(roman) and roman[indice] == 'I' and roman[indice + 1] == 'V':
            sum += 4
        elif roman[indice] == 'I' and indice == 0:
            sum += 1    
        elif roman[indice] == 'I' and roman[indice-1] != 'I':
            sum += 1
        elif roman[indice] == 'V' and roman[indice - 1] != 'I':
            sum += 5
        elif indice+2 < len(roman) and roman[indice] == 'X' and roman[indice+1] == 'X' and roman[indice+2] == 'X':
            sum += 30
        elif indice+1 < len(roman) and roman[indice] == 'X' and roman[indice+1] == 'X' and roman[indice-1] != 'X':
            sum += 20
        elif indice+1 < len(roman) and roman[indice] == 'X' and roman[indice+1] == 'L':
            sum += 40
        elif indice+1 < len(roman) and roman[indice] == 'X' and roman[indice+1] == 'C':
            sum += 90  
        elif roman[indice] == 'X' and indice == 0:
            sum += 10
        elif roman[indice] == 'X' and roman[indice-1] != 'X' and roman[indice-1] != 'I':
            sum += 10
        elif roman[indice] == 'L' and indice == 0:
            sum += 50
        elif roman[indice] == 'L' and roman[indice-1] != 'X':
            sum += 50
        elif indice+1 < len(roman) and roman[indice] == 'C' and roman[indice+1] == 'M':
            sum += 900
        elif indice+1 < len(roman) and roman[indice] == 'C' and roman[indice+1] == 'D':
            sum += 400
        elif roman[indice] == 'C' and indice == 0:
            sum +=100
        elif roman[indice] == 'C' and roman[indice-1] != 'X':
            sum += 100
        elif roman[indice] == 'D' and indice == 0:
            sum += 500
        elif roman[indice] == 'D' and roman[indice-1] != 'C':
            sum += 500
        elif roman[indice] == 'M' and indice == 0:
            sum += 1000   
        elif roman[indice] == 'M' and roman[indice-1] != 'C':
            sum += 1000    

        indice += 1
    return sum


print(solution('MCMXCVI'))