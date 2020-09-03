import os

url = input("Input the URL > ")

#dir listing
os.system(f"gobuster dir -u {url} -t 100 -w wordlist/big.txt -e php,html,sql,bak,js,txt,py")
os.system(f"gobuster dir -u {url} -t 100 -w wordlist/directory-2.3-medium.txt -e php,html,sql,bak,js,txt,py")

#subdomain
os.system(f"gobuster dns -u {url} -t 100 -w wordlist/fierce-hostlist.txt"
os.system(f"gobuster dns -u {url} -t 100 -w wordlist/subdomains-top1million-110000.txt"

#CMSeek
os.system("python3 /bin/CMSeek/cmseek.py")


#nikto 
os.system(f"nikto -h {url}")
