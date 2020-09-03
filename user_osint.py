import os

token=0
#Sherlock and crunch for user enum
os.system("python3 /bin/cupp.py -i ")
filename= input("Tell the File Name (with or without extension!)> ")
if ".txt" in filename:
    token+=1
else:
    filename= filename+".txt"
with open(filename,"rb") as f:
    z = f.readlines()

print("Checking ")
for i in z:
    os.system(f"python3 /bin/sherlock/sherlock.py {i}")

#move the results
os.system("mkdir results")
for i in z:
    i = i+".txt"
    os.system(f"mv {i} /root/sec/github/Osint_Scripts/results/")

#list valid results
os.chdir("/root/sec/github/Osint_Scripts/results/")
l =  os.walk("."):
l = list(l)
d = list(l[0])
leng = len(d[2])
for i in range(leng):
    os.system("cat "+ i)
#     os.system("cat "+i+" | grep -v 'Error Connecting' | grep -v ''")