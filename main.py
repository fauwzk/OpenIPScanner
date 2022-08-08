import sys, ipaddress, rich, socket, os, json
from pythonping import ping

def clear_screen():
	if(os.name == 'posix'):
		os.system('clear')
	else:
		os.system('cls')

def set_testports(port):
	global ports
	if type(port) == list:
		ports = port
	else:
		ports = port.split(" ")

def set_iptimeout(ip):
	global ip_timeout
	ip_timeout = float(ip)

def set_porttimeout(port):
	global port_timeout
	port_timeout = float(port)

def set_showfail(show_fail):
	global showfail
	showfail = str(show_fail)

def helper(zone):
	if zone == 'main':
		print("todo")
	elif zone == 'ip':
		print("todo")
	elif zone == 'ports':
		print("todo")
	elif zone == 'settings':
		print("todo")
	else:
		print(f'Unknown menu: {zone}')

def load_defaults_settings():
	global defaults_ports
	defaults_ports = [22, 443, 25565, 80]
	set_iptimeout(0.1)
	set_porttimeout(0.1)
	set_showfail("False")
	set_testports(defaults_ports)

def load_settings():
	global settings_filename; settings_filename = 'settings.json'
	try:
		with open(settings_filename, 'r') as savefile:
			save_json = json.load(savefile)
			print(save_json)
			set_testports(save_json["ports"])
			set_iptimeout(save_json["ip_timeout"])
			set_porttimeout(save_json["port_timeout"])
			set_showfail(save_json["showfail"])
	except Exception as e:
		print(f"{settings_filename} does not exist.\nLoading defaults")
		load_defaults_settings()

clear_screen()
load_settings()
print("\n")

def test_ip(addressMin, addressMax, showFail):
	global workingip_list, notworkingip_list, totalAddress
	workingip_list = []
	notworkingip_list = []
	totalAddress = int(ipaddress.IPv4Address(str(addressMax))) - int(ipaddress.IPv4Address(str(addressMin)))
	ipEnd = 0
	while totalAddress >= ipEnd:
		ip = ipaddress.IPv4Address(int(ipaddress.IPv4Address(addressMin)) + ipEnd)
		ipEnd += 1
		ip_test = ping(str(ip), count=1, timeout=ip_timeout)
		if ip_test.success() == True:
			rich.print(f"Working: [green]{ip}[/green] ip: [blue]{ip_test.rtt_avg_ms}[/blue] ms")
			workingip_list.append(str(ip))
		else:
			if showFail == "True":
				rich.print(f"Not working: [bold red]{ip}[/bold red]")
			else:
				notworkingip_list.append(str(ip))
	print("")

def test_port(ips, ports, showFail):
	if type(ips) == list and len(ips) != 0:
		for ip in ips:
			if type(ports) == list and len(ports) != 0:
				for port in ports:
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.settimeout(port_timeout)
					try:
						sock.connect((ip, int(port)))
						sock.shutdown(2)
						print(f"{ip}:{port} is open")
					except:
						if showFail == "True":
							print(f"{ip}:{port} is not open")
						else:
							continue
			else:
				print("Error in ports list")
	else:
		print("Error in ip list")
	print("")

rich.print("|[bold]nettools[/bold] [italic]v0.1a[/italic]|")
rich.print("Type [italic]help[/italic] to begin")

while True:
	command = input("nettools> ").split(" ")
	if command[0] == "help":
		helper('main')
	elif command[0] == "ip":
		while True:
			ip_command = input("ip> ").split(" ")
			if ip_command[0] == "help":
				helper('ip')
			if ip_command[0] == "test":
				if len(ip_command) < 3:
					print("Error: Not enough arguments")
				else:
					test_ip(str(ip_command[1]), str(ip_command[2]), showfail)
			elif ip_command[0] == "show":
				rich.print(f"Working IPs ([yellow]{len(workingip_list)}/{totalAddress}[/yellow]): {workingip_list}")
			elif ip_command[0] == "clear" or ip_command[0] == "\x0c":
				clear_screen()
			elif ip_command[0] == "exit":
				break
			else:
				print(f"Unknown command: {command}")
	elif command[0] == "port":
		while True:
			port_command = input("port> ").split(" ")
			if port_command[0] == "help":
				helper('ports')
			if port_command[0] == "test":
				if port_command[1] == "working":
					try:
						test_port(workingip_list, ports, showfail)
					except NameError:
						print("Working ip list does not exist")
			elif port_command[0] == "set":
				if settings_command[2] == "defaults":
					set_testports(defaults_ports)
				elif settings_command[2] == "custom":
					set_testports(input('Enter ports with spaces: '))
				print(f"Ports set: {ports}")
			elif port_command[0] == "show":
				print(f"Test ports: {ports}")
			elif port_command[0] == "clear" or port_command[0] == "\x0c":
				clear_screen()
			elif port_command[0] == "exit":
				break
			else:
				print(f"Unknown command: {command}")
	elif command[0] == "settings":
		while True:
			settings_command = input("settings> ").split(" ")
			if settings_command[0] == "help":
				helper('settings')
			elif settings_command[0] == "show":
				print(f"Current ip timeout: {ip_timeout}")
				print(f"Current port timeout: {port_timeout}")
				print(f"Show fail: {showfail}")
				print(f"Test ports: {ports}")
			elif settings_command[0] == "set":
				if settings_command[1] == "timeout" and settings_command[2] == "ip":
					timeout = input('Enter timeout: ')
					set_iptimeout(timeout)
					print(f"ip timeout set: {ip_timeout}")
				elif settings_command[1] == "timeout" and settings_command[2] == "port":
					timeout = input('Enter timeout: ')
					set_porttimeout(timeout)
					print(f"Port timeout set: {port_timeout}")
				elif settings_command[1] == "fail":
					if settings_command[2] == "True" or settings_command[2] == "true":
						set_showfail("True")
					if settings_command[2] == "False" or settings_command[2] == "false":
						set_showfail("False")
					print(f"Set show fail: {showfail}")
				# elif settings_command[1] == "ports":
				# 	if settings_command[2] == "defaults":
				# 		set_testports(defaults_ports)
				# 	elif settings_command[2] == "custom":
				# 		set_testports(input('Enter ports with spaces: '))
				# 	print(f"Ports set: {ports}")
			elif settings_command[0] == "save":
				save_data = {"ip_timeout":ip_timeout, "port_timeout":port_timeout, "showfail":showfail, "testlmports":ports}
				save_json = json.dumps(save_data, indent=4)
				print(save_json)
				with open(settings_filename, "w") as savefile:
					savefile.write(save_json)
			elif settings_command[0] == "load":
				load_settings()
				# defaults_ports = [22, 443, 25565, 80]
				# set_iptimeout(0.1)
				# set_porttimeout(0.1)
				# set_showfail("False")
				# set_testports(defaults_ports)
			elif settings_command[0] == "defaults":
				load_defaults_settings()
			elif settings_command[0] == "clear" or settings_command[0] == "\x0c":
				clear_screen()
			elif settings_command[0] == "exit":
				break
			else:
				print(f"Unknown command: {command}")
	elif command[0] == "clear" or command[0] == "\x0c":
		clear_screen()
	elif command[0] == "exit":
		sys.exit(0)
	else:
		print(f"Unknown command: {command}")