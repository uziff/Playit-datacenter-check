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
    isp_message = " (Your ISP might be blocking Playit's IPs!)" if not status_debug_ip else ""
    if status_debug_ip:
        print(f"  {Fore.YELLOW}Debug.{Style.RESET_ALL}IP: {Fore.GREEN}Online{Style.RESET_ALL}" + (f" ({latency_debug}ms)" if latency_debug != "N/A" else " (N/A)"))
    else:
        print(f"  {Fore.YELLOW}Debug.{Style.RESET_ALL}IP: {Fore.RED}Offline{Style.RESET_ALL}{isp_message}")
    print("")

    for ip in datacenters:
        if keyboard.is_pressed('r'):
            break

        address = ip.split('.')
        a, b = address[1], '.'.join(address[2:])
        status, latency = ping_ip(ip)
        subdmin = f"{Fore.YELLOW}{a}{Style.RESET_ALL}"
        if status:
            reslt = f"{Fore.GREEN}Online{Style.RESET_ALL} ({latency}ms)" if latency != "N/A" else f"{Fore.GREEN}Online{Style.RESET_ALL} (N/A)"
        else:
            reslt = f"{Fore.RED}Offline{Style.RESET_ALL}"
        print(f"  {address[0]}.{subdmin}.{b}: {reslt}")

    if keyboard.is_pressed('r'):
        continue

    if wait_or_interrupt(300):
        continue
