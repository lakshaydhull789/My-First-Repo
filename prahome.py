#New practise of adding data into csv file
import csv
'''
o=open("Recors.csv","a",newline="")
d=csv.writer(o)
l=[]
a=int(input("\n\t\tPlease enter the number of students info you want to enter: "))
for i in range(1,a+1):
    rl=input(f"\n\t\tPlease enter the roll no of {i} student: ")
    n=input(f"\n\t\tPlease enter the name of {i} student: ")
    ag=input(f"\n\t\tPlease enter age of {i} student: ")
    l.append([rl,n,ag])

d.writerows(l)
o.close()
'''

'''
import tabulate as t
o=open("Recors.csv","r")
d=csv.reader(o)
l=[]
l1=[]
delstat=0
b=input("\n\t\tPlease enter the age by which you want to search: ")
for i in d:
    if i[2]==b:
        l.append(i)
    else:
        l1.append(i)
if len(l)==0:
    print(f"\n\t\tNo student of age {b} found!!!")
else:
    print(t.tabulate(l,headers=("Roll_No","Name","Age"),tablefmt="grid"))
    a=input("\n\t\tType Yes if you want to delete this data:    ")
    if a.lower()=='yes':
        print("\n\t\tData deleted!!!")
        delstat=1
    else:
        print("\n\t\tNo data deleted")
o.close()
if delstat==1:
    o=open("Recors.csv","w",newline="")
    r=csv.writer(o)
    r.writerows(l1)
    o.close()
'''


'''
import csv
import os
import tabulate as t
f=open("records1.csv","r")
f1=open("temp.csv","w",newline="")
data=csv.reader(f)

x=int(input("\n\tEnter age to delete: "))

temp=0
temp1=[]
for i in data:
    if int(i[2])==x:
        print(t.tabulate([i],headers=("Roll_No","Name","Age"),tablefmt="grid"))
        temp=1
        choice=input("\n\tPress Yes to delete: ")
        if choice.upper()=="YES":
            print("\n\tData deleted: ")
        else:
            print("\n\tRecord Not deleted")
            temp1.append(i)
    else:
        temp1.append(i)

f.close()
if temp==0:
    print("\n\tRecord not found")

xx=csv.writer(f1)
xx.writerows(temp1)
f1.close()

os.remove("records1.csv")
os.rename("temp.csv","records1.csv")
'''
import csv
import tabulate as t
import os
f=open("records1.csv")
d=csv.reader(f)
a=input("\n\tPlease select the option by which you want to delete the data: \n\t1.By Name\t2.By Roll No.\n\t3.By Age")
l=[]
l1=[]
final=[]
status="no"
if a=='1':
    n=input("\n\t\tPlease type name for which you want to delete: ")
    for i in d:
        if i[1]==n:
            status="yes"
            l.append(i)
        else:
            l1.append(i)
    pos=0
    for i in l:
        print(t.tabulate([i],headers=("Roll_No","Name","Age"),tablefmt="grid"))
        cho=input("\n\tEnter YES to delete data: ")
        if cho.lower()=="yes":
            print("\n\tdata deleted")
            ch=input(f"\n\t\tType Y to see details of next {n}:")
            if ch not in 'yY':
                for k in range(pos+1,len(l)):
                    final.append(l[k])
                break
        else:
            final.append(i)
        pos=pos+1

    for i in l1:
        final.append(i)
    f.close()
    if status=='no':
        print("data not found")
    f=open("records1.csv","w",newline="")
    xx=csv.writer(f)
    xx.writerows(final)
    f.close()
