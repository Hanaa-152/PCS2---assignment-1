def dna_2_rna(dna_str):
    rna_str = ""
    
    for base in dna_str:
      
        rna_str += 'U' if base == 'T' else base
    
    return rna_str


dna_str = "ACGACAGAGAAGTCACTAAAGGCGGACGCAATGCTTGGTCCCGTAGCTTAACAGGCCGTATGGCTTGCTATTCAAACTCCGAACGTTTCAGGAATATAGGACTTTGCAATTTGTGTATCGCGTGTTCGGTCCCTAGCCATTTCGAGTGAAGCCAACCCCAGTACGACCGTCGACCAGTTTAGCGCGAACTGATTATTCTCGATTGCGTGCTCGATCGCCAAGTCAGCTAAGGATGCGGGATGCTAAATTGTCGCGCCGATTTCGCTGACACCCTGAAGGTCGATTGCTCAGAATCAGTCGGCTAGTGGCTAAACTGCGCATATCATTCTATGCCCGCGCCATATGAAAATAAGGACTGGCCAGGTGCCTATCGAAGTCGCCCGCCCCTGTCGCTAGCAGAACAGTTCGCAGTGGATAGCTGCTTACTAGCAAACCACGCGTCGTCCTCCTTCGTTTAATCCCCAAACCTGCCTGCTCCTTCCGAGTAGCGTGTTCTAATGTTCCGTAACCAAAACAGCCAGACGAGACAGGGGTATGAGGTACTAAGATCCGATTGGCGTACTCGCCCAGCAGAAGGCTCATGGCATTCAATTGTGCGCGTGGTTTGCGTCTAGAGAATTACTCCAACAAGCTTGATTCTCGCGGTGAATGTGCAGGATAGGGTTCACACATGGATTGCTAGCGGGGTCGACGGGTGTAAACGTGTAAATATTTTGGGCCGTGCAGCTTGTCTACAGACAGCGGGTCGAACGTCGGCTAGGTGTGAACGAAGTCAGTCTGATAATATTAAGTTGTCTGACGGACCTATTGGATTGTCGAAATTCGGGCATCGCCTATATTTTAGACACGTTTCGCACATAAGTCAGGCTTTAGGACCAATATAAATATCAAATTACGCTACAGTGAGTGATAACTCTCTATACCTATGGATTGCACTTCTGCGATAAACGTCCTTCTCGCGCCGCCGGAGCGGTCGGAAGGT"

rna_str = dna_2_rna(dna_str)

print(rna_str)