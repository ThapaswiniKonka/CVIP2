import random
upper= "ABCDEFGHIJKL"
lower= "mnopqrstuvwxyz"
numbers= "1234567890"
special_char= "!@#$%^&*()"
string = upper+lower+numbers+special_char
length = 12
password = "". join(random.sample(string,length))
print("The random password generated is:", password)
