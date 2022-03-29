import random

DNA_dictionary = {"A": 0, "T": 1, "G": 2, "C": 3, "K": 4, "M": 5, "R": 6, "Y": 7, "S": 8, "W": 9, "B": 10,
                      "V": 11, "H": 12, "D": 13, "X": 14, "N": 14}
RNA_dictionary = {"A": 0, "U": 1, "G": 2, "C": 3, "K": 4, "M": 5, "R": 6, "Y": 7, "S": 8, "W": 9, "B": 10,
                      "V": 11, "H": 12, "D": 13, "X": 14, "N": 14}
Show_dict = {A: B for B, A in DNA_dictionary.items()}
Show_dict_RNA = {A: B for B, A in RNA_dictionary.items()}


seq = ["A", "T", "G", "C"]


print(random.choice(list(DNA_dictionary)))


import random

array = ["A", "T", "G", "C"]
dna = ''
x=1
i=0
atg_number = 0
total_dna_number = 20

#GAT GAC

while i<total_dna_number:
    for x in range(3):
        nic = random.choice(array)
        dna = dna + nic

    if i == total_dna_number-1:
        print(dna)
        dna_converted = dna.replace("T", "U")
        print(dna_converted)
    i=i+1