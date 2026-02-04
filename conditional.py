#guessing game
secret_num=8
num=int(input("Guess the number:"))
if num>secret_num:
    print("Too high")
elif num<secret_num:
    print("Too low")
else:
    print("Your guessed the correct number")
    
#Week day
week_day=int(input("Enter a number(1 to 7):"))
if week_day==1:
    print("Monday")
elif week_day==2:
    print("Tuesday")
elif week_day==7:
    print("Sunday")
elif week_day==3:
    print("Wednesday")
elif week_day==4:
    print("Thursday")
elif week_day==5:
    print("Friday")
elif week_day==6:
    print("Saturday")
else:
    print("you entered invalid number")

#discount amount
amount=float(input("Enter the amount:"))
if amount>100:
    discount=amount * 0.10
elif amount>50:
    discount=amount * 0.5
else:
    discount=0
final_amount=amount-discount
print("Final amount is",final_amount)

#checking credentials
valid_username="Akhila"
valid_password="Akks"
username=input("Enter the name:")
password=input("Enter the password:")

if username==valid_username:
    if password==valid_password:
        print("Password is correct")
    else:
        print("password is not valid")
else:
    print("USername is correct")