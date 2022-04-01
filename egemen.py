import re

thisDict = {
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
    "ATG": "Methionine (Met/M) Start1",
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

# test_dic = {"ATG": "ATG-Methionine (Met/M) Start1", "ACG": "ACG-Threonine", "ACA": "ACA-Threonine"}

array = ["A", "T", "G", "C"]


def encrypt(string, length):
    return [string[i:i + length] for i in range(0, len(string), length)]


pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
Seq = "CCTCAGCGAGGACAGCAAGGGACTAGCCAGGAGGGAGAACAGAAACTCCAGAACATCTTGGAAATAGCTCCCAGAAAAGCAAGCAGCCAACCAGGCAGGTTCTGTCCCTTTCACTCACTGGCCCAAGGCGCCACATCTCCCTCCAGAAAAGACACCATGAGCACAGAAAGCATGATCCGCGACGTGGAACTGGCAGAAGAGGCACTCCCCCAAAAGATGGGGGGCTTCCAGAACTCCAGGCGGTGCCTATGTCTCAGCCTCTTCTCATTCCTGCTTGTGGCAGGGGCCACCACGCTCTTCTGTCTACTGAACTTCGGGGTGATCGGTCCCCAAAGGGATGAGAAGTTCCCAAATGGCCTCCCTCTCATCAGTTCTATGGCCCAGACCCTCACACTCAGATCATCTTCTCAAAATTCGAGTGACAAGCCTGTAGCCCACGTCGTAGCAAACCACCAAGTGGAGGAGCAGCTGGAGTGGCTGAGCCAGCGCGCCAACGCCCTCCTGGCCAACGGCATGGATCTCAAAGACAACCAACTAGTGGTGCCAGCCGATGGGTTGTACCTTGTCTACTCCCAGGTTCTCTTCAAGGGACAAGGCTGCCCCGACTACGTGCTCCTCACCCACACCGTCAGCCGATTTGCTATCTCATACCAGGAGAAAGTCAACCTCCTCTCTGCCGTCAAGAGCCCCTGCCCCAAGGACACCCCTGAGGGGGCTGAGCTCAAACCCTGGTATGAGCCCATATACCTGGGAGGAGTCTTCCAGCTGGAGAAGGGGGACCAACTCAGCGCTGAGGTCAATCTGCCCAAGTACTTAGACTTTGCGGAGTCCGGGCAGGTCTACTTTGGAGTCATTGCTCTGTGAAGGGAATGGGTGTTCATCCATTCTCTACCCAGCCCCCACTCTGACCCCTTTACTCTGACCCCTTTATTGTCTACTCCTCAGAGCCCCCAGTCTGTATCCTTCTAACTTAGAAAGGGGATTATGGCTCAGGGTCCAACTCTGTGCTCAGAGCTTTCAACAACTACTCAGAAACACAAGATGCTGGGACAGTGACCTGGACTGTGGGCCTCTCATGCACCACCATCAAGGACTCAAATGGGCTTTCCGAATTCACTGGAGCCTCGAATGTCCATTCCTGAGTTCTGCAAAGGGAGAGTGGTCAGGTTGCCTCTGTCTCAGAATGAGGCTGGATAAGATCTCAGGCCTTCCTACCTTCAGACCTTTCCAGATTCTTCCCTGAGGTGCAATGCACAGCCTTCCTCACAGAGCCAGCCCCCCTCTATTTATATTTGCACTTATTATTTATTATTTATTTATTATTTATTTATTTGCTTATGAATGTATTTATTTGGAAGGCCGGGGTGTCCTGGAGGACCCAGTGTGGGAAGCTGTCTTCAGACAGACATGTTTTCTGTGAAAACGGAGCTGAGCTGTCCCCACCTGGCCTCTCTACCTTGTTGCCTCCTCTTTTGCTTATGTTTAAAACAAAATATTTATCTAACCCAATTGTCTTAATAACGCTGATTTGGTGACCAGGCTGTCGCTACATCACTGAACCTCTGCTCCCCACGGGAGCCGTGACTGTAATCGCCCTACGGGTCATTGAGAGAAATAA"
tes = pattern.findall(Seq)  # forward search
tes = str(tes[0])
result = Seq.index("ATG")
last = result + len(tes)
valid_seq = tes + Seq[last:last + 3]

total_seq_char = len(tes + Seq[last:last + 3])
print("Total Sekans: " + str(Seq))

print("ATG'den sonrası: ", encrypt(valid_seq, 3))

proteins = [thisDict[i] for i in encrypt(valid_seq, 3)]
print(proteins)