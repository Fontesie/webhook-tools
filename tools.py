import os
from random import choice
import requests
import colorama
from dhooks import Webhook
import time



os.system("title Webhook Tools")

def main():
    print(f"""{colorama.Fore.RED}
     

                                        __      __      ___.   .__                   __             ___________           .__           
                                       /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  ______ \__    ___/___   ____ |  |   ______ 
                                       \   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / /  ___/   |    | /  _ \ /  _ \|  |  /  ___/ 
                                        \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \___ \    |    |(  <_> |  <_> )  |__\___ \  
                                         \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \/____  >   |____| \____/ \____/|____/____  > 
                                              \/       \/    \/     \/                   \/     \/                                  \/ 
                                                            
                                                                            
                                                                      Webhook Tools
     """)

def nuker():
    choice1 = input(f"{colorama.Fore.BLUE}                                                                  [1] Webhook Deleter\n                                                                  [2] Webhook Sender\n                                                                  [3] Webhook Spam\n                                                                  [4] Credit\n\n{colorama.Fore.RED}                                                                  Choice: ")


    if choice1 == "1":
        os.system("cls")    
        print(f"""{colorama.Fore.RED}
     

                                        __      __      ___.   .__                   __             ___________           .__           
                                       /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  ______ \__    ___/___   ____ |  |   ______ 
                                       \   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / /  ___/   |    | /  _ \ /  _ \|  |  /  ___/ 
                                        \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \___ \    |    |(  <_> |  <_> )  |__\___ \  
                                         \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \/____  >   |____| \____/ \____/|____/____  > 
                                              \/       \/    \/     \/                   \/     \/                                  \/ 
                                                            
                                                                            
                                                                      Webhook Tools
     """)

        print(f'{colorama.Fore.BLUE}                                                    /!\ If the webhook does not work the tools crash')
        webhookdeleter = input(f"{colorama.Fore.RED} \nWebhook link: {colorama.Fore.WHITE}")

        hook = Webhook(webhookdeleter)
        x = requests.delete(webhookdeleter)
        print("     Wait...")
        time.sleep(3)
        print("     Webhook deleted.")

        time.sleep(10)
        os.system("exit")
    if choice1 == "2":
        os.system("cls")
        print(f"""{colorama.Fore.RED}
     

                                        __      __      ___.   .__                   __             ___________           .__           
                                       /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  ______ \__    ___/___   ____ |  |   ______ 
                                       \   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / /  ___/   |    | /  _ \ /  _ \|  |  /  ___/ 
                                        \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \___ \    |    |(  <_> |  <_> )  |__\___ \  
                                         \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \/____  >   |____| \____/ \____/|____/____  > 
                                              \/       \/    \/     \/                   \/     \/                                  \/ 
                                                            
                                                                            
                                                                      Webhook Tools
     """)
        print(f'{colorama.Fore.BLUE}                                                    /!\ If the webhook does not work the tools crash')
        webhooklink = input(f"{colorama.Fore.RED} \nWebhook link: {colorama.Fore.WHITE}")
        webhookmsg = input(f"{colorama.Fore.RED} \nMessage: {colorama.Fore.WHITE}")
        data = {
            "content" : "",
            "username" : "Webhook Tool"
        }
        data["embeds"] = [
        {
        "description" : f"{webhookmsg}",
        "title" : "Webhook Tool"
        }
]
        result = requests.post(webhooklink, json = data)
        print("\n\nMessage sended restart tool.")
        time.sleep(9999)

    if choice1 == "3":
        os.system("cls")
        print(f"""{colorama.Fore.RED}
     

                                        __      __      ___.   .__                   __             ___________           .__           
                                       /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  ______ \__    ___/___   ____ |  |   ______ 
                                       \   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / /  ___/   |    | /  _ \ /  _ \|  |  /  ___/ 
                                        \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \___ \    |    |(  <_> |  <_> )  |__\___ \  
                                         \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \/____  >   |____| \____/ \____/|____/____  > 
                                              \/       \/    \/     \/                   \/     \/                                  \/ 
                                                            
                                                                            
                                                                      Webhook Tools
     """)
        print(f'{colorama.Fore.BLUE}                                                    /!\ If the webhook does not work the tools crash')
        webhooklink = input(f"{colorama.Fore.RED} \nWebhook link: {colorama.Fore.WHITE}")
        webhookmsg = input(f"{colorama.Fore.RED} \nMessage: {colorama.Fore.WHITE}")
        webhooknumber = input(f"{colorama.Fore.RED} \nNumber of message: {colorama.Fore.WHITE}")    
        data = {
            "content" : "",
            "username" : "Webhook Tool"
        }
        data["embeds"] = [
        {
        "description" : f"{webhookmsg}",
        "title" : "Webhook Tool"
        }
]

        count = 0
        while (count < 50):   
            count = count + 1
            print(f"{colorama.Fore.RED}Message sended")
            result = requests.post(webhooklink, json = data)
        print("\n\nSpam ended.")

        time.sleep(9999)

    if choice1 == "4":
        os.system("cls")
        print(f"""{colorama.Fore.RED}
     

                                        __      __      ___.   .__                   __             ___________           .__           
                                       /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  ______ \__    ___/___   ____ |  |   ______ 
                                       \   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / /  ___/   |    | /  _ \ /  _ \|  |  /  ___/ 
                                        \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \___ \    |    |(  <_> |  <_> )  |__\___ \  
                                         \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \/____  >   |____| \____/ \____/|____/____  > 
                                              \/       \/    \/     \/                   \/     \/                                  \/ 
                                                            
                                                                            
                                                                      Webhook Tools
     """)
        print(f"{colorama.Fore.BLUE}Developer: {colorama.Fore.WHITE}Fontesie\n{colorama.Fore.BLUE}Discord: {colorama.Fore.WHITE}Fontesie#2621\n")
        time.sleep(9999)


    else:
        os.system("cls")
        print("Error restart tool.")
        time.sleep(10)

main()
nuker()
