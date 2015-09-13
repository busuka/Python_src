import os

f = open("aaab.txt","w")
for val in range(1,101):
    f.write(str(val))
f.close()