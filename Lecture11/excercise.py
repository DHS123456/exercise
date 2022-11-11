#!usr/bin/python

#split the sequence
sequence = open("AJ223353.fasta")
sequence = sequence.read().replace("\n","")
coding = sequence[28:409] 
nocoding = sequence[0:28]+sequence[409:] 
seq_local = open("plain_genomic_seq.txt").read().rstrip().upper()
print(sequence)
print(seq_local)
seq_localdna = seq_local.replace("X","").replace("S","").replace("K","").replace("L","")
print(seq_localdna)
localcds = seq_localdna[0:63]+seq_localdna[90:]
local_intron = seq_localdna[63:90]
exons_out = open("All_exons.fasta", "w")
exons_out.write(">AJ223353_exon01_length" + str(len(coding)) + "\n" + coding+ "\n")
exons_out.write(">LocalSeqcds_length" + str(len(localcds)) + "\n" + localcds + "n")
exons_out.close()
print(open("All_exons.fasta").read())
introns_out = open("All_noncodings.fasta", "w")
introns_out.write(">AJ223353_noncoding01_length" + str(len(nocoding)) + "\n" + nocoding + "\n")
introns_out.write(">LocalSeq_intron01_length" + str(len(local_intron)) + "\n" + local_intron)
introns_out.close()
print(open("All_noncodings.fasta").read())

