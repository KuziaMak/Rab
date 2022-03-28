import locale
import platform
import subprocess
from ipaddress import ip_address
from tabulate import tabulate

def host_ping(listInt):
    masR = []
    masU = []
    for ip in listInt:
        reply = subprocess.run(['ping', '-n', '1','-w','1',  ip], stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        if reply.returncode == 0:
            masR.append(ip)
        else:
            masU.append(ip)
    return tabulate({"Reachable":masR,"Unreachable":masU}, headers='keys')

def host_range_ping(start, end):
    sta = ip_address(start)
    en = ip_address(end)
    dip = int(en) - int(sta)
    return  host_ping([str(sta+x) for x in range(0,dip+1) ])

def  host_range_ping_tab(start, end):
    return host_range_ping(start, end)
if  __name__ == "__main__":
    print(host_ping(['yandex.ru','8.8.8.0']))
    print(host_range_ping("8.8.8.0", "8.8.8.8"))
    print( host_range_ping_tab("8.8.8.9", "8.8.8.20"))