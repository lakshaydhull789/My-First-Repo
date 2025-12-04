#...readlines()

'''
f=open("sample data.txt","r")

data=f.readlines()

#print("total lines found in file=",len(data))

for i in data:
    print(i,end="")
'''

#....total no of words

f=open("sample data.txt","r")

data=f.read()

print(len(data.split()))

#...line by line word count
'''
f=open("sample data.txt","r")
count=1
data=f.readlines()
for i in data:
    x=i.split()
    print("line number",count,"contains",len(x),"words")
    count=count+1
'''

'''
f=open("sample data.txt","r")

data=f.readlines()

for i in data:
    x=i.split()
    if len(x)>5:
        print(i.strip())
'''


'''
o=open("sample data.txt")
d=o.readlines()
c=1
for i in d:
    
    count1=0
    for e in i:
        if e in 'aeiouAEIOU':
            count1=count1+1
    print(f"line number {c} contains {count1} vowels")
    c=c+1

'''

'''
o=open("sample data.txt.","r")
d=o.readlines()
d1=o.read()
c=1
c1=1
for i in d:
    count=0
    for e in i:
        if e not in "AEIOUaeiou":
            count=count+1
    print(f"Total number of consonents in {c} are",count)
    c=c+1
for i in d1:
    if i not in "AEIOUaeiou":
        c1=c1+1
print("Total consonents: ",c1)
'''

'''
f=open("sample data.txt")
d=f.read(5)
print(d)

d=f.read(5)
print(d)

d=f.read()
print(d)
'''


#...WAP to delete those lines whose no of words are less than 5
'''

f=open("sample data.txt")

data=f.readlines()
l=[]
for i in data:
    x=len(i.split())
    if x<5:
        pass
    else:
        l.append(i)

f.close()

f=open("sample data.txt","w")
for i in l:
    f.write(i)
f.close()
'''

import os
#...remove(), rename()

f=open("sample data.txt")
f1=open("temporary.txt","w")

data=f.readlines()
l=[]
for i in data:
    x=len(i.split())
    if x<5:
        pass
    else:
        l.append(i)

f.close()


for i in l:
    f1.write(i)
f1.close()

os.remove("sample data.txt")
os.rename("temporary.txt","sample data.txt")

