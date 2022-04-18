##pip install colorama
##pip install termcolor
##pip install art==4.1

import os
import time
import sys
import collections
import itertools
import emoji
import shutil
from colorama import Fore, Back, Style, init
from termcolor import colored
from art import *
from decimal import Decimal

init()

class myFunctions:

    itemreader=0
    itemreadlimit=20
    num=1
    itemPage=20
    itemAddNumPage=1
    
    def itemPaging(self):
        ##self.itemReaderforVI()
        
        filenameforPaging = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventory.txt"
        countPage = len(open(filenameforPaging).readlines(  )) 
        ##print (countPage)
        
        IPhold = countPage / 20
        IPchecker = int(IPhold)
        ##print(IPhold)
        
        if IPchecker == IPhold:
            IPholdV = int(IPhold)
        
            IPmaxPage = str(IPholdV)
        else:
            IPholdV = int(IPhold)
            IPholdV1 = IPholdV + 1
            IPmaxPage = str(IPholdV1)
            
        ##print(IPmaxPage) --- String Integer not Float
        
        
        
        self.IPmaxPageShare = IPmaxPage
        
    def itemReaderforVI(self):
        self.itemreader
        self.itemreadlimit
        self.num
        self.itemPage
        self.itemAddNumPage
        self.filename = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventory.txt"
        self.data = open(self.filename, "r")


    ## ---- If user input is 5 in view Inventory(currently 1-4), Still in progress Ma'am
    def itemPageChoice(self):
        self.itemPaging()
        self.itemReaderforVI()
        print(" ")
        print(colored("                       Select Page: ",'blue'), end = '')
        userinputIPC = input()
        if( userinputIPC.isdigit()):
            int_userinputIPC = int(userinputIPC)
            a = self.num - 1
            b = self.itemPage * int_userinputIPC
            IPCcheck = b / a
            ##IPCcheck1 = (Decimal(IPCcheck).normalize())
            IPCcheck2 = str(int(IPCcheck))
            print(a," <-- num")
            print(b," <-- b")
            print(self.itemPage," <-- itempage")
            print(int_userinputIPC," <-- input to INT")
            print(IPCcheck2," <-- ipcheck2")
            ##print(IPCcheck1," <-- ipcheck1")
            print(IPCcheck," <-- ipcheck")
            
            self.itemreader = 0
            self.itemreadlimit = 20
            self.num = 1
            
            if userinputIPC == "1":
                os.system('cls')
                self.itemreader = 0
                self.itemreadlimit = 20
                self.num = 1
                self.itemAddNumPage = 1
                self.viewInventory()
            elif userinputIPC == IPCcheck2:
                os.system('cls')
                self.itemAddNumPage = int_userinputIPC
                
                value = self.IPmaxPageShare * 10
                
                self.itemreader = 0
                self.itemreadlimit = 20
                self.num = 1
                
                self.itemreader = 1 * (int_userinputIPC * 10)
                self.itemreadlimit = 1 * (int_userinputIPC * 20)
                
                self.num = 1 + (20*(int_userinputIPC-1))
                
                print(a," <-- num")
                print(b," <-- b")
                print(self.itemPage," <-- itempage")
                print(int_userinputIPC," <-- input to INT")
                print(IPCcheck2," <-- ipcheck2")
                ##print(IPCcheck1," <-- ipcheck1")
                print(IPCcheck," <-- ipcheck")
                ##time.sleep(5)
                
                self.viewInventory()
        
            
        else:
            if "." in userinputIPC:
                print(" no decimal output")
            else:
                print("error paging")
        
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
             
                elif user_input == "5":
                    ch = 5
                    os.system('cls')
                    self.logout()
                    iloop=2
                else:
                    print(Style.BRIGHT+colored("   Note: You can only select the numbers given above the program.",'red'))
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
                    elif user_input == "5.0":
                        ch = 5
                        iloop=2
                else:        
                    print(Style.BRIGHT+colored("   Note: You can only select the numbers given above the program.",'red'))
                    iloop=1
        return ch
    
    def choiceVI(self):
        global ch1
        self.itemReaderforVI()
        self.itemPaging()
        i=1
        while i != 2:
            print(" ")
            print(colored("                       Input: ",'blue'), end = '')
            userinputVI = input()
            
            if( userinputVI.isdigit()):
                if userinputVI == "1":
                    ch1=1
                    os.system('cls')
                    self.itemreader=0
                    self.itemreadlimit=20
                    self.num=1
                    self.itemAddNumPage=1
                    self.menu()
                    i=2
                
                elif userinputVI == "2":
                    ch1=2
                    os.system('cls')
                    self.modifyItem()
                    i=2
                    
            
                elif userinputVI == "3":
                    ch1=3
                    
                    
                    if self.itemreader == 20:
                        
                        print(" ")
                        print("            Minimum Page!")
                        ##print("            [1] Back | [2] Modify Item | [4] Next Page")
                        i=1
                    else: 
                    
                        os.system('cls')
                        self.itemAddNumPage-=1
                        if self.itemreader <= 0:
                            self.itemreader = 0
                        elif self.itemreader >= 20 and self.itemreader <=39:
                            
                            self.itemreader = self.itemreader - 20
                        elif self.itemreader >= 40:
                            self.itemreader = self.itemreader - 40
                        
                        if self.itemreadlimit <= 20:
                            self.itemreadlimit = 20
                        elif self.itemreadlimit >= 40:
                            self.itemreadlimit = self.itemreadlimit - 20
                            
                        if self.num == 1:
                            self.num = 1
                        elif self.num >= 20 and self.num <= 39:
                            self.num = self.num - 20
                        elif self.num >= 40:
                            self.num = self.num - 40
                        ##self.items[self.itemreader:self.itemreadlimit]
                        self.viewInventory()
                        i=2
                
                elif userinputVI == "4":
                    ch1=4
                    ##print(self.num) --- checking
                    
                    CVIpagelimit = (self.num - 1) / self.itemPage
                    CVIpagelimit1 = (Decimal(CVIpagelimit).normalize())
                    
                    ##print(CVIpagelimit1) --- checking
                    
                    CVIpagelimit2 = str(CVIpagelimit1)
                    
                    if self.itemAddNumPage == self.IPmaxPageShare:
                    
                        print(" ")
                        print("            You have reached the maximum page.")
                        i=1
                    elif "." in CVIpagelimit2:
                    
                        ##print(CVIpagelimit2) --- checking
                        print(" ")
                        print("            You have reached the maximum page.")
                        i=1
                    
                    
                    else:
                        os.system('cls')
                        self.itemAddNumPage+=1
                        self.itemreadlimit+=20
                        ##self.items[self.itemreader:self.itemreadlimit]
                        self.viewInventory()
                        i=2
                
                elif userinputVI == "5":
                        
                        
                        self.itemPageChoice()
                        
                        i=2
                
                elif userinputVI == "9":
                    ch1=9
                    os.system('cls')
                    self.deleteItem()
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
              
    def viewInventory(self):
        self.itemReaderforVI()
        self.itemPaging()
        select = ch
        '''
        print(self.itemreader,"start")
        print(self.itemreadlimit,"limit")
        print(self.itemreader,"counts")
        '''
        ##print(self.IPmaxPageShare)
        ##print(self.itemAddNumPage)
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
            ##num =1
            
            fileq = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            filen = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            filep = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            
            
            
            dataq = open(fileq, "r")
            datan = open(filen, "r")
            datap = open(filep, "r")
            itemsq = dataq.readlines()
            itemsn = datan.readlines()
            itemsp = datap.readlines()
            
        
            with self.data as items:
                
                for item in itertools.islice(items, self.itemreader, self.itemreadlimit):
                    
                    numlist = str(self.num) + '.'
                    sign="₱"
                    numlistcolor = Style.BRIGHT+colored(numlist,'grey')
                    ##print(self.itemreader)
                    ##print(self.itemreadlimit)
                    ##print(itemsn[self.itemreader], end='')
                    
                    if self.itemreader != self.itemreadlimit:
                        count = str(itemsn[self.itemreader])
                    else:
                        ##print("  ")
                        break
                        
                        
                    ##print(len(count))
                    
                    
                    if len(count) <= 6:
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1

                    elif len(count) == 7:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1

                    elif len(count) == 8:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1

                    elif len(count) <= 16 and len(count) >=9:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1
                            
                    elif len(count) >= 17 and len(count) <= 22:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1
       
                    elif len(count) >= 23 and len(count) <= 31:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1

                    elif len(count) >= 32 and len(count) <= 39:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1
      
                    elif len(count) >= 40 and len(count) <= 47:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1

                    elif len(count) >= 48 and len(count) <= 50:
                        
                        name, quantity, price = item.split(",")
                        print("   ",numlistcolor,"{0}\t".format(Style.DIM+colored(name,'cyan')), end = '')
                        print("{0}".format(colored(quantity,'yellow')), end = '')
                        print("\t  {0}".format(Style.BRIGHT+colored(sign+price,'red')))
                        self.num+=1
                        self.itemreader+=1
                        
                    else:
                        print("error1")
            ##else:
             ##   print("error2")   
            print(colored("   -------------------------------------------------------------------------------",'magenta'))
            print("                                 Page ",self.itemAddNumPage, "of ",self.IPmaxPageShare)   
            if self.itemreader == 20:
                print(colored("   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",'magenta'))
                print(colored("    [1]Back",'red'),colored("    [2]Modify",'red'),colored("    [3]Previous Page",'red'),colored("    [4]Next Page",'red'),colored("    [9]Delete Item",'red'))
                print(colored("   ===============================================================================",'green'))
                print("  ")
            elif self.itemreader >= 21:
            
                VIpagelimit = (self.num - 1) / self.itemPage
                VIpagelimit1 = (Decimal(VIpagelimit).normalize())
                
                ##print(CVIpagelimit1) --- checking
                
                VIpagelimit2 = str(VIpagelimit1)
                if VIpagelimit2 == str(VIpagelimit1):
                    
                    
                    print(colored("   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",'magenta'))
                    print(colored("    [1]Back",'red'),colored("    [2]Modify",'red'),colored("    [3]Previous Page",'red'),colored("    [4]Next Page",'red'),colored("    [9]Delete Item",'red'))
                    print(colored("   ===============================================================================",'green'))
                    print("  ")
                elif self.itemAddNumPage == self.IPmaxPageShare:
                    print(colored("   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",'magenta'))
                    print(colored("    [1]Back",'red'),colored("         [2]Modify",'red'),colored("         [3]Previous Page",'red'),colored("         [9]Delete Item",'red'))
                    print(colored("   ===============================================================================",'green'))
                    print("  ")
                    
                
            
            '''
            print(self.itemreader,"start")
            print(self.itemreadlimit,"limit")
            print(self.itemreader,"counts")
            print("  ")
            '''
            self.choiceVI()   
            
            
            ##self.itemreader+=10
            
            
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
        self.itemReaderforVI()
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
            file = open(filename, "a")
            file.write("\n"+newItem+", "+newQuantity+", "+newPS)
            file.close()
            
            filename1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            file1 = open(filename1, "a")
            file1.write("\n"+newItem)
            file1.close()
            
            filename2 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            file2 = open(filename2, "a")
            file2.write("\n"+newQuantity)
            file2.close()
            
            filename3 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            file3 = open(filename3, "a")
            file3.write("\n"+newPS)
            file3.close()
            
            
            '''
            filename10 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventoryStrip.txt"
            filen = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            filen1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\nameStrip.txt"
            fileq = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            fileq1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantityStrip.txt"
            filep = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            filep1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\priceStrip.txt"
            
            ##--- NAME
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(filen) as infile, open(filen1, 'w') as outfile:
                for line1 in infile:
                    if not line1.strip(): continue  # skip the empty line
                    outfile.write(line1)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileA = open(filen1, 'rb')

            fileB = open(filen, 'wb')
            ##print("writing..")
            shutil.copyfileobj(fileA, fileB)
            ##print("done with name.")                        
            ##--- END
            
            
            ##--- Quantity
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(fileq) as infileq, open(fileq1, 'w') as outfileq:
                for lineq in infileq:
                    if not lineq.strip(): continue  # skip the empty line
                    outfileq.write(lineq)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileC = open(fileq1, 'rb')

            fileD = open(fileq, 'wb')
            ##print("writing..")
            shutil.copyfileobj(fileC, fileD)
            ##print("done with name.")                         
            ##--- END
            
            
            ##--- PRICE
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(filep) as infilep, open(filep1, 'w') as outfilep:
                for linep in infilep:
                    if not linep.strip(): continue  # skip the empty line
                    outfilep.write(linep)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileE = open(filep1, 'rb')

            fileF = open(filep, 'wb')

            shutil.copyfileobj(fileE, fileF)            
            ##--- END
            
            
            ##--- Inventory
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(filename) as infilename, open(filename10, 'w') as outfilename:
                for linename in infilename:
                    if not linename.strip(): continue  # skip the empty line
                    outfilename.write(linename)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileG = open(filename10, 'rb')

            fileH = open(filename, 'wb')

            ##shutil.copyfileobj(fileG, fileH)
            ##--- END    
            shutil.copy2(filename10, filename)
            
            
            '''
            
            print(" ")
            print(colored("   ====================================",'green'))
            
            ##self.savingItem()
            
            print(" ")
            print("   The item '", Style.BRIGHT+colored(newItem,'yellow'),"' with the quantity \n   of '",colored(newQuantity,'cyan'),"' and with the price of '",Style.BRIGHT+colored(newPS,'red'),"'\n   has been added succesfully.")
            print(" ")
            print(colored("   ====================================",'green'))
            print(Style.BRIGHT+colored("       Press [ENTER] key to Continue...",'green'), end='')
            ui = input()
            os.system('cls')
            '''
            self.itemreader=0
            self.itemreadlimit=20
            self.num=1
            self.itemAddNumPage=1
            '''
            self.menu()
        else:
            print("Error A2")

    def deleteItem(self):
        self.itemReaderforVI()
        selectDI = ch1
        if selectDI == 9:
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            print("                Delete Item")
            print(" ")
            print(colored("   ====================================",'green'))
            print(" ")
            
            filename = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventory.txt"
            filename1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\inventoryStrip.txt"
            filen = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\name.txt"
            filen1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\nameStrip.txt"
            fileq = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantity.txt"
            fileq1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\quantityStrip.txt"
            filep = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\price.txt"
            filep1 = "D:\\Users\\asus\\Desktop\\Files\\Works\\python\\Art and Craft Inventory System\\files\\inventory\\priceStrip.txt"
            deleteloop = 1
            while deleteloop !=2:
                print(Style.BRIGHT+colored("      Item Number '(#)': ", 'grey'), end='')
                itemNumberDel = input()
                
                if (itemNumberDel.isdigit()):
                    if "." in itemNumberDel:
                        print("   ")
                        print(" Select the item number beside the item name without a decimal.")
                        print("   ")
                        deleteloop=1
                    elif int(itemNumberDel) > int(self.itemreadlimit) :
                        print("   ")
                        print(" Sorry, that item number is not listed.")
                        print("   ")
                        deleteloop=1
                    else:
                        intItemNumberDel = int(itemNumberDel) - 1
                        ##print(intItemNumber) --- For Checking
                        
                        itemOpenN = open(filen, 'r')
                        itemOpenQ = open(fileq, 'r')
                        itemOpenP = open(filep, 'r')
                        itemReadN = itemOpenN.readlines()
                        itemReadQ = itemOpenQ.readlines()
                        itemReadP = itemOpenP.readlines()
                        
                        deleteloop=2
                else:
                    print("   ")
                    print(" Select the item number you want to delete beside the item name.")
                    print("   ")
                    deleteloop=1
            
            
                        
                        
            print("   ")
            print(colored("      The Item ", 'yellow'), end='')
            print(itemReadN[intItemNumberDel], end='')
            print(colored("      With the Quantity of ", 'cyan'), end='')
            print(itemReadQ[intItemNumberDel], end='')
            print(colored("      and with the Price of ", 'red'), end='')
            print(itemReadP[intItemNumberDel], end='')
            print("   ")
            print(colored("   Successfully deleted!", 'red'))
            
            
            ##Turn of the Name
            
            
            ##--- Start of deleting item
            with open(filen, 'r') as fileDel1:
                itemsn = fileDel1.readlines()
            
            
            itemsn[intItemNumberDel] = "\n"
            
            with open(filen, 'w') as file01:
                file01.writelines(itemsn)
                file01.close()
            ##--- END
            
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(filen) as infile, open(filen1, 'w') as outfile:
                for line1 in infile:
                    if not line1.strip(): continue  # skip the empty line
                    outfile.write(line1)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileA = open(filen1, 'rb')

            fileB = open(filen, 'wb')
            ##print("writing..")
            ##shutil.copyfileobj(fileA, fileB)
            ##print("done with name.")                        
            ##--- END
            shutil.copy2(filen1, filen)
            
            with open(filen) as f_nIn:
                dataN = f_nIn.read().rstrip('\n')

            with open(filen, 'w') as f_Nout:    
                f_Nout.write(dataN)
            
            
            ##Turn of the Quantity
            
            
            ##--- Start of deleting item
            with open(fileq, 'r') as fileDelq:
                itemsq = fileDelq.readlines()
            
            
            itemsq[intItemNumberDel] = "\n"
            
            with open(fileq, 'w') as fileDelq1:
                fileDelq1.writelines(itemsq)
                fileDelq1.close()
            ##--- END
            
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(fileq) as infileq, open(fileq1, 'w') as outfileq:
                for lineq in infileq:
                    if not lineq.strip(): continue  # skip the empty line
                    outfileq.write(lineq)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileC = open(fileq1, 'rb')

            fileD = open(fileq, 'wb')
            ##print("writing..")
            ##shutil.copyfileobj(fileC, fileD)
            ##print("done with name.")                         
            ##--- END
            shutil.copy2(fileq1, fileq)
            with open(fileq) as f_qIn:
                dataQ = f_qIn.read().rstrip('\n')

            with open(fileq, 'w') as f_Qout:    
                f_Qout.write(dataQ)
            
            
            
            ##Turn of the Price
            
            
            ##--- Start of deleting item
            with open(filep, 'r') as fileDelp:
                itemsp = fileDelp.readlines()
            
            
            itemsp[intItemNumberDel] = "\n"
            
            with open(filep, 'w') as fileDelp1:
                fileDelp1.writelines(itemsp)
                fileDelp1.close()
            ##--- END
            
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(filep) as infilep, open(filep1, 'w') as outfilep:
                for linep in infilep:
                    if not linep.strip(): continue  # skip the empty line
                    outfilep.write(linep)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileE = open(filep1, 'rb')

            fileF = open(filep, 'wb')

            ##shutil.copyfileobj(fileE, fileF)  
            shutil.copy2(filep1, filep)            
            ##--- END
            with open(filep) as f_pIn:
                dataP = f_pIn.read().rstrip('\n')

            with open(filep, 'w') as f_Pout:    
                f_Pout.write(dataP)
            
            
            
            ##Turn of the Inventory
            
            
            ##--- Start of deleting item
            with open(filename, 'r') as fileDelname:
                itemsname = fileDelname.readlines()
            
            
            itemsname[intItemNumberDel] = "\n"
            
            with open(filename, 'w') as fileDelname1:
                fileDelname1.writelines(itemsname)
                fileDelname1.close()
            ##--- END
            
            ##--- Start of removing blank lines and creating a new Clean file without blanklines
            with open(filename) as infilename, open(filename1, 'w') as outfilename:
                for linename in infilename:
                    if not linename.strip(): continue  # skip the empty line
                    outfilename.write(linename)
            ##--- END

            ##--- Start of copying the temporary clean file to the original file
            fileG = open(filename1, 'rb')

            fileH = open(filename, 'wb')

            ##shutil.copyfileobj(fileG, fileH)
            ##--- END    
            shutil.copy2(filename1, filename)
            
            with open(filename) as f_nameIn:
                dataname = f_nameIn.read().rstrip('\n')

            with open(filename, 'w') as f_nameout:    
                f_nameout.write(dataname)
            
                
               
            self.itemreader=0
            self.itemreadlimit=20
            self.num=1
            self.itemAddNumPage=1
            print(" ")
            print(Style.BRIGHT+colored("       Press [ENTER] key to Continue...",'green'), end='')
            ui = input()
            
            os.system('cls')
            
            self.menu()
                
    def modifyItem(self):
        self.itemReaderforVI()
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
                    if int(itemNumber) > int(self.itemreadlimit):
                        print("   ")
                        print(" Sorry, that item number is not listed.")
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
            
            self.itemreader=0
            self.itemreadlimit=20
            self.num=1
            self.itemAddNumPage=1
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
        print(" ")
        print("               5 | Log Out")
        print(" ")
        print(colored("   ====================================",'green'))
        print(" ")
        
        self.choice()

    def loginmenu(self):
        ##tprint("Arts & Craft")
        ##tprint("Inventory System ")
        ##print('\U0001F600	')
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
