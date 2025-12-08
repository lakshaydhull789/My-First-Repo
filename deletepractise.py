import csv
import tabulate as t
f=open("records1.csv")
d=csv.reader(f)
l=[]
l1=[]
stat=0
ch=input("\n\t\tBy what optino you want to delete the data.\n\t1.By Name\t2.By Roll No\n\tPlease enter your choice: ")
if ch=='1':
    n=input("\n\tPlease enter the name by which you want to delete the data: ")
    for i in d:
        if i[1]==n:
            l.append(i)
            stat=1
        else:
            l1.append(i)
    ct=0
    for i in l:
        print(t.tabulate([i],headers=("Roll_No","Name","Age"),tablefmt="grid"))
        dc=input("\n\tType yes if you want to delete this data: ")
        if dc.lower()=='yes':
            print("\n\tData deleted!!!")
            nd=input(f"\n\tType Y if you want to see data of next person name {n}")
            if nd.lower!='y':
                for k in range(ct+1,len(l)):
                    l1.append(l[k])                    
                break
        if ct+1==len(l):
            print(f"\n\tNo more student with {n} name")
        else:
            l1.append(i)
        ct=ct+1
    f.close()
    if stat==0:
        print(f"\n\t\tNo data found by name {n}")
    f=open("records1.csv","w",newline="")
    ne=csv.writer(f)
    ne.writerows(l1)
    f.close()
if ch=='2':
    r=input("\n\tPlease enter the roll no by which you want to delete the data: ")
    for i in d:
        if i[0]==r:
            print(t.tabulate([i],headers=("Roll_No","Name","Age"),tablefmt="grid"))
            dc=input("\n\tType yes if you want to delete this data: ")
            if dc.lower()=='yes':
                print("\n\tData deleted!!!")
            else:
                l1.append(i)
    f=open("records1.csv","w",newline="")
    ne=csv.writer(f)
    ne.writerows(l1)
    f.close()
else:
    print("\n\t\tInvalid option selected")
