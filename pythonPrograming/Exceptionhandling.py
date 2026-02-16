# exception - runtime errors which will disrupt the normal program flow
# benefit
# prevents program crashing
# helps in debugging
#handeling errors and exceptions in the code more efficiently

# try except

# try - code to be executed
# except - exception details does not catching
#else : if the exception does not occur then else part will be executed
#finaly -mandated code
#custom exceptions


try :
    a= int (input("Enter the number"))
    b= int (input ("Enter the number"))
    print (a/b)
except ZeroDivisionError:
    print("Can not Divide by zero")
except ValueError:
    print("Please enter valid number")

#generic exception
try:
    a=10/2
except Exception as e:
    print(e)
#runs only if no exception occurs
else:
    print("Division successful")
# mandatory code
finally:
    print("close the Browser")

# custom exceptions - creating a own exception
age = int (input("Enter the age"))
if age < 18:
    raise ValueError("Age must be 18 or above")


#custome exception - creating a can exception



