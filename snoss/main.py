import colorama
import requests
import os
import getpass
import socket
import requests
import datetime

blue = colorama.Fore.LIGHTBLUE_EX
red = colorama.Fore.LIGHTRED_EX
green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.LIGHTCYAN_EX

os.system("title CrazySnos - один из лучших сносеров, ТГК: t.me/КРЯКНУТЫЕ_БЛЯДИ, Разработчик: @ХУЕСОС, КРЯКНУТ: ВЕЛИКИМ @ASTRADEATH")

print(green + "[!] Ваше устройство обнаружено, доступ разрешен")
# os.system("clear | clr")

banner = blue + """

   █████████                                             █████████
  ███░░░░░███                                           ███░░░░░███
 ███     ░░░  ████████   ██████    █████████ █████ ████░███    ░░░  ████████    ██████   █████
░███         ░░███░░███ ░░░░░███  ░█░░░░███ ░░███ ░███ ░░█████████ ░░███░░███  ███░░███ ███░░
░███          ░███ ░░░   ███████  ░   ███░   ░███ ░███  ░░░░░░░░███ ░███ ░███ ░███ ░███░░█████
░░███     ███ ░███      ███░░███    ███░   █ ░███ ░███  ███    ░███ ░███ ░███ ░███ ░███ ░░░░███
 ░░█████████  █████    ░░████████  █████████ ░░███████ ░░█████████  ████ █████░░██████  ██████
  ░░░░░░░░░  ░░░░░      ░░░░░░░░  ░░░░░░░░░   ░░░░░███  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░░
                                              ███ ░███
                                             ░░██████
                                              ░░░░░░

┌───────────────────────────────────────────────────────────────────────────────┐                                       
│                Разработчик: @скуф  // ТГК: @петушары                          │
└───────────────────────────────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────────────────────────────┐
│[1] Снос аккаунта [почты]                  [6] Снос аккаунта [сайт]            │
│[2] Снос сессий [почты]                    [7] Снос сессий [сайт]              │
│[3] Снос ТГК [почты]                       [8] Снос ТГК [сайт]                 │
│[4] Снос бота [почты]                      [9] Снос бота [сайт]                │
│[5] Бомбер входами в аккаунт               [10] Информация                     │
│───────────────────────────────────────────────────────────────────────────────│
│                                  [11] Выйти                                   │
└───────────────────────────────────────────────────────────────────────────────┘

"""
print(banner)
choice = input(blue + "[?] Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    os.system("python account.py")
elif choice == "2":
    os.system("clear")
    os.system("python sessions.py")
elif choice == "3":
    os.system("clear")
    os.system("python channel.py")
elif choice == "4":
    os.system("clear")
    os.system("python bot.py")
elif choice == "5":
    os.system("clear")
    os.system("python bomber.py")
elif choice == "6":
    os.system("clear")
    os.system("python siteaccount.py")
elif choice == "7":
    os.system("clear")
    os.system("python sitesessions.py")
elif choice == "8":
    os.system("clear")
    os.system("python sitechannel.py")
elif choice == "9":
    os.system("clear")
    os.system("python sitebot.py")
elif choice == "10":
    print(blue + "CrazySnos - это один из лучший python софтов для сноса telegram аккаунтов, каналов, ботов, а также для спама кодами в telegram\nРазработчик: @долбаеб_нищий\nТГК: t.me/крякнутые_пидарки\n")
    print(red + "ПРОГРАММА БЫЛА ВЫЕБАНА В ОЧКО АСТРАЛОМ DISCORD: ITZ_XO. #УСПЕХНЕИЗБЕЖЕН")
    getpass.getpass(blue + "Нажмите ENTER для возврата в главное меню\n")
    os.system("python main.py")
elif choice == "11":
    print(cyan + "Завершение работы...")
    exit()