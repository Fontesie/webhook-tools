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
                                                            
                                                                    

                                   .....                                                    ................                                    
                                 .....................                                        ........        ........                                
                              ......               ......                                  .....                    .....                             
                            ....                       .....                            .....                          ....                           
                          ....                           .....                         ....                              ....                         
                        ....                               ....                       ...                                  ...                        
                       ...                                   ...                    ....                                    ...                       
                      ...                                     ...                   ...                                      ...                      
                      ...                                     ....                 ...                                       ...                      
                     ...                                       .'...................'.                                        ...                     
                     ...                                       .,'................',,.                                        ...                     
                     ...                                       ....              .....                                        ...                     
                      ...                                   .:oxkkkxdc,.     .:oxxxdo:'                                      ...                      
                      ...                                 ,xXWMMMMMMMWNO, .;oKWMMMMMWWXk:.                                  ....                      
                       ...                               :KMMMMMMMMMMMMM0oONWMWMMMMMMMMMWk,                                 ...                       
                        ....                            ,0MMMMMMMMMMMMMMMWMMMMMMMWNNWMMMMW0,                              ....                        
                         ....                           oWMMMMMMMWXXWMMMMMMMMMMWXKXWMMMMMMWo                            ....                          
                           .....                       .kMMMMMMMMMKdOWMMMMMWMMWkxXMMMMMMMMMx.                         ....                            
                              ......                   .kMMMMMMMMWd.'xXWMMMWNKo.,0MMMMMMMMWo                      ......                              
                                 .............'..      .dWMMMMMMMXc   ;0MMWNx.  .xWMMMMMMMK;      .,'................                                 
                                       .......,'    ... 'OWMMMMMMNc   '0MMWWd.  .xWMMMMMMWd.       ',..........                                       
                                            .... .ckKKKOoxXMMMMMMWx.  ;KWWWNx.  ,0MMMMMMMXdlddl;.  ....                                               
                                             ....lXWMMMMMWWMWMMMMMXdldOKXXXXKxolOWMMMMMMMMMMMMMNk, ...                                                
                                             ....dNWX00XWMMMWWMMMMMNOooxddxxooONMMMMMMMMMMWWXXNMWd....                                                
                                              ...lKNNK0XWMMMMMMMMMMk. .;,,,,. .OMMMMMMMMMMMN0OKNWd'...                                                
                                              ...'dXWMN0OXWMMMMMMMMXd,.......;dXMMMMMMMMMWKKNWWW0;...                                                 
                                               ...,dXWMWOoxKWWMMMMMMWNXKKKKXXWMMMMMMMMMN0oxXWMW0:...                                                  
                                                ...'oKWMW0:'l0WMMMMMMWMMMMMMMMMMMMMMWXx;,oXMMNO;...                                                   
                                                 ....:ONWMXl.'lxOKKKXNWWWWWWWWNXKXKxc,.'kNMWKo,...                                                    
                                                   ...'l0NWWk'. .....,;;::::;,'....   :0WW0d;....                                                     
                                                    ....,cxKNKo.                    ,xXKxc,....                                                       
                                                      .....,:d00d;.              .:xOxc;....                                                          
                                                         .....,lx00koc:,,,,,;:ldkOxl,.....                                                            
                                                            .....':loxxxkkxxxxol:,....                                                                
                                                               .....................                                                                  
                                                                     .........                                                                                                                                                                               



                                                                      Webhook Tools
     """)

def webh():
    main()
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
        print("     Wait...")
        x = requests.delete(webhookdeleter)
        print("     Webhook deleted.")
        time.sleep(3)
        os.system("cls")
        webh()
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
        print("\n\nMessage sended.")
        time.sleep(3)
        os.system("cls")
        webh()

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
        time.sleep(2)
        os.system("cls")
        webh()   

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
        input(f"\n\n{colorama.Fore.RED}Press ENTER to exit")
        os.system("cls")
        webh()




    else:
        os.system("cls")
        webh()



main()
webh()
