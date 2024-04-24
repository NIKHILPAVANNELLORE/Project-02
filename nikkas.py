print("=====================================")
print(" ----Welcome to NIKKAS Bank----       ")
print("*************************************")
print("=<< 1. Open a new account         >>=")
print("=<< 2. Deposit Money             >>=")
print("=<< 3. WithDraw Money              >>=")
print("=<< 4. Check Customers & Balance  >>=")
print("=<< 5. Exit/Quit                  >>=")
print("*************************************")
print("To Open Your account Please Enter Your Details")
a=input("Name : ")
b=int(input("Age : "))
c=int(input("Phone Number : ")) 
print("=====PLEASE LOGIN=====")
username='nikkas'
password=1609
user_name=input("enter the username:")
pass_word=int(input("enter the password:"))
if user_name==username and pass_word==password:
    print("successfully login")
    print('''
           1.Deposit money
           2.withdraw money
           3.balance enquiry
           4.exit
''')
    amount=50000
    while True:
     num=int(input("enter the option:"))
     if num==1:
      print("Deposit money")
      dept=int(input("enter the money to deposit:"))
      amount+=dept
      print("total amount:",amount)
     elif num==2:
      print("Withdraw money")
      withdraw=int(input("enter the amount to withdraw:"))
      amount-=withdraw
      print("withdraw_amt:",withdraw) 
      remaining_amt=amount
      print("remaining_amt:",remaining_amt)
     elif num==3:
       print("balance amount:",amount)
     else:
      print("Exit\n *********Thank You Vist Again*********")     
