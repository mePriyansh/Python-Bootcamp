password = input('Enter the password: ')
result=[]
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit=False             #digit set as false initially
for i in password:      #check if there is a digit in the password
    if i.isdigit():
        digit=True      #if there is a digit, digit is set to True

result.append(digit)    #append the result to the list

upper=False             #upper set as false initially
for i in password:      #check if there is an uppercase letter in the password
    if i.isupper():
        upper=True      #if there is an uppercase letter, upper is set to True
result.append(upper)    #append the result to the list

if (all(result)):       #equivalent to if(all(result)==True
    print("Strong Password")    
else:
    print("Weak Password")
