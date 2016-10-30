# -*- coding: UTF-8 -*-
from nltk.util import ngrams
import sys
import operator

n = int(sys.argv[2])
#print n
i = 0
mydict={}
temp=[]
#輸入第一個值 是檔案名稱
file_input = file(sys.argv[1],"r")
file_output = open("Data_Output.txt", "w",)

while True:
  line = file_input.readline()
  #replace mark
  line=line.replace('\n','  ')
  line=line.replace('.',' . ')
  line=line.replace(',',' , ')
  line=line.replace(':',' : ')
  line=line.replace(';',' ; ')
  line=line.replace('{',' { ')
  line=line.replace('}',' } ')
  line=line.replace('[',' [ ')
  line=line.replace(']',' ] ')
  line=line.replace('!',' ! ')
  line=line.replace('+',' + ')
  line=line.replace('-',' - ')
  line=line.replace('"',' " ')
  line=line.replace('*',' * ')
  line=line.replace('/',' / ')
  line=line.replace('=',' = ')
  line=line.replace('(',' ( ')
  line=line.replace(')',' ) ')
  line=line.replace('>',' > ')
  line=line.replace('<',' < ')
  #去除標點符號
  if line =='':
    break
  else:
    line_temp = line.split()
    for word in line_temp:
      #print word
      temp.append(word)
      #print temp
file_output.write('token:')
file_output.write('\ntoken:'.join(temp))

file_input.close()
file_output.close()