#...WAP to open and read text file data
'''
a=open("sample data.txt","r")
data=a.read()
print("*"*70)
print("\n\t\tFile Content Currently\n")
print(data)
print("*"*70)

upper=0
for i in data:
    if i.isupper():
        upper+=1

print("\n\tTotal Uppercase Characters found=",upper)
'''

#...WAP to open sampledata.txt and copy its data into newsampledata.txt file
a=open("sample data.txt","r")
data=a.read()
b=open("newsampledata.txt","w")
b.write(data)
print(data)

vowels=0
space=0
lower=0
for i in data:
    if " " in data:
        space=space+1
    if i in 'aeiouAEIOU':
        vowels=vowels+1
    if i.islower():
        lower=lower+1
print("\n\n\t\tFile information")

print("\tTotal spaces in between character are: ",space)
print("\tTotal lower characters in file are: ",lower) 
print("\tTotal vowels in the file are: ",vowels)
b.write("\n\n\t\tFile Information\n\n")
b.write("*"*70)
b.write("\n\n\tTotal spaces in between character are: "+str(space))
b.write("\n\tTotal lower characters in file are: "+str(lower))
b.write("\n\tTotal vowels in the file are: "+str(vowels))

b.close()
