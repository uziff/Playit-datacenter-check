import subprocess
import platform
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

def cls():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

def ping_ip(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

datacenters = ['control.los.ply.gg','control.sea.ply.gg','control.dal.ply.gg','control.mia.ply.gg','control.chi.ply.gg','control.jer.ply.gg','control.tor.ply.gg','control.mex.ply.gg','control.sao.ply.gg','control.esp.ply.gg','control.gbr.ply.gg','control.deu.ply.gg','control.pol.ply.gg','control.swe.ply.gg','control.del.ply.gg','control.mum.ply.gg','control.ban.ply.gg','control.sgp.ply.gg','control.tok.ply.gg','control.syd.ply.gg','control.san.ply.gg','control.isr.ply.gg',]

while True:
    cls()
    for ip in datacenters:
        address = ip.split('.')
        a = address[1]  
        b = '.'.join(address[2:])  
        status = ping_ip(ip)
        subdmin = f"{Fore.YELLOW}{a}{Style.RESET_ALL}"
        reslt = f"{Fore.GREEN}Online{Style.RESET_ALL}" if status else f"{Fore.RED}Offline{Style.RESET_ALL}"
        print(f"{address[0]}.{subdmin}.{b}: {reslt}")
    
    time.sleep(5)
