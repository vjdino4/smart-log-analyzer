""" print("Hello Vijaya")
print(5+7)
a=3
print("a")
print(a)
name = "Vijay"
name1 = "SHREE RAM"
attempts = 5
print(name, attempts)
print(a, name1, attempts)
----

number= 2
if number > 3:
    print("ALERT!!!")
else:
    print("ALL OKAY... GO ON")
    
----
No1 = 15
if No1 < 10:
    print("HELLO PYTHON")
else:
    print("ARE YOU REALLY SECURE")
----

for i in range(5):
    print(i)
    
fruits=["apple", "banana", "orange", "cherry"]
for fruit in fruits:
    print(fruit)
----

for letter in "python":
    print(letter)
----

dict= {'1':'vij', '2':'san', '3':'ran'}
for key, value in dict.items():
    print(f"Key: {key}, Value:{value}")
    
----
name = input("Enter your name here:")
print("HELLO,",name,"!WELCOME!")


----
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for ip in ips:
    print(ip)


vj= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for n in vj:
    if n>=18:
        print("ALERT:", n)


attempts=[1,20,5,3,7,1]
for i in attempts:
    if i>=5:
        print("Suspicious attempts detected:", i)
        
"""

#ips=["192.168.1.10","192.168.1.20","192.168.1.30"]
#print(ips[0])
#print(ips[1])
#print(ips[2])

"""
for ip in ips:
 print(ip)

ips=[]
ips.append("192.168.0.10")
ips.append("192.168.0.20")
print(ips)


a=[1,2,3,4,5]
for a in a:
    if a<=2:
        print("🚨 Suspicious attempt:", a)
              
"""

failed_ips={
    "192.168.1.10": 3,
    "192.168.1.20":1
    }

"""
print(failed_ips["192.168.1.10"])

failed_ips={}

failed_ips["192.168.1.30"]=1
failed_ips["192.168.1.40"]=5

print(failed_ips)


ips={}

ip="192.168.0.10"

if ip in ips:
    ips[ip] +=1
else:
    ips[ip] =1

print(ips)
        
"""

for ip in failed_ips:
    if failed_ips[ip]>=3:
        print("🚨 Suspicious IP:", ip)
