import json
import sys
filename='films.txt'
myfile=open(filename,mode='r')
films=json.load(myfile)
string1=sys.argv[1]
for i in range(2,len(sys.argv)):
    string1=string1+' '+sys.argv[i] #Проверяем если в sys.argv>1 слово
string2=string1[0].swapcase()+string1[1:]  #Меняем 1 букву. 
for num in films:
    if num.find(string1)!=-1 or num.find(string2)!=-1:
        print(num)

