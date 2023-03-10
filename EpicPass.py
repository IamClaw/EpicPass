import random
import pyfiglet
from termcolor import colored
#Colours the text
design = pyfiglet.figlet_format("EpiC PasS")
coloured_design = colored(design, "red")

#Prints the designed text
print("**********************************************************")
print(coloured_design)
print("This is coded by CL4W")
print("**********************************************************")


#Variables 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols = "@#%&*-+()!':;/?"

string = lower + upper + numbers + symbols
length = 16
length_2 = 8
length_3 = 6

print("Options: ")
print("1) Password of 16 characters ")
print("2) Password of 8 characters ")
print("3) Password of 6 characters ")
print("#################")

c = int(input("Type number of any option: "))

if(c==1):
    passwd = "".join(random.sample(string,length))
    print("Your 16 character password is generated!")
    print(passwd)
elif(c==2):
    passwd2 = "".join(random.sample(string,length_2))
    print("Your 8 character password is generated!")
    print(passwd2)
elif(c==3):
    passwd3 = "".join(random.sample(string,length_3))
    print("Your 6 character password is generated!")
    print(passwd3)
else:
    print("Options not found please retry." )



