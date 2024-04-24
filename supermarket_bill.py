import time
k=time.asctime(time.localtime(time.time()))


name=input("Enter your name:")
lists='''
RICE           RS  25/kg
WHEAT FLOUR    RS  70/kg
RAGI FLOUR     RS  55/kg
OIL            RS  110/L
PEARS SOAP     RS  45/P
COLGATE PASTE  RS  30/P
'''
price=0                                #declaration
pricelist=[]
total_price=0
final_price=0
ilist=[]
qlist=[]
plist=[]

items={'RICE':25,'WHEAT FLOUR':70,'RAGI FLOUR':55,'OIL':110,'PEARS SOAP':45,'COLGATE PASTE':30}
option=int(input("for list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    user_input=int(input("if you want to buy press 1or 2 for exit:" ))    
    if user_input==2:
        break
    if user_input==1:
        item=input("Enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            total_price+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(total_price*5)/100
            final_price=gst+total_price
        else:
            print("SORRY YOU ENTERED ITEMS ARE NOT AVAILABLE PEASE SELECT LISTED ITEMS") 
    else:
        print("you entered wrong number")
    inp=input("CAN I BILL THE ITEMS YES OR NO:")
    if inp=='YES':
        pass
        if final_price!=0:
            print(25*'^',"NIKKAS SUPERMARKET",25*'^')
            print(30*'#',"KURNOOL",30*'#')
            print("Name:",name,25*" ","Date:",k)
            print(60*"-")
            print("s.no",8*" ",'items',8*" ","quantity",4*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*" ",ilist[i],8*" ",qlist[i],4*" ",plist[i])
            print(60*"-")  
            print(50*" ",'TOTAL_PRICE:',"RS",total_price)  
            print(50*" ","GST AMOUNT:",'rs',gst)
            print(75*"-")
            print(50*" ",'FINAL_PRICE:','RS',final_price)
            print(75*"-")
            print(50*" ","THANK YOU FOR VISITING",50*" ")  
            print(25*'^',"VISIT AGAIN",25*'^')                         