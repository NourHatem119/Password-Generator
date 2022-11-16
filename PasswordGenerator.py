#Password_Generator
import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%*/£"
Use_for = lowerCase + upperCase + number + symbols
length_for_pass = 12
password = "".join(random.sample(Use_for, length_for_pass))
print("Pass is: " + password)