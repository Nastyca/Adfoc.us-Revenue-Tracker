import os
import requests

from time import sleep
from colorama import Fore, init

os.system("cls")

print(f"")

cookie = "YOUR_COOKIE"

while True:
    try:
        headers = {"Host": "adfoc.us",
                    "Cookie": f"phpsessionname={cookie}",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36"',
                    "Accept-Encoding": "gzip, deflate, br"}
    
        requete = requests.get("https://adfoc.us/links?_=1734846862800", headers=headers)
        data = requete.json()

        nombre = data["iTotalRecords"]

        for record in data["aaData"]:
            lien = record[0]
            euros = record[4]
            date = record[5]
            print(f"{Fore.BLUE}Lien : {Fore.RESET}{lien} {Fore.GREEN}| {Fore.BLUE}Argent : {Fore.RESET}{euros} {Fore.GREEN}| {Fore.BLUE}Date : {Fore.RESET}{date}")
        
        print(f"\n{Fore.RESET}-------------------------------------------------------------------------------------\n")
    except:
        pass

    sleep(10)
