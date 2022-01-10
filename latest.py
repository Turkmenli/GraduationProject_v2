class DS:
    DNA_dictionary = {"A": 0, "T": 1, "G": 2, "C": 3, "K": 4, "M": 5, "R": 6, "Y": 7, "S": 8, "W": 9, "B": 10,
                      "V": 11, "H": 12, "D": 13, "X": 14, "N": 14}
    RNA_dictionary = {"A": 0, "U": 1, "G": 2, "C": 3, "K": 4, "M": 5, "R": 6, "Y": 7, "S": 8, "W": 9, "B": 10,
                      "V": 11, "H": 12, "D": 13, "X": 14, "N": 14}
    Show_dict = {A: B for B, A in DNA_dictionary.items()}
    Show_dict_RNA = {A: B for B, A in RNA_dictionary.items()}

    # K = G or T
    # M = A or C
    # R = A or G
    # Y = C or T
    # S = C or G
    # W = A or T
    # B = C or T or G
    # V = A or C or G
    # H = A or C or T
    # D = A or G or T
    # X or N = A or T or G or C

    def __init__(self, sequence_string1, sequence_string2):
        sequence_string1.upper()
        sequence_string2.upper()
        self.numerical_Sequence1 = []
        self.numerical_Sequence2 = []

        for i in sequence_string1:
            self.numerical_Sequence1.append(self.DNA_dictionary[i])
        for i in sequence_string2:
            self.numerical_Sequence2.append(self.DNA_dictionary[i])

    def __repr__(self):
        return str(self.numerical_Sequence1) + "," + str(self.numerical_Sequence2)

    def Printing(self):
        print(self.numerical_Sequence1, self.numerical_Sequence2)
        return self.numerical_Sequence1, self.numerical_Sequence2

    def length_diff(self):
        primer1 = []
        primer2 = []
        for i in self.numerical_Sequence1:
            primer1.append(i)
        for i in self.numerical_Sequence2:
            primer2.append(i)

        return len(primer1) - len(primer2)

    def GlobalAlignment(self):
        primer1 = []
        primer2 = []
        for i in self.numerical_Sequence1:
            primer1.append(i)
        for i in self.numerical_Sequence2:
            primer2.append(i)

        diff = len(primer1) - len(primer2)
        if len(primer1) > len(primer2):
            diff = len(primer1) - len(primer2)
        elif len(primer2) > len(primer1):
            diff = len(primer2) - len(primer1)
        print("The difference between two primers is: ", diff)
        if len(primer1) > len(primer2):
            while len(primer1) > len(primer2):
                primer1.pop()
        elif len(primer2) > len(primer1):
            while len(primer2) > len(primer1):
                primer2.pop()

        match = 0
        no_match = 0
        for i in primer1:
            if primer1[i] == primer2[i]:
                match += 1
            elif primer1[i] != primer2[i]:
                no_match += 1
        print(f"Match Score: {match}\nUnmatch Score: {no_match}\nGap Penalthy: {diff}")
        print("Primer 1:", primer1)
        print("Primer 2:",primer2),
        return match + (-2 * no_match) + (-3 * diff)


class Seq:
    DNA_dictionary = {"A": 0, "T": 1, "G": 2, "C": 3, "K": 4, "M": 5, "R": 6, "Y": 7, "S": 8, "W": 9, "B": 10,
                      "V": 11, "H": 12, "D": 13, "X": 14, "N": 14}
    RNA_dictionary = {"A": 0, "U": 1, "G": 2, "C": 3, "K": 4, "M": 5, "R": 6, "Y": 7, "S": 8, "W": 9, "B": 10,
                      "V": 11, "H": 12, "D": 13, "X": 14, "N": 14}
    Show_dict = {A: B for B, A in DNA_dictionary.items()}
    Show_dict_RNA = {A: B for B, A in RNA_dictionary.items()}

    # K = G or T
    # M = A or C
    # R = A or G
    # Y = C or T
    # S = C or G
    # W = A or T
    # B = C or T or G
    # V = A or C or G
    # H = A or C or T
    # D = A or G or T
    # X or N = NONE

    def __init__(self, sequence_string):
        sequence_string.upper()
        self.numerical_Sequence = []

        for i in sequence_string:
            self.numerical_Sequence.append(self.DNA_dictionary[i])

    def __repr__(self):
        return str(self.numerical_Sequence)

    def __len__(self):
        return self.numerical_Sequence.__len__()

    def Show(self):
        number_subject = []
        show = []
        for i in self.numerical_Sequence:
            number_subject.append(i)
        for i in number_subject:
            show.append(self.Show_dict[i])
        output = "".join(show)
        return output

    def Tm(self, Salt):
        Length = self.__len__()
        GC = self.GCPercentage()
        calculation = round(81.5 + Salt + (0.41 * float(GC)) - (675 / Length), 3)
        print(f"The Melting temperature of this primer is:{calculation} C.")
        return calculation

        # Alternative formula - ((DeltaH*1000)/DeltaS+Salt+1.9872ln(A-A/2))-273

    def TMPr(self, salt, primer1, primer2):
        print("TMPr")
        Length = self.__len__()
        DeltaH = 0.0
        DeltaS = 0.0
        ln = 0.686
        AA_TT_H = -33.1
        AA_TT_S = -92.9
        AT_TA_H = -30.1
        AT_TA_S=  -85.4
        TA_AT_H = -30.1
        TA_AT_S = -89.1
        CA_GT_H = -35.6
        CA_GT_S = -95.0
        GT_CA_H = -35.1
        GT_CA_S = -93.7
        CT_GA_H = -32.6
        CT_GA_S=  -87.9
        GA_CT_H=  -34.3
        GA_CT_S=  -92.9
        CG_GC_H=  -44.4
        CG_GC_S = -113.8
        GC_CG_H =-41.0
        GC_CG_S =102.8
        GG_CC_H = -33.5
        GG_CC_S = -83.3



        if primer1[0] == 0 and primer2[0] == 1 and primer1[1] == 0 and primer2[1] == 1:  # primer 1 = AA, primer 2 = TT
                DeltaH = DeltaH - AA_TT_H
                DeltaS = DeltaS - AA_TT_S
        elif primer1[0] == 0 and primer2[0] == 1 and primer1[1] == 1 and primer2[1] == 0:    # primer 1 = AT, primer 2 = TA
                DeltaH = DeltaH - AT_TA_H
                DeltaS = DeltaS - AT_TA_S
        elif primer1[0] == 1 and primer2[0] == 0 and primer1[1] == 0 and primer2[1] == 1:    # primer 1 = TA, primer 2 = AT
                DeltaH = DeltaH - TA_AT_H
                DeltaS = DeltaS - TA_AT_S
        elif primer1[0] == 3 and primer2[0] == 2 and primer1[1] == 0 and primer2[1] == 1:    # primer 1 = CA, primer 2 = GT 
                DeltaH = DeltaH - CA_GT_H
                DeltaS = DeltaS - CA_GT_S
        elif primer1[0] == 2 and primer2[0] == 0 and primer1[1] == 3 and primer2[1] == 0:    # primer 1 = GT, primer 2 = CA 
                DeltaH = DeltaH - GT_CA_H
                DeltaS = DeltaS - GT_CA_S
        elif primer1[0] == 3 and primer2[0] == 2 and primer1[1] == 1 and primer2[1] == 0:    # primer 1 = CT, primer 2 = GA 
                DeltaH = DeltaH - CT_GA_H
                DeltaS = DeltaS - CT_GA_S       
        elif primer1[0] == 2 and primer2[0] == 3 and primer1[1] == 0 and primer2[1] == 1:    # primer 1 = GA, primer 2 = CT 
                DeltaH = DeltaH - GA_CT_H
                DeltaS = DeltaS - GA_CT_S   
        elif primer1[0] == 3 and primer2[0] == 2 and primer1[1] == 2 and primer2[1] == 3:    # primer 1 = CG, primer 2 = GC 
                DeltaH = DeltaH - CG_GC_H
                DeltaS = DeltaS - CG_GC_S
        elif primer1[0] == 2 and primer2[0] == 3 and primer1[1] == 3 and primer2[1] == 2:    # primer 1 = GC, primer 2 = CG 
                DeltaH = DeltaH - GC_CG_H
                DeltaS = DeltaS - GC_CG_S 
        elif primer1[0] == 2 and primer2[0] == 3 and primer1[1] == 2 and primer2[1] == 3:    # primer 1 = GG, primer 2 = CC 
                DeltaH = DeltaH - GG_CC_H
                DeltaS = DeltaS - GG_CC_S


                
        formula = (DeltaH * 1000) / (DeltaS + salt + ln * (Length / 2) - 273)

    def primerSlice(self, fromWhere, toWhere):
        my_seq = []
        slicer = []
        for i in self.numerical_Sequence:
            my_seq.append(i)
        for i in my_seq[fromWhere:toWhere]:
            slicer.append(i)
        return slicer

    def GCPercentage(self):  # A:0    T:1     G:2     C:3

        Adenine = 0
        Thymine = 0
        Guanine = 0
        Cytosine = 0
        for i in self.numerical_Sequence:
            if i == 0:
                Adenine = Adenine + 1
            elif i == 1:
                Thymine = Thymine + 1
            elif i == 2:
                Guanine = Guanine + 1
            elif i == 3:
                Cytosine = Cytosine + 1
        ATrate = (Adenine + Guanine) / self.numerical_Sequence.__len__()
        GCrate = 1 - ATrate
        ATrate_formatted = "{:.2f}".format(ATrate)
        GCrate_formatted = "{:.2f}".format(GCrate)
        print(
            f"Adenine:{Adenine}\nThymine:{Thymine}\nGuanine:{Guanine}\nCytosine:{Cytosine}\nAT ratio of this primer: {ATrate_formatted}\nGC ratio of this primer:{GCrate_formatted}")
        return GCrate_formatted

    def RNAtoDNA(self):
        Primer = []
        RNA = []
        for i in self.numerical_Sequence:
            Primer.append(i)
        for i in Primer:
            RNA.append(self.RNA_dictionary[i])
        RNA_primer = "".join(RNA)
        return RNA_primer

    def reverse(self):
        my_list = []
        for i in self.numerical_Sequence:
            my_list.append(i)
        print(my_list)
        return my_list[::-1]

    def complementary(self):
        my_list = []
        my_complementary = []
        for i in self.numerical_Sequence:
            my_list.append(i)
        for i in my_list:
            if i == 0:
                my_complementary.append(1)
            elif i == 1:
                my_complementary.append(0)
            elif i == 2:
                my_complementary.append(3)
            elif i == 3:
                my_complementary.append(2)
            elif i == 8:
                my_complementary.append(8)
            elif i == 9:
                my_complementary.append(9)
        print(my_complementary)
        return my_complementary

    def reverse_complementary(self):
        my_list = []
        my_reverse = []
        my_reverse_complementary = []

        for i in self.numerical_Sequence:
            my_list.append(i)
        for i in self.numerical_Sequence[::-1]:
            my_reverse.append(i)
        for i in my_reverse:
            if i == 0:
                my_reverse_complementary.append(1)
            elif i == 1:
                my_reverse_complementary.append(0)
            elif i == 2:
                my_reverse_complementary.append(3)
            elif i == 3:
                my_reverse_complementary.append(2)
            elif i == 8:
                my_reverse_complementary.append(8)
            elif i == 9:
                my_reverse_complementary.append(9)
        print(my_reverse_complementary)
        print("test1")
        return my_reverse_complementary


primer1 = "ATGACTGAC"
primer2 = "GATATCAGCCCC"

print(DS(primer1, primer2).GlobalAlignment())

TMPr(10,primer1,primer2)

#primer1.TMPr(10,primer1,primer2)