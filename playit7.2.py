import subprocess
import platform
import os
import sys
from colorama import init, Fore, Style
import keyboard
import time
import re

init(autoreset=True)

def title():
    if platform.system().lower() == 'Windows':
        os.system(f"title PLAYIT.GG")
    else:
        sys.stdout.write(f"\x1b]2;PLAYIT.GG\x07")
        sys.stdout.flush()
title()

def cls():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)

def ping_ip(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, _ = process.communicate()    
    if process.returncode == 0:
        match = re.search(r'(\d+[,.]?\d*)ms', stdout)
        latency = match.group(1).replace(',', '.') if match else "N/A"
        return True, latency
    else:
        return False, "N/A"

    
api_server = 'api.playit.gg'
debug_ip = '147.185.221.1'
datacenters = ['control.los.ply.gg','control.sea.ply.gg','control.dal.ply.gg','control.mia.ply.gg','control.chi.ply.gg','control.jer.ply.gg','control.tor.ply.gg','control.mex.ply.gg','control.sao.ply.gg','control.esp.ply.gg','control.gbr.ply.gg','control.deu.ply.gg','control.pol.ply.gg','control.swe.ply.gg','control.del.ply.gg','control.mum.ply.gg','control.ban.ply.gg','control.sgp.ply.gg','control.tok.ply.gg','control.syd.ply.gg','control.san.ply.gg','control.isr.ply.gg',]
datacenter_regions = {
    'los': 'us-la',
    'sea': 'us-seattle',
    'dal': 'us-dallas',
    'mia': 'us-miami',
    'chi': 'us-chicago',
    'jer': 'us-new-jersey',
    'tor': 'ca-toronto',
    'mex': 'mexico',
    'sao': 'bra-sao-paulo',
    'esp': 'spain',
    'gbr': 'london',
    'deu': 'germany',
    'pol': 'poland',
    'swe': 'sweden',
    'del': 'in-delhi',
    'mum': 'in-mumbai',
    'ban': 'in-bangalore',
    'sgp': 'singapore',
    'tok': 'tokyo',
    'syd': 'sydney',
    'san': 'santiago',
    'isr': 'israel',
}
terminal_width = 120
def wait_or_interrupt(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        if keyboard.is_pressed('r'):
            return True
        time.sleep(0.1)
    return False

while True:
    cls()
    print(f"\n Unofficial {Fore.YELLOW}Playit{Fore.CYAN}.gg{Style.RESET_ALL} Datacenter checker\n")
    print(" Checking..")
    status_api, latency_api = ping_ip(api_server)
    if status_api:
        print(f"  {Fore.YELLOW}api{Style.RESET_ALL}.playit.gg: {Fore.GREEN}Online{Style.RESET_ALL}" + (f" ({latency_api}ms)" if latency_api != "N/A" else " (N/A)"))
    else:
        print(f"  {Fore.YELLOW}api{Style.RESET_ALL}.playit.gg: {Fore.RED}Offline{Style.RESET_ALL}")

    status_debug_ip, latency_debug = ping_ip(debug_ip)
    isp_error = " (Your ISP might be blocking Playit's IPs!)" if not status_debug_ip else ""
    debug_1part = f"  {Fore.YELLOW}Debug.{Style.RESET_ALL}IP: "
    if status_debug_ip:
        status = f"{Fore.GREEN}Online{Style.RESET_ALL}"
        latency = f" ({latency_debug}ms)" if latency_debug != "N/A" else " (N/A)"
    else:
        status = f"{Fore.RED}Offline{Style.RESET_ALL}"
        latency = ""
    padding = ' ' * ((terminal_width - len("Datacenter Map List")) // 3)
    final_message = f"{debug_1part}{status}{latency}{padding}           Datacenter Map List"
    print(final_message)
    if not status_debug_ip:
        print(f"  {Fore.RED}{isp_error}")
    #Gonna be honest, ChatGPT kind of helped me formatting this text.
    #Thanks you Maxomatic458 for the datacenter list, without it, this could've not be possible
    print(f"{padding}{Fore.LIGHTBLACK_EX}                                    Thanks to Maxomatic458 for the Datacenter List")


    for ip in datacenters:
        if keyboard.is_pressed('r'):
            break

        address = ip.split('.')
        a = address[1]
        r = datacenter_regions.get(a, "unknown region")
        b = '.'.join(address[2:])
        status, latency = ping_ip(ip)
        subdmin = f"{Fore.YELLOW}{a}{Style.RESET_ALL}"
        ll = len(str(latency))
        if ll == 1:
            s = '  '
        elif ll == 2:
            s = ' '
        elif ll == 3:
            s = ''
        else:
            s = ''
        if status:
            reslt = f"{Fore.GREEN}Online{Style.RESET_ALL} ({latency}ms)" if latency != "N/A" else f"{Fore.GREEN}Online{Style.RESET_ALL} (N/A)"
            dcrn = f"{' ' * ((terminal_width - len(f'{address[0]}.{address[1]}: {reslt}')) // 3)}{s}    |{r}"
        else:
            reslt = f"{Fore.RED}Offline{Style.RESET_ALL}"
            dcrn = f"{' ' * ((terminal_width - len(f'{address[0]}.{address[1]}: {reslt}')) // 3)}{s}    |{r}"
        print(f"  {address[0]}.{subdmin}.{b}: {reslt} {dcrn}")

    if keyboard.is_pressed('r'):
        continue

    if wait_or_interrupt(300):
        continue
