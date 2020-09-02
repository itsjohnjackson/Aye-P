#!/usr/bin/python3
import ipaddress
import os
import re

file_exists = 0
error_check = 0

# define our clear function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print("Use sensibly, minor error checking has been implemented.")
input("\nPress ENTER to continue.\n")
cls()
print("Script must be in the folder with relevant IP file.\nEnsure this is the folder you plan to work from." + "\n")

is_in_work_folder = input("Is this in your work folder? (y or n): ")
if is_in_work_folder.lower() == "y" or is_in_work_folder.lower() == "yes" or is_in_work_folder.lower() == "aye" or is_in_work_folder.lower() == "":
    cls()
    pass
else:
    print("Move script to relevant folder")
    exit()

print("Ensure each IP entry is on a new line in the file.\n\nAlso ensure that the following is true:\n")
print("IP address ranges/spans are presented in full.\nRanges are INCLUSIVE.\nFor example, use: 127.0.0.1-127.0.0.255\nDO NOT use: 127.0.0.1-255\n")
print("CIDR ranges are self explanatory.\n")
print("Singular ranges are self explanatory.\n")

is_ip_format_correct = input("Are the above statements true for the IP file? (y or n): ")
if is_ip_format_correct.lower() == "y" or is_ip_format_correct.lower() == "yes" or is_ip_format_correct.lower() == "aye" or is_ip_format_correct.lower() == "":
    cls()
    pass
else:
    print("Fix IP file")
    exit()

if os.path.isfile('./total-ips.txt') == True:
    print("ERROR: total-ips.txt already exists in the pwd")
    file_exists = 1
elif os.path.isfile('./total-ips2.txt') == True:
    print("ERROR: total-ips2.txt already exists in the pwd")
    file_exists = 1
else:
    pass

if file_exists == 1:
    exit()
else:
    pass

print("Here is all files within the pwd:\n")
os.system('ls -al')
with open(input("\nEnter target IP file: "),'r') as file1:
    print("")
    Lines = file1.readlines()
    # Strips the newline character
    fo = open("total-ips.txt", "a")
    for line in Lines:
        if "-" in line:
            ip_range_string = line.rstrip('\r\n')
            start, end = ip_range_string.split('-')
            try:
                ipaddress.IPv4Address(start)
                ipaddress.IPv4Address(end)
                span = list(ipaddr for ipaddr in ipaddress.summarize_address_range(ipaddress.IPv4Address(start), ipaddress.IPv4Address(end)))
                for i in span:
                    for addr in ipaddress.IPv4Network(i):
                        fo.write(str(addr) + "\n")
            except:
                print("ERROR: INVALID RANGE: " + ip_range_string)
                error_check = 1
                pass

        elif "/" in line:
            ip_cidr = line.rstrip('\r\n')
            try:
                span = list(ipaddr for ipaddr in ipaddress.ip_network(ip_cidr, False))
            except:
                print("ERROR: INVALID CIDR: " + ip_cidr)
                error_check = 1
            if error_check == 0:
                for i in span:
                    try:
                        ipaddress.IPv4Address(i)
                        for addr in ipaddress.IPv4Network(i):
                            fo.write(str(addr) + "\n")
                    except:
                        print("ERROR: INVALID CIDR: " + ip_cidr)
                        error_check = 1
                        pass
            else:
                pass
        else:
            ip_single = line.rstrip('\r\n')
            try:
                ipaddress.IPv4Address(ip_single)
                fo.write(str(ip_single) + "\n")
            except:
                print("ERROR: INVALID IP: " + ip_single)
                error_check = 1
                pass
    fo.close()

if error_check == 1:
    print("\nCleaning up and exiting due to errors highlighted above")
    os.system('rm total-ips.txt')
    exit()
else:
    pass
os.system("sort -t . -k 3,3n -k 4,4n total-ips.txt | uniq > total-ips2.txt && rm total-ips.txt && mv total-ips2.txt total-ips.txt")
print("File output with individual IP addresses to: total-ips.txt\n")
