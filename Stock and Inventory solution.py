    #Stock inventory management system
from stockfunction import*
while True:
    print("\n\t\tWelcome to Inventory and Stock Management System")
    print("\n\t\t1. Add Product")
    print("\t\t2. Update Product details")
    print("\t\t3. View all inventory")
    print("\t\t4. Show items which are out of stock")
    print("\t\t5. Want to see a specific product?")
    print("\t\t6. Delete a certain product out of Inventory")
    print("\t\t7. Create a text document file")
    print("\t\t8. Exit")
    a=int(input("\t\tPlease select the operation you want to perform: "))
    if a==1:
        addprdt()
    if a==2:
        updtprdt()
    if a==3:
        viewall()
    if a==4:
        outstk()
    if a==5:
        spfprdt()
    if a==6:
        delprdt()
    if a==7:
        textdmt()
    if a==8:
        print("\t\tThank you for using our application")
        break
    if a>8 or a<0:
        print("\t\tInvalid input")
        
