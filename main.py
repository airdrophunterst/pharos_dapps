import asyncio
import importlib
from colorama import *


def main():
    while True:
        print(f"{Fore.GREEN + Style.BRIGHT}Select Option:{Style.RESET_ALL}")
        print(f"{Fore.WHITE + Style.BRIGHT}1. Pharsos {Style.RESET_ALL}")
        print(f"{Fore.WHITE + Style.BRIGHT}2. OpenFi {Style.RESET_ALL}")
        print(f"{Fore.WHITE + Style.BRIGHT}3. Brokex {Style.RESET_ALL}")
        print(f"{Fore.WHITE + Style.BRIGHT}4. Faros {Style.RESET_ALL}")
        print(f"{Fore.WHITE + Style.BRIGHT}4. Gotchip {Style.RESET_ALL}")

        option = int(input(f"{Fore.BLUE + Style.BRIGHT}Choose [1/2/3/4/5] -> {Style.RESET_ALL}").strip())
        
        if option == 1:
            pharos = importlib.import_module('pharos')
            bot = pharos.PharosTestnet()  
            asyncio.run(bot.main())  
        elif option == 2:
            openfi = importlib.import_module('openfi')
            bot = openfi.OpenFi()  
            asyncio.run(bot.main())  
        elif option == 3:
            brokex = importlib.import_module('brokex')
            bot = brokex.Brokex()  
            asyncio.run(bot.main())  
        elif option == 4:
            faros = importlib.import_module('faros')
            bot = faros.Faroswap()  
            asyncio.run(bot.main())  
        elif option == 5:
            gotchip = importlib.import_module('gotchip')
            bot = gotchip.Gotchipus()  
            asyncio.run(bot.main())  
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()