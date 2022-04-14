import re

codonToAA = {
    "TTT": "Phenylalanine",
    "TTC": "Phenylalanine",
    "TTA": "Leucine",
    "TTG": "Leucine",
    "CTT": "Leucine",
    "CTC": "Leucine",
    "CTA": "Leucine",
    "CTG": "Leucine",
    "ATT": "Isoleucine (Ile/I)",
    "ATC": "Isoleucine",
    "ATA": "Isoleucine",
    "ATG": "Methionine (Met/M) Start",
    "GTT": "Valine (Val/V)",
    "GTC": "Valine",
    "GTA": "Valine",
    "GTG": "Valine",
    "TCT": "Serine (Ser/S)",
    "TCC": "Serine",
    "TCA": "Serine",
    "TCG": "Serine",
    "CCT": "Proline (Pro/P)",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    "ACT": "Threonine (Thr/T)",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    "GCU": "Alanine (Ala/A)",
    "GCC": "Alanine",
    "GCA": "Alanine",
    "GCG": "Alanine",
    "TAT": "Tyrosine (Tyr/Y)",
    "TAC": "Tyrosine",
    "TAA": "Ochre/Stop",
    "TAG": "Amber/Stop",
    "CAT": "Histidine (His/H)",
    "CAC": "Histidine",
    "CAA": "Glutamine (Gln/Q)",
    "CAG": "Glutamine",
    "AAT": "(Asn/N)Asparagine",
    "AAC": "(Asn/N)Asparagine",
    "AAA": "(Lys/K)Lysine",
    "AAG": "(Lys/K)Lysine",
    "GAT": "(Asp/D)Aspartic acid",
    "GAC": "(Asp/D)Aspartic acid",
    "GAA": "(Glu/E)Glutamic acid",
    "GAG": "(Glu/E)Glutamic acid",
    "TGT": "(Cys/C)Cysteine",
    "TGC": "(Cys/C)Cysteine",
    "TGA": "Opal (Stop)",
    "TGG": "(Trp/W)Tryptophan",
    "CGT": "(Arg/R)Arginine",
    "CGC": "(Arg/R)Arginine",
    "CGA": "(Arg/R)Arginine",
    "CGG": "(Arg/R)Arginine",
    "AGT": "(Ser/S)Serine",
    "AGC": "(Ser/S)Serine",
    "AGA": "(Arg/R)Arginine",
    "AGG": "(Arg/R)Arginine",
    "GGT": "(Gly/G)Glycine",
    "GGC": "(Gly/G)Glycine",
    "GGA": "(Gly/G)Glycine",
    "GGG": "(Gly/G)Glycine",
    "GCT": "(Ala/A)Alanine"
}
seq="""TTTATGTCATAGTCATTTATGTTCATAGATTAAATTTATGTCATAGTCATTTATGTTCATAGATTAAATTTATGTCATAGTCATTTATGTTCATAGATTAAAGAAATAGCTCCCAGAAAAGCAAGCAGCCAACCAGGCAGGTTCTGTCCCTTTCACTCACTGGTTATGTCATAGTCATTTATGTTCATAGATTAAATTTATGTCATAGTCATTTATGTTCATAGATTAAATCCCAAGGCGCCACATCTCCCTCCAGAAAAGACACCATGAGCACA"""
Seq = "CCTCAGCGAGGACAGCAAGGGACTAGCCAGGAGGGAGAACAGAAACTCCAGAACATCTTGGAAATAGCTCCCAGAAAAGCAAGCAGCCAACCAGGCAGGTTCTGTCCCTTTCACTCACTGGCCCAAGGCGCCACATCTCCCTCCAGAAAAGACACCATGAGCACAGAAAGCATGATCCGCGACGTGGAACTGGCAGAAGAGGCACTCCCCCAAAAGATGGGGGGCTTCCAGAACTCCAGGCGGTGCCTATGTCTCAGCCTCTTCTCATTCCTGCTTGTGGCAGGGGCCACCACGCTCTTCTGTCTACTGAACTTCGGGGTGATCGGTCCCCAAAGGGATGAGAAGTTCCCAAATGGCCTCCCTCTCATCAGTTCTATGGCCCAGACCCTCACACTCAGATCATCTTCTCAAAATTCGAGTGACAAGCCTGTAGCCCACGTCGTAGCAAACCACCAAGTGGAGGAGCAGCTGGAGTGGCTGAGCCAGCGCGCCAACGCCCTCCTGGCCAACGGCATGGATCTCAAAGACAACCAACTAGTGGTGCCAGCCGATGGGTTGTACCTTGTCTACTCCCAGGTTCTCTTCAAGGGACAAGGCTGCCCCGACTACGTGCTCCTCACCCACACCGTCAGCCGATTTGCTATCTCATACCAGGAGAAAGTCAACCTCCTCTCTGCCGTCAAGAGCCCCTGCCCCAAGGACACCCCTGAGGGGGCTGAGCTCAAACCCTGGTATGAGCCCATATACCTGGGAGGAGTCTTCCAGCTGGAGAAGGGGGACCAACTCAGCGCTGAGGTCAATCTGCCCAAGTACTTAGACTTTGCGGAGTCCGGGCAGGTCTACTTTGGAGTCATTGCTCTGTGAAGGGAATGGGTGTTCATCCATTCTCTACCCAGCCCCCACTCTGACCCCTTTACTCTGACCCCTTTATTGTCTACTCCTCAGAGCCCCCAGTCTGTATCCTTCTAACTTAGAAAGGGGATTATGGCTCAGGGTCCAACTCTGTGCTCAGAGCTTTCAACAACTACTCAGAAACACAAGATGCTGGGACAGTGACCTGGACTGTGGGCCTCTCATGCACCACCATCAAGGACTCAAATGGGCTTTCCGAATTCACTGGAGCCTCGAATGTCCATTCCTGAGTTCTGCAAAGGGAGAGTGGTCAGGTTGCCTCTGTCTCAGAATGAGGCTGGATAAGATCTCAGGCCTTCCTACCTTCAGACCTTTCCAGATTCTTCCCTGAGGTGCAATGCACAGCCTTCCTCACAGAGCCAGCCCCCCTCTATTTATATTTGCACTTATTATTTATTATTTATTTATTATTTATTTATTTGCTTATGAATGTATTTATTTGGAAGGCCGGGGTGTCCTGGAGGACCCAGTGTGGGAAGCTGTCTTCAGACAGACATGTTTTCTGTGAAAACGGAGCTGAGCTGTCCCCACCTGGCCTCTCTACCTTGTTGCCTCCTCTTTTGCTTATGTTTAAAACAAAATATTTATCTAACCCAATTGTCTTAATAACGCTGATTTGGTGACCAGGCTGTCGCTACATCACTGAACCTCTGCTCCCCACGGGAGCCGTGACTGTAATCGCCCTACGGGTCATTGAGAGAAATAA"
def encrypt(string, length):
    return [string[i:i + length] for i in range(0, len(string), length)]

def comma_adder(string, length=3):
    return ','.join(string[i:i+length] for i in range(0,len(string),length))

def findORFs():
    pattern = re.compile(r'(?=(ATG(?:...)*?)(?<=TAG|TGA|TAA))')
    Seq= input("enter seq> ")
    tes = pattern.findall(Seq)  # forward search
    
    #[print(comma_adder(x,)) for x in tes]

    valid_seq = [[codonToAA[x] for x in encrypt(t,3)] for t in tes]
    valid_codon_number=0
    for x in tes:
        
        print(comma_adder(x))
        print(valid_seq[valid_codon_number])
        valid_codon_number += 1
        print("---------------- Codon " + str(valid_codon_number) + " ----------------")

def finditerORFs():
    
    seq = "TTTATGTCATAGTCATTTATGTTCATAGATTAAATTTATGTCATAGTCATTTATGTTCATAGATTAAATTTATGTCATAGTCATTTATGTTCATAGATTAAAGAAATAGCTCCCAGAAAA"

    test1=[m.start() for m in re.finditer('ATG', seq)]
    for i in len(test1):
        print(test1)

if __name__ == "__main__":
    findORFs()


# tes = str(tes[0])
# result = Seq.index("ATG")
# last = result + len(tes)
# valid_seq = tes + Seq[last:last + 3]
#
# total_seq_char = len(tes + Seq[last:last + 3])
# print("Total Sekans: " + str(Seq))
#
# print("ATG'den sonrası: ", encrypt(valid_seq, 3))
#
# aminoasit= [codonToAA[i] for i in encrypt(valid_seq, 3)]
# print(aminoasit)


# TODO: 1. protein dizilerini tek aa olarak yazdır. arası birleşik 
# TODO: 2. codonu aralarında virgül ile yazdır - DONE
# TODO: 3. bunu findORFs adıyla bir fonskyona çevir - DONE
# TODO: 4. findall yerine finditer ile ayrı bir fonksyon yaz.
