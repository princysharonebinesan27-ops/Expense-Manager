print("\n=======EXPENSE MANAGER==========\n")#displaying the title "EXPENSE MANAGER" 
monthly=int(input("\nEnter monthly budget:"))#to get  monthly budget as  an input value from the user
expense1=int(input("\nEnter Expense:"))#to get expense1 amount as an input value from the user
category1=input("\nEnter Expense Category:")#to get the expense category1 from user
expense2=int(input("\nEnter Expense:"))#to get expense2 amount as an input value from the user
category2=input("\nEnter Expense Category:")#to get the expense category2 from user
expense3=int(input("\nEnter Expense:"))#to get expense3 amount as an input value from the user
category3=input("\nEnter Expense Category:")#to get the expense category3 from user
print("\n--------------------------------------------------")
total_expense=expense1+expense2+expense3#getting the total_expense by adding all 3 expense amounts
print("\ntotal_expense:",total_expense)#displaying the total_expense
Remaining=monthly-total_expense#getting the remaining by subtracting monthly amount by total_expense
print("\nRemaining:",Remaining)#displaying the remaining amount
print("\n------------------------------------------------")
print("status:within Budget")#displaying the status as within budget





print("\n==========SECURE LOGIN SYSTEM==========\n")#displaying the title "secure login system"
user=input("\nEnter Username:")#to get  username from user 
pw=int(input("\nenter password:"))#to get password from user
password=123#assinging the password
if pw == password:#assinging the password to the variable name "pw"
    print("\nLogin Credentials Verified!")#displaying login credentials verified
else:#using else part to declare the alternate output
    print("\ninvalid password")#displaying invalid password when wrong password is given by the user
otp=583214#assinging the otp number
attempts=3#assinging the number of attempts
for i in range(attempts):#using for loop to use the 3 attempts
    user_otp=int(input("\nenter the otp:"))#to get user_otp from user
    if user_otp==otp:#using if statement to check the correct otp
        print("\nOTP verification successful!")#displaying otp verification successful when the otp is correct
        break
    else:#using else part to declare the alternate output
        print("\ninvalid otp")#displaying that the otp is wrong
        if i < attempts -1:#assigning the condition for continuos loop
            print("\ntry again")#displaying try again for wrong otp    
        else:#using else part to declare the alternate output
            print("access denied")#displaying that the entered otp is wrong
            print("\n=================================")
            print("\nLOGIN SUCCESSFUL")#displaying login successful
            print("\n=================================")














































