

ipVersion = input("Which IP-Family do you want to have? [4/6]: ")
print("The IP version was: ", ipVersion)


cidr = input("What is the CIDR?: ")  # <-- 10.0.0.0/16
print("The chosen CIDR was: ", cidr)

# cidr[-2:] # Option 1: Select the last two digits -> Problem: there might be only 1 digit
splittedCidr = cidr.split("/")
firstIp = splittedCidr[0]           # 10.0.0.0
cidrRange = int(splittedCidr[1])
# firstIp, cidrRange = cidr.split("/")

def check_ip4(ip_address, cidr_range):
    condition1 = len(ip_address.split(".")) == 4
    condition2 = cidr_range >= 0 and cidr_range <= 32
    result = (condition1 and condition2)
    return result # true or false


def calculate_number_of_ips(cidr_range, ip_version):
    if ip_version == "4":
        x = 32 - cidrRange  
    else:
        x = 128 - cidrRange # <-- IPv6

    number_of_ips = 2 ** x
    return number_of_ips


validIpv4 = check_ip4(firstIp, cidrRange)
# validIpv4 = true/false
number_of_ips = calculate_number_of_ips(firstIp, cidrRange)

print("The answer is: ", number_of_ips)