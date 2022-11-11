#!usr/bin/python
#1
import os 
data2= open('data.csv')

#print(data)
for line in data2: 
  line=line.split(',')
  if line[0] == "Drosophila melanogaster" or line[0] == "Drosophila simulans" :
    print(line[0],":", "genename is", line[2])
  if len(line[1]) > 90 and len(line[1]) < 110
    print("base is between 90 and 110" , line[2])    
  if line[3] > 200 and (line[1]count.("a")+line[1].count("t"))/len(line[1]) < 0.5
    print("condition is fullfilled", line[2])
  if str(line[2]).startswith("k") or line[2].startswith("h") and line[0] != "Drosophila melanogaster"
    print("complete conditions is fullfilled", line[2])
  if (line[1]count.("a")+line[1].count("t"))/len(line[1]) > 0.65
    print (line[2],"high"))
  	elif (line[1]count.("a")+line[1].count("t"))/len(line[1]) < 0.45
    	print (line[2],"low"))
  		elif
    		print (line[2],"medium"))
		  
  
#else 
 
 
	
