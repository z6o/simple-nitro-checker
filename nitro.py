
import random
from colorama import Fore, Back, init
import requests
import string
import os
from configparser import ConfigParser
import time

init(convert=True)


def webhook_tester():
    embed = {
        "avatar_url": f"",
        "username": "webhook-tester",
        "content": "@everyone",
        "embeds": [
            {
                "author": {
                    "name": "webhook-tester",
                    "url": "",
                    "icon_url": f""
                },
                "description": f"Webhook working",
                "color": 0x000000,
                "footer": {
                    "text": "Made by github.com/z6o"
                }
            }
        ]
    }
    requests.post(webhook, json=embed)

def valid_nitro():
    embed = {
        "avatar_url": f"https://cdn.tech-latest.com/wp-content/uploads/2022/01/Discord-Nitro-vs-Nitro-Classic.jpeg",
        "username": "nitro generator + checker",
        "content": "",
        "embeds": [
            {
                "author": {
                    "name": "nitro generator + checker",
                    "url": "",
                    "icon_url": f"https://cdn.tech-latest.com/wp-content/uploads/2022/01/Discord-Nitro-vs-Nitro-Classic.jpeg"
                },
                "description": f"Valid nitro code:\ndiscord.gift/{nitro_code}",
                "color": 0x000000,
                "footer": {
                    "text": "Made by github.com/z6o"
                }
            }
        ]
    }
    requests.post(webhook2, json=embed)

def invalid_nitro():
    embed = {
        "avatar_url": f"https://cdn.tech-latest.com/wp-content/uploads/2022/01/Discord-Nitro-vs-Nitro-Classic.jpeg",
        "username": "nitro generator + checker",
        "content": f"discord.gift/{nitro_code}",
        
    }
    requests.post(webhook, json=embed)

proxies = open("./proxies.txt").read().splitlines()
print(f'{Fore.YELLOW}[INFO]{Fore.RESET} Scraping proxies...')
f = open("./proxies.txt", "a+")
r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
for proxy in r.text.split("\n"):
    proxy = proxy.strip()
    if proxy:
        f.write(str(proxy)+"\n")
os.system('cls||clear')
logo = f'''{Fore.BLUE}
       .__  __                 
  ____ |__|/  |________  ____  
 /    \|  \   __\_  __ \/  _ \ 
|   |  \  ||  |  |  | \(  <_> )
|___|  /__||__|  |__|   \____/ 
     \/                        
{Fore.RESET}
'''
print(f'{Back.YELLOW}[INFO]{Back.RESET}{Fore.CYAN} Reading config file...{Fore.RESET}\n')
file = 'config.ini'
config = ConfigParser()
config.read(file)
webhook = config['webhook']['webhook_url']
webhook2 = config['webhook']['webhook_for_invalid_codes']
invaled_codes = config['webhook']['invalid_codes']
hits = config['hits-file']['hits_file']
print(f'{Back.GREEN}[SUCCESS]{Back.RESET}{Fore.CYAN} Readed config file.{Fore.RESET}\n')
print(f'{Back.GREEN}[SUCCESS]{Back.RESET}{Fore.CYAN} Founded a webhook.{Fore.RESET}\n')
print(f'{Back.YELLOW}[INFO]{Back.RESET}{Fore.CYAN} Testing webhook...{Fore.RESET}\n')
webhook_tester()
os.system("cls||clear")
print(f'{logo}\n{Fore.CYAN}[1]{Fore.RESET} - {Fore.CYAN}Nitro code checker with proxies. [2]{Fore.RESET} - {Fore.CYAN}Nitro code checker without proxies.{Fore.RESET}')
init(convert=True)
answer = input(f'> ')
if answer == "2":
    while True:
        nitro_code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print(f"{Fore.GREEN}[VALID] discord.gift/{nitro_code}")
            valid_nitro()
            if hits == "True":
                file = open('hits.txt',"w")
                file.write(nitro_code)
        else:
            print(f"{Fore.RED}[INVALID] discord.gift/{nitro_code}")
            
if answer == "1":
    while True:
        nitro_code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true", proxies={"http": 'http://' + random.choice(proxies)})
        if r.status_code == 200:
            print(f"{Fore.GREEN}[VALID] discord.gift/{nitro_code} {Fore.RESET}")
            valid_nitro()
            if hits == "True":
                file = open('hits.txt',"w")
                file.write(nitro_code)
        else:
            print(f"{Fore.RED}[INVALID] discord.gift/{nitro_code} {Fore.RESET}")
            if invalid_codes == "True":
                invalid_nitro()
            
                

       
