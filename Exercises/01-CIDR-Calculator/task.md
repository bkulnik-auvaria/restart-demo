## Example: CIDR Subnet Calculator

Make a python program that calculates the number of ip addresses for a subnet.

It should work like this: 

- The program starts and should ask the user for IP family (4 or 6)
- The program then asks for the CIDR number (so '/16' part of 10.0.0.0/16)
- The program prints the answer and terminates

_Hint_:

x=32-cidr_number (ip4)
x=128-cidr_number (ip6)
number_of_ip_adresses 2**x