import tabula
import pandas as pd
tables = tabula.read_pdf("aa.pdf", pages = "all", multiple_tables = True,lattice=True)
cnt=0
cn=1
li1=[]
li2=[]

for i in tables:
    if(cnt>1 and cn!=4):
        #i.to_csv("Sel\\ng"+str(cnt)+".csv")
        #print(i)
        li1.append(i)
        cn+=1
    elif(cnt>1 and cn==4):
        cn=1
    cnt+=1
cnt=0
cn=1
for i in tables:
    if(cnt>1 and cn!=4 and (not i.empty)):
        #i.to_csv("Sel\\ng"+str(cnt)+".csv")
        #print(i)
        li2.append(i)
        cn+=1
    elif(cnt>1 and cn==4):
        cn=1
    cnt+=1

li3=[str(i) for i in li2]
#print(li3)

for i in li1:
    if(not(str(i) in li3)):
        li2.append(i)

df=pd.concat(li2)
df.to_csv("resnic3.csv")
#print(li2)
#tabula.convert_into("aa.pdf","res43.csv",output_format="csv",pages='all',lattice=True)
