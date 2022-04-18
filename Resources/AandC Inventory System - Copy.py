##pip install colorama
##pip install termcolor
##pip install art==4.1

import os
import time
import sys
import collections
from colorama import Fore, Back, Style, init
from termcolor import colored
from art import *
init()

class myFunctions:
    itemreader=0
    itemreadlimit=0
    
    def itemReaderforVI():
        itemreader+=20
        itemreadlimit+=20
    
    def login(self):
        global login1
        
        i=1
        while i != 2:
            print(" ")
            print(colored("               Input: ",'blue'), end = '')
            welcome = input()
            print(" ")
            if( welcome.isdigit()):
                if welcome == "2":
                    while True:
                        username  = input("            Enter a username: ")
                        password  = input("            Enter a password: ")
                        password1 = input("            Confirm password: ")
                        if password == password1:
                            filename="D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\accounts\\"+username+".txt"
                            file = open(filename, "w+")
                            file.write(username+":"+password)
                            file.close()
                            welcome = "1"
                            i=2
                            break
                        print(" ")
                        print(Style.BRIGHT+colored("          Passwords do NOT match!",'red'))
                        print(" ")
                        
         
                if welcome == "1":
                    while True:
                        login1 = input("            Login: ")
                        login2 = input("         Password: ")
                        exists = os.path.isfile("D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\accounts\\"+login1+".txt")
                        if exists:
                            i=1
                        else:
                            print(" ")
                            print("   Sorry, your account '", login1,"' doesn't exists.")
                            print("    Create account first in order to login.")
                            print(" ")
                            self.login()
                        filename1="D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\accounts\\"+login1+".txt"    
                        file = open(filename1, "r")
                        data   = file.readline()
                        file.close()
                        if data == login1+":"+login2:
                            print(" ")
                            i=2
                            os.system('cls')
                            self.menu()
                            break
                        print(" ")
                        print(Style.BRIGHT+colored("       Incorrect username or password.",'red'))
                        print(" ")
                        
                        
                if welcome == "3":
                    os.system('cls')
                    raise SystemExit
                else:
                    print("   Note: You can only select the numbers\n   given above the program.")                
                
            else:
                if "." in welcome :
                    if welcome == "2.0":
                        while True:
                            username  = input("            Enter a username: ")
                            password  = input("            Enter a password: ")
                            password1 = input("            Confirm password: ")
                            if password == password1:
                                filenamefloat="D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\accounts\\"+username+".txt"
                                file = open(filenamefloat, "w+")
                                file.write(username+":"+password)
                                file.close()
                                welcome = "1.0"
                                i=2
                                break
                            print(" ")
                            print(Style.BRIGHT+colored("          Passwords do NOT match!",'red'))
                            print(" ")
                            
             
                    if welcome == "1.0":
                        while True:
                            login1 = input("            Login: ")
                            login2 = input("         Password: ")
                            exists = os.path.isfile("D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\accounts\\"+login1+".txt")
                            if exists:
                                i=1
                            else:
                                print(" ")
                                print("   Sorry, your account '", login1,"' doesn't exists.")
                                print("    Create account first in order to login.")
                                print(" ")
                                self.login()
                            filename1="D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\accounts\\"+login1+".txt"    
                            file = open(filename1, "r")
                            data   = file.readline()
                            file.close()
                            if data == login1+":"+login2:
                                print(" ")
                                i=2
                                os.system('cls')
                                self.menu()
                                break
                            print(" ")
                            print(Style.BRIGHT+colored("       Incorrect username or password.",'red'))
                            print(" ")
                            
                    if welcome == "3.0":
                        os.system('cls')
                        raise SystemExit  
                    
                    else:
                        print("   Note: You can only select the numbers\n   given above the program.")
                else:
                    print("   Note: You can only select the numbers\n   given above the program.")            
                    i=1

    def logout(self):
        w=0
        x=0
        y=0
        z=0
        a=0
        b=0
        while a != 1:
            while w !=1:
                print("  ")
                print("   Logging out")
                print("  ")

                time.sleep(.5)
                w=1
                os.system('cls')
            while x !=1:
                print("  ")
                print("   Logging out.")
                print("  ")
                print("   "+Back.GREEN+"         ")
                print(Style.RESET_ALL)
                time.sleep(.5)
                x=1
                os.system('cls')
            while y !=1:
                print("  ")
                print("   Logging out..")
                print("  ")
                print("   "+Back.GREEN+"             ")
                print(Style.RESET_ALL)
                time.sleep(.5)
                y=1
                os.system('cls')
            while z !=1:
                print("  ")
                print("   Logging out...")
                print("  ")
                print("   "+Back.GREEN+"                           ")
                print(Style.RESET_ALL)
                time.sleep(.5)
                z=1
                os.system('cls')
            while b !=1:
                print("  ")
                print("   You've log out succesfully!")
                print("  ")
                print("   "+Back.GREEN+"                           ")
                print(Style.RESET_ALL)
                time.sleep(1)
                b=1
                os.system('cls')      
            a=1
        self.loginmenu()

    def savingItem(self):
        w=0
        x=0
        y=0
        z=0
        a=0
        b=0
        while a != 1:
            while w !=1:
                print(colored("   ====================================",'green'))
                print("  ")
                print("   Saving")
                print("  ")
                print("  ")
                print("  ")
                print(colored("   ====================================",'green'))
                
                time.sleep(.25)
                w=1
                os.system('cls')
            while x !=1:
                print("  ")
                print("   Saving.")
                print("  ")
                print("   "+Back.GREEN+"     ")
                print("  ")
                print(colored("   ====================================",'green'))
                print(Style.RESET_ALL)
                time.sleep(.25)
                x=1
                os.system('cls')
            while y !=1:
                print("  ")
                print("   Saving..")
                print("  ")
                print("   "+Back.GREEN+"                  ")
                print("  ")
                print(colored("   ====================================",'green'))
                print(Style.RESET_ALL)
                time.sleep(.5)
                y=1
                os.system('cls')
            while z !=1:
                print("  ")
                print("   Saving...")
                print("  ")
                print("   "+Back.GREEN+"                          ")
                print("  ")
                print(colored("   ====================================",'green'))
                print(Style.RESET_ALL)
                time.sleep(.25)
                z=1
                os.system('cls')
            while b !=1:
                print("  ")
                print("   Saved succesfully!")
                print("  ")
                print("   "+Back.GREEN+"                           ")
                print("  ")
                print(colored("   ====================================",'green'))
                print(Style.RESET_ALL)
                time.sleep(1)
                b=1
                os.system('cls')      
            a=1
        
    def clear(self):
        os.system("cls")

    def choice(self):
        global ch
        ch=0
        iloop=1
        while iloop != 2:
            print(colored("               Input: ",'blue'), end = '')
            user_input = input ()
            if( user_input.isdigit()):
                if user_input == "1":
                    ch = 1
                    os.system('cls')
                    self.viewInventory()
                    iloop=2
                elif user_input == "2":
                    ch = 2
                    os.system('cls')
                    self.addItem()
                    iloop=2
                elif user_input == "3":
                    ch = 3
                    iloop=2
                elif user_input == "4":
                    ch = 4
                    loop=2
                elif user_input == "5":
                    ch = 5
                    os.system('cls')
                    self.logout()
                    iloop=2
                else:
                    iloop = 1
            else:
                if "." in user_input :
                    if user_input == "1.0":
                        ch = 1
                        os.system('cls')
                        self.viewInventory()
                        iloop=2
                    elif user_input == "2.0":
                        ch = 2
                        os.system('cls')
                        self.addItem()
                        iloop=2
                    elif user_input == "3.0":
                        ch = 3
                        iloop=2
                    elif user_input == "4.0":
                        ch = 4
                        iloop=2
                    elif user_input == "5.0":
                        ch = 5
                        iloop=2
                else:        
                    print(Style.BRIGHT+colored("   Note: You can only select the numbers given above the program.",'red'))
                    iloop=1
        return ch
        
    def viewInventory(self):
        itemReaderforVI()
        select = ch
        global ch1
        if select == 1:
            print(" ")
            print(colored("   ===============================================================================",'green'))
            print(" ")
            print(Style.BRIGHT + colored("                           Arts & Craft Inventory System   ",'yellow'))
            print("   ")
            print("                                  View Inventory")
            print("    ")
            print(colored("   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",'magenta'))
            print(Style.BRIGHT+colored("    #",'grey'),Style.DIM+colored("   Item Name",'cyan'),colored("                                           Quantity",'yellow'),Style.BRIGHT+colored("    Price",'red'))
            print(colored("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯",'magenta'))
            num =1
            filename = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventory.txt"
            fileq = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            filen = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            filep = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            
            data = open(filename, "r")
            items = data.readlines()
            
            dataq = open(fileq, "r")
            datan = open(filen, "r")
            datap = open(filep, "r")
            itemsq = dataq.readlines()
            itemsn = datan.readlines()
            itemsp = datap.readlines()
            
        
            
            for item in items:
        
                numlist = str(num) + '.'
                sign="₱"
                numlistcolor = Style.BRIGHT+colored(numlist,'grey')
                ##print(itemsn[itemreader], end='')
                if itemreader != itemreadlimit:
                    count = str(itemsn[itemreader])
                else:
                    break
                ##print(len(count))
                
                
                if len(count) <= 6:
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1

                elif len(count) == 7:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1

                elif len(count) == 8:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1

                elif len(count) <= 16 and len(count) >=9:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1
                        
                elif len(count) >= 17 and len(count) <= 22:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1
   
                elif len(count) >= 23 and len(count) <= 31:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1

                elif len(count) >= 32 and len(count) <= 39:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1
  
                elif len(count) >= 40 and len(count) <= 47:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1

                elif len(count) >= 48 and len(count) <= 50:
                    
                    name, quantity, price = item.split(",")
                    print("   ",numlistcolor,"{0}\t".format(Style.DIM+colored(name,'cyan')), end = '')
                    print("{0}".format(colored(quantity,'yellow')), end = '')
                    print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                    num+=1
                    itemreader+=1
                    
                else:
                    print("error1")
            ##else:
             ##   print("error2")        
                
               
            print(colored("   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",'magenta'))
            print(colored("         [1]Back",'red'),colored("         [2]Modify",'red'))
            print(colored("   ===============================================================================",'green'))
            
            i=1
            while i != 2:
                print(" ")
                print(colored("                       Input: ",'blue'), end = '')
                userinputVI = input()
                
                if( userinputVI.isdigit()):
                    if userinputVI == "1":
                        ch1=1
                        os.system('cls')
                        self.menu()
                        i=2
                    
                    elif userinputVI == "2":
                        ch1=2
                        os.system('cls')
                        self.modifyItem()
                        i=2
                    
                    elif userinputVI == "2":
                        ch1=2
                        os.system('cls')
                        self.modifyItem()
                        i=2
                        
                    else:
                        i=1
                else:
                    if "." in userinputVI:
                        if userinputVI == "1.0":
                            ch1=1
                            os.system('cls')
                            self.menu()
                            i=2
                    
                        elif userinputVI == "2.0":
                            ch1=2
                            os.system('cls')
                            self.modifyItem()
                            i=2
                            
                        else:
                            i=1
                    else:
                        print(" ")
                        print(Style.BRIGHT+colored("   Note: You can only select the numbers given above the program.",'red'))
                        i=1
            else:
                i=1
        else:
            print("error A1")
            
        '''
        name, quantity, price = item.split(",")
        filew="D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\name.txt"
        filewrite = open(filew,"a+")
        filewrite.write(name+"\n")
        filewrite.close()
        '''

    def addItem(self):
        ##global newQuantity
        ##global newPrice
        select = ch
        if select == 2:
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            print("                Add Item")
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            print(Style.BRIGHT+colored("      Item Name: ", 'yellow'), end='')
            newItem = input()
            
            i=1
            while i != 2:
                print(colored("      Quantity: ", 'cyan'), end='')
                newQuantity = input()
                if "." in newQuantity:
                    i=2
                elif( newQuantity.isdigit()):
                    i=2
                else:
                    i=1
                    print("Please enter the Quantity of the item '",Style.BRIGHT+colored(newItem,'yellow'),"'.")
                    
            i2=1
            while i2 != 2:
                print(Style.BRIGHT+colored("      Price: ", 'red'), end='')
                newPrice = input()
                if "." in newPrice:
                    i2=2
                elif( newPrice.isdigit()):
                    i2=2
                else:
                    i2=1
                    print("Please enter the Price of the item '",Style.BRIGHT+colored(newItem,'yellow'),"'.")
            
            newP=float(newPrice)
            newPS=str(newP)
            
            filename = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventory.txt"
            file = open(filename, "a+")
            file.write("\n"+newItem+", "+newQuantity+", "+newPS)
            file.close()
            
            filename1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            file1 = open(filename1, "a+")
            file1.write("\n"+newItem)
            file1.close()
            
            filename2 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            file2 = open(filename2, "a+")
            file2.write("\n"+newQuantity)
            file2.close()
            
            filename3 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            file3 = open(filename3, "a+")
            file3.write("\n"+newPS)
            file3.close()
            
            
            print(" ")
            print(colored("   ====================================",'green'))
            
            self.savingItem()
            
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            print("   The item '", Style.BRIGHT+colored(newItem,'yellow'),"' with the quantity \n   of '",colored(newQuantity,'cyan'),"' and with the price of '",Style.BRIGHT+colored(newPS,'red'),"'\n   has been added succesfully.")
            print(" ")
            print(colored("   ====================================",'green'))
            print(Style.BRIGHT+colored("       Press [ENTER] key to Continue...",'green'), end='')
            ui = input()
            os.system('cls')
            self.menu()
        else:
            print("Error A2")

    def modifyItem(self):
        selector = ch1
        if selector == 2:
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            print("                Modify Item")
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            
            
            
            
                    
            
            filename = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventory.txt"
            fileq = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            filen = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            filep = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            
            ##------- Input Item Number
            a=1
            while a != 2:
                print(Style.BRIGHT+colored("      Item Number '(#)': ", 'grey'), end='')
                itemNumber = input()
                
                if (itemNumber.isdigit()):
                    if "." in itemNumber:
                        print("   ")
                        print("Select the item number beside the item name without a decimal.")
                        print("   ")
                        a=1
                    else:
                        intItemNumber = int(itemNumber) - 1
                        ##print(intItemNumber) --- For Checking
                        
                        itemOpenN = open(filen, 'r')
                        itemOpenQ = open(fileq, 'r')
                        itemOpenP = open(filep, 'r')
                        itemReadN = itemOpenN.readlines()
                        itemReadQ = itemOpenQ.readlines()
                        itemReadP = itemOpenP.readlines()
                        
                        a=2
                else:
                    print("   ")
                    print("Select the item number beside the item name.")
                    print("   ")
                    a=1
            
            ##------- Input Mod Item Name
            b=1
            while b != 2:
                print("   ")
                print(colored("      Old Item Name: ", 'yellow'), end='')
                print(itemReadN[intItemNumber], end='')
                print(Style.BRIGHT+colored("      Modify Item Name: ", 'yellow'), end='')
                modItemName = input()
                
                with open(filen, 'r') as file1:
                    itemsn = file1.readlines()
                
                
                itemsn[intItemNumber] = modItemName+"\n"
                
                with open(filen, 'w') as file01:
                    file01.writelines(itemsn)
                    file01.close()
                b=2;
            
            ##------- Input Mod Quantity
            c=1
            while c != 2:
                print("   ")
                print(colored("      Old Quantity: ", 'cyan'), end='')
                print(itemReadQ[intItemNumber], end='')
                print(Style.BRIGHT+colored("      Modify Quantity: ", 'cyan'), end='')
                modQuantity = input()
                
                if (modQuantity.isdigit()):
                    if "." in modQuantity:
                        with open(fileq, 'r') as file2:
                            itemsq = file2.readlines()
                        
                        
                        itemsq[intItemNumber] = modQuantity+"\n"
                        
                        with open(fileq, 'w') as file02:
                            file02.writelines(itemsq)
                            file02.close()
                        c=2;
                    else:
                        with open(fileq, 'r') as file2:
                            itemsq = file2.readlines()
                        
                        
                        itemsq[intItemNumber] = modQuantity+"\n"
                        
                        with open(fileq, 'w') as file02:
                            file02.writelines(itemsq)
                            file02.close()
                        c=2;
                else:
                    print("   ")
                    print("   Enter the quantity of the item '",Style.BRIGHT+colored(modItemName, 'yellow'),"'")
                    c=1
            
            ##------- Input Mod Price
            d=1
            while d != 2:
                print("   ")
                print(colored("      Old Price: ", 'red'), end='')
                print(itemReadP[intItemNumber], end='')
                print(Style.BRIGHT+colored("      Modify Price: ", 'red'), end='')
                modPrice = input()
                
                
                if (modPrice.isdigit()):
                    if "." in modPrice:
                        with open(filep, 'r') as file3:
                            itemsp = file3.readlines()
                        
                        newmodP=float(modPrice)
                        newmodPS=str(newmodP)
                        
                        itemsp[intItemNumber] = newmodPS+"\n"
                        
                        with open(filep, 'w') as file03:
                            file03.writelines(itemsp)
                            file03.close()
                        d=2;
                    else:
                        with open(filep, 'r') as file3:
                            itemsp = file3.readlines()
                            
                        newmodP=float(modPrice)
                        newmodPS=str(newmodP)
                        
                        itemsp[intItemNumber] = newmodPS+"\n"
                        
                        with open(filep, 'w') as file03:
                            file03.writelines(itemsp)
                            file03.close()
                        d=2;
                else:
                    print("   ")
                    print("   Enter the price of the item '",Style.BRIGHT+colored(modItemName, 'yellow'),"'")
                    d=1
            
            ##------ Finally writes to the inventory
            with open(filename, 'r') as file4:
                    items = file4.readlines()
                
                
                    items[intItemNumber] = modItemName+", "+modQuantity+", "+newmodPS+"\n"
                
            with open(filename, 'w') as file04:
                file04.writelines(items)
                file04.close()
            
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            print("   The item number'", Style.BRIGHT+colored(itemNumber,'grey'),"' named '", Style.BRIGHT+colored(modItemName,'yellow'),"' \n   with the quantity of '",colored(modQuantity,'cyan'),"' and with \n   the price of '",Style.BRIGHT+colored(newmodPS,'red'),"' has been modified.")
            print(" ")
            print(Style.BRIGHT+colored("       Press [ENTER] key to Continue...",'green'), end='')
            ui = input()
            os.system('cls')
            
            self.viewInventory()
            
        else:
            print("ErrorModify")

    def menu(self):
        print(" ")
        print(colored("   ====================================",'green'))
        print(" ")
        print(Style.BRIGHT + colored("      Arts & Craft Inventory System   ",'yellow'))
        print("   ")
        print("            Welcome,",login1)
        print("   ")
        print(colored("   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",'magenta'))
        print("   ")
        print("               1 | View Inventory")
        print("               2 | Add Item")
        print("               3 | Modify Item")
        print("               4 | Delete Item")
        print(" ")
        print("               5 | Log Out")
        print(" ")
        print(colored("   ====================================",'green'))
        print(" ")
        
        self.choice()

    def loginmenu(self):
        ##tprint("hey")
        print(" ")
        print(colored("   ====================================", 'green'))
        print(" ")
        print(Style.BRIGHT + colored("      Arts & Craft Inventory System   ",'yellow'))
        print("   ")
        print("               1 | Login")
        print("               2 | Create Acount")
        print("               3 | Exit")
        print("   ")
        print(colored("   ====================================", 'green'))
        self.login()
    
function = myFunctions()

function.loginmenu()
