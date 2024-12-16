
def reverse_complement(dna):
    dna_pairs = {"A": "T", "C": "G", "T": "A", "G": "C"}
    
    reverse_comp = "".join(dna_pairs[base] for base in dna[::-1])
    return reverse_comp

dna_str = "CGACGCTAAGTGCCTGTCTTGCCCGCGATTTGCCAGTAAACCGCATTCATTTCGGGTCGAACGGACAGTATACTGGGGGTCCGTTGCCGTTGGCGGGGCCATTTTCGTACCCATTAGGTTAAAACTTCCCGTAGTCACACGACATTATCGTGCATACGTCTAATAGCTAACAATTTCGGGGGGCCGGTTTCTGGCATACCCGCATAGATAGACCATCATATTGTGCGGTGTCACGCGTGCGCTCGAGCCTACAACTGCGCGCGGAATAATTGGGTACATGCGTGTTACGGCAGCCACCGGAGATGGGCGAGGGCTCGATGGACCTACCTAACCTGGGTACCTTCACTCCACTAGGGGCAAGTCCATAGGGCGCACTGTCCTGTGTAGATTTCGAAGGATTGTGAGGCGACACTGTATGTTGACCCATCGCCTATAAATGCCAAACTCTCCCAAGAAATTCGCGCTGGAGATCCTGATGCGACTCCCTTAGGAGCCCACGCCGAAGTTTATCCGGCCACTTGTATCGATTCCCTACGCTTGACCTAAGGCTTTACACCCTGTGTACTTAGGGTGCTTCACACTAGCAACCAAAACAAGATCAGAAGACTCGAAGAGGAGAGGATGCATCCCTTTGGCGTCAACTTATGAAAGTACCACAAGGTAAGGCCTACTATCACGAGTGTTAAGGTAAGCATTCTGACATGAAGACGCATCTCTCCAGAACTGATAGGATCCGATCGTAGTGTGACTGCCACCGAGCCTAGGAAATGGTGAGCCCGGTCAGCCAACCTACTGGTTTCAATTTGAGTCTAGGAATTCTTTAATTCTGAGTCTTACAGGGACGCATTCAACAGGATTCCGTTATACTGTGGTACCTAGGTGATTTTACAGCCCTTAGGTTATTCTT"
result = reverse_complement(dna_str)
print(result)
