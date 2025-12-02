#.....FILE HANDLING
'''

FILE IS A COLLECTION OF DATA

file is of 3 types...
1) text file
2) binary file
3) CSV file

file operations

1) create
2) delete

3) rename
4) open
5) close

6) read
7) write

file opening modes
1) r(read)
2) w(write)
3) a(append)
'''

#...WAP to create a text file "data.txt" and store student names in it
'''
a=open("data.txt","a")
name=input("\n\tEnter Student Name: ")
a.write(name)
a.close()
'''


'''
a=open("records","a")

size=int(input("\n\tTotal Names: "))
for i in range(1,size+1):
    name=input("\n\tEnter Name: ")
    name="Name: "+name+"\n"
    a.write(name)
a.close()
print("\n\t!!!Data Saved!!!")
'''

new=open("Empdata.txt.","a")
l=int(input("\t\tHow many employees data you want to enter"))
for i in range (0,l):
    Name=input("\t\tPlease enter employee Name: ")
    EmpID=input("\t\tPlease enter employee ID:")
    Des=input("\t\tPlease enter employee designation: ")
    empdata="\nName: "+Name+"\tEmployee ID: "+EmpID+"\tDesignation: "+Des+"\n"
    new.write(empdata)
    new.write("_"*70)
    
      
              
new.close()
print("\n\t-----------Data Saved to file-----------------")
