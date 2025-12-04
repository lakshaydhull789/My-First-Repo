#.....csv files

#...csv
#....reader(), writer(), writerows()

#...WAP to open and read data from a CSV FILE

'''
f=open("bharatnewcsv.csv")

import csv

data=csv.reader(f)

new=[]
for i in data:
    print(i)
    if i[1].upper()=='DELHI':
        new.append(i)

import tabulate as t
print(t.tabulate(new,headers=('name','address','salary'),tablefmt='grid'))



for i in new:
    if i[1].upper()=='DELHI':
        print(t.tabulate([i],headers=('name','address','salary'),tablefmt='grid'))


for i in new:
    if i[2]>'10000':
        print(t.tabulate([i],headers=('name','address','salary'),tablefmt='grid'))


'''






'''
data=[]
f=open("bharatnewcsv.csv","w",newline="")

x=int(input("\n\tEnter no of employees: "))
for i in range(1,x+1):
    print(f"--------Enter details for Employee Number {i}----------\n")
    name=input("\n\tEnter Name: ")
    add=input("\n\tEnter address: ")
    sal=int(input("\n\tEnter Salary: "))
    data.append([name,add,sal])


import csv
d=csv.writer(f)
d.writerows(data)
f.close()

print("\n\tdata saved!!!")

'''

'''
with open("sample.txt") as d:
    print(d.read())
'''

#d=open("sample.txt","a")
with open("sample.txt","w") as d:
    d.write("bharat")
    d.write(123)
    
    
