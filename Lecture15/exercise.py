#1 fun
name = input("what is your name\n")
print(name)
def intere(name):
    old = input("how old are you\n")
    print(old)
    color = input("what color do you like best\n")
    python = input("do you like python\n")
        if python = "yes" :
            print("you are a goodman")
                else: 
                    print("you need to learn some python")
    world = input("is the world a flat\n")
        if world = "yes" :
            print("you need to learn more common sense")
                else:
                    print("you have the common sense,yeah!!!")
    return

#2 DNA translation
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
def translation(DNA) :
    nondna = DNA.upper().replace("A","").replace("T","").replace("C","").replace("G","")
    DNAseq = DNA.upper()
    for i in nondna :
        DNAseq = DNAseq.replace(i,"")
    if len(DNAseq) % 3 == 0 :
        last_amino = len(DNAseq)
    if len(DNAseq) % 3 == 1 :
        last_amino = len(DNAseq) - 1
    if len(DNAseq) % 3 == 2 :
        last_amino = len(DNAseq) - 2
    #there might be last_amino = len(DNAseeq) - 2 
    protein = ""
    for start in list(range(0,last_amino,3)) :
        amino_acid = gencode[DNAseq[start:start+3],"x"] # set x as non-condon if there is no condon for the 3 base 
        protein = protein + amino_acid
    return protein
c_dna = dna.replace("G","c").replace("A","t").replace("T","a").replace("C","g").upper()
reverse DNA = c_dna[::-1] 
framestart = abs(frame) - 1 # Define the start location 


