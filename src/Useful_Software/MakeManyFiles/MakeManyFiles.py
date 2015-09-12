import os

for x in range(1,101):
    f_names = str(x)
    p_names = ".txt"
    os.system("date > " + f_names + p_names)
