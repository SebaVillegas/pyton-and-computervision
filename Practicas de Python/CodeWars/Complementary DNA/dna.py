def DNA_strand(dna):
    complementary_dna=list(dna)

    if dna == []:
        return dna
    else:
        for i in range(len(dna)):
            if dna[i] == "A" or dna[i] == "T":
                if dna[i] == "A":
                    complementary_dna[i]="".join("T")
                else:
                    complementary_dna[i]="".join("A")
            elif dna[i] == "C" or dna[i] == "G":
                if dna[i] == "C":
                    complementary_dna[i]="".join("G")
                else:
                    complementary_dna[i]="".join("C")

    complementary_dna="".join(complementary_dna)

    return complementary_dna
        
print(DNA_strand("AAAA"))
