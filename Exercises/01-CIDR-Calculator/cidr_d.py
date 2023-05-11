ipVersion=input("Which IP-Family do you want to have? [4/6]")
print('The IP version was: ', ipVersion)

cidr = input('What is the CIDR?: ') # <--- 10.0.0.0/16
ip,cidr=cidr.split('/')[0],int(cidr.split('/')[1])
print('The choosen CIDR was: ', cidr)

ip4_check= lambda ip,cidr: len(ip.split('.'))==4 & cidr<=32
ip6_check= lambda cidr: cidr<=128


x=32-cidr #<--- IPv6
number_of_ips = 2**x
print(number_of_ips)

def ipdestruct(ip):
    n=ip.split('.')
    m=0
    for x in n:
        m*=256
        m+=int(x)
    return m

def ipconstruct(num):
    ip=''
    ipl=[]
    for x in range(4):
        m=num%256
        ipl.append(m)
        num=num//256
    for x in range(4):
        if x!=0:
            ip=ip+'.'
        ip=ip+str(ipl[-1-x])
    return ip

print('first ip adress: ',ip)
m=ipdestruct(ip)
ip2=ipconstruct(m+number_of_ips-1)
print('last ip adress: ',ip2)