import openipscanner

""" addressMin = int(ipaddress.IPv4Address(str(input("address min: "))))
addressMax = int(ipaddress.IPv4Address(str(input("address max: ")))) """

addressMin = "192.168.80.1"
addressMax = "192.168.80.128"
port = 21

openipscanner.run(addressMin, addressMax, port)

print(f"Working IPs ({len(openipscanner.workingip_list)}/{openipscanner.totalAddress}): {openipscanner.workingip_list}")