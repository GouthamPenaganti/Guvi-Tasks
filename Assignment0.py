import json
import os
import re

filename = "Goutham.txt"


def PasswordCheck(password):
  pattern = "^.*(?=.{6,15})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
  result = re.findall(pattern, password)
  if (result):
    return True
  else:
    print("Password not valid")
    return False



def Validate(email):
  #Special characters aren't added as its not mentioned in the problem statement
  regex = '^[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
  if (re.search(regex, email)):
    print("Valid Email")
    return True
  else:
    print("Invalid Email")
    return False

def ForgotPassword():
  Forgotpass_Email=input("Enter your email ")
  f=open(filename,"r")
  filecontents=f.read()
  x=json.loads(filecontents)
  f.close()
  if(Forgotpass_Email in x.keys()):
    print(x[Forgotpass_Email])
  else:
    print("Go and Register")


def Login():
  Login_Email = input("Enter your login email ")

  f = open(filename, "r")
  filecontents = f.read()
  x = json.loads(filecontents)
  f.close()
  if (Login_Email not in x.keys()):
    print("Go and Register!")
    Register()
  else:
    Login_Password = input("Enter your login password ")
    if (x[Login_Email] == Login_Password):
      print("Login Successfull")
    else:
      print("Forgot Password? Retrieve here")
      ForgotPassword()


def Register():
  Name = input("Enter your Name ")
  EmailID = input("Enter your email ")
  if (Validate(EmailID)):
    Password = input("Enter your password")
    PasswordCheck(Password)
  else:
    print("Try Again!")

  if (PasswordCheck(Password)):
    email_pass_Dict = {EmailID: Password}
    if (os.stat(filename).st_size == 0):
      f = open(filename, "w")
      f.write(json.dumps(email_pass_Dict))
      f.close()
      print("Registration Successful")
    else:

      f = open(filename, "r")
      filecontents = f.read()
      x = json.loads(filecontents)
      f.close()
      x.update(email_pass_Dict)
      f = open(filename, "w")
      f.write(json.dumps(x))
      f.close()
      print("Registration Successful")


print("Enter 1 to Register")
print("Enter 2 to Login")
user_input=int(input())
if(user_input==1):
  print("Register")
  Register()
elif(user_input==2):
  print("Login")
  Login()
else:
  print("Invalid input")

