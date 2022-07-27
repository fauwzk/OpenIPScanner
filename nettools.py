from pythonping import ping
import ipaddress
import rich 

def test_ip(addressMin, addressMax, showfail):
	global workingip_list, notworkingip_list, totalAddress
	workingip_list = []
	notworkingip_list = []
	totalAddress = int(ipaddress.IPv4Address(str(addressMax))) - int(ipaddress.IPv4Address(str(addressMin)))
	ipEnd = 0
	while totalAddress >= ipEnd:
		ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(addressMin)) + ipEnd)
		ipEnd += 1
		a = ping(str(ip), count=1, timeout=0.25)
		if a.success() == True:
			rich.print(f"Work: [green]{ip}[/green] Ping: [blue]{a.rtt_avg_ms}[/blue] ms")
			workingip_list.append(str(ip))
		else:
			if showfail == True:
				rich.print(f"Not working: [bold red]{ip}[/bold red]", end="\r")
			notworkingip_list.append(str(ip))