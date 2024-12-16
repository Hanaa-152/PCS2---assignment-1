codon_table = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUU': 'I',
    'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
    'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
    'CAA': 'Q', 'CAG': 'Q', 'CAU': 'H', 'CAC': 'H', 'CCU': 'P',
    'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
    'GGG': 'G', 'UAA': '', 'UAG': '', 'UGA': ''
}

def translate_rna(rna):
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon_table.get(codon) == '':
            break
        protein += codon_table.get(codon, '')
    return protein

rna_sequence = "AUGCGUUUCCCCGAAGUAUUGACAGUCAGUUCUGCCUGUACGUUCAAAUCGCGUUCCAUAGUCGGCCAGCAGCUGGUUUGA"
print(translate_rna(rna_sequence))
