
#1 amino acid percentage
def aa_content(protein,amino_acid):
    length = len(protein)
    amino_acid_num = protein.upper().count(amino_acid.upper())
    aa_content = 100*(amino_acid_num / length)
    print(aa_content)
    print(amino_acid_num)
    return round(aa_content) 
    
#2 amino acid percentage v2
def aa_content2(protein,amino_acid = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    length = len(protein)
    amino_acid_num = [protein.upper().count(e.upper()) for e in amino_acid]
    sum = 0
    for i in amino_acid_num:
      sum += i
    print(amino_acid_num)
    aa_content2 = 100*(sum / length)
    return round(aa_content2)
#3 undetermined bases true or false
def unbases(DNA,threshold = 0.2):
    #DNA = input("DNA sequence = ")
    length = len(DNA)
    goodbase = ["A","T","C","G"]
    sum=0
    for i in goodbase:
      sum = sum + DNA.upper().count(i)
    result = (length-sum)/length 
    return result >= threshold
#4 kmer
def kmer(DNA, Kmer = 2, n = 2):
  DNA = DNA.upper()
  kmersfound = []
  kmerrange = list(range(0,len(DNA)))
  for startingbase in kmerrange:
      if (startingbase+Kmer)< len(DNA)+1   :
          seqout = (DNA)[startingbase:startingbase+Kmer]
          kmersfound = kmersfound + [seqout]
  nonredundantset = list(set(kmersfound))
  for kmerfrequencies in nonredundantset   :
      if kmersfound.count(kmerfrequencies) > n :
           print("Lots! " + str(kmerfrequencies)+" "+str(kmersfound.count(kmerfrequencies)))
  return
#5 Kmer
DNA = input("Please enter the raw DNA sequence you want to analyse\n").upper()
Kmer = input("please enter the interested kmer-size\n")
n = input("please enter the interested threhold\n")
Kmer = int(Kmer)
n = int(n)
def kmer(DNA, Kmer = 2, n = 2):
  DNA = DNA.upper()
  kmersfound = []
  kmerrange = list(range(0,len(DNA)))
  for startingbase in kmerrange:
      if (startingbase+Kmer)< len(DNA)+1   :
          seqout = (DNA)[startingbase:startingbase+Kmer]
          kmersfound = kmersfound + [seqout]
  nonredundantset = list(set(kmersfound))
  for kmerfrequencies in nonredundantset   :
      if kmersfound.count(kmerfrequencies) > n :
           print("Lots! " + str(kmerfrequencies)+" "+str(kmersfound.count(kmerfrequencies)))
  return 
  print(kmer(DNA,Kmer,n))