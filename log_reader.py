
file = open("log.txt","r")
lines = file.readlines()
for line in lines:
    ip = line.strip()
    print(ip)
    
