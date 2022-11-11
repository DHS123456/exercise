# read data and do some data analysis
#question 1
import os, sys, subprocess
import numpy as np
import pandas as pd
subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)
df = pd.read_csv('eukaryotes.txt', sep="\t")
df.columns
fungi = df[df.apply( lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1 )]
fungi.shape()
result = fungi.apply( lambda x : x['#Organism/Name'].split(' ')[1],axis = 1)
#question 2
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df['Group'].value_counts()
#df.groupby('Group')['WGS'].count()
#question 3
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df_result = df[df.apply( lambda x : x['#Organism/Name'].split(' ')[0] == "Heliconius", axis = 1)]
result = df_result.apply( lambda x : x['#Organism/Name'].split(' ')[1:], axis = 1)
#question 4
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df_count = df.groupby('Group')['Center'].value_counts()
df_count["Plants"]
df_count2 = df.groupby('SubGroup')['Center'].value_counts()
df_count2["Insects"]
#question 5 
#protein per gene = proteins/genes
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df["pergene"] = df["Proteins"] / df["Genes"]
df1 = df[df.apply( lambda x : x ["pergene"] > 1.1, axis =1)]
df1.apply( lambda x : x["#Organism/Name"].split(' ')[1:], axis = 1)





