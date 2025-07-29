import socket
import requests

COLOR_CODE = {
    "RESET": "\033[0m",  
    "GREEN": "\033[32m",
}

def get_ip():
    ip = input(f'{COLOR_CODE["GREEN"]}[@]Введите айпи: ')

    try:
        ip = socket.gethostbyname(ip)
        
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()
        
        if infoList.get("success"):
            print(f'''{COLOR_CODE["GREEN"]}

      Айпи адресс:   {infoList["ip"]}
      Успех:         {infoList["success"]}
      Тип:           {infoList["type"]}
      Континент:     {infoList["continent"]}
      Страна:        {infoList["country"]}
      Регион:        {infoList["region"]}
      Город:         {infoList["city"]}
      Почтовый код:  {infoList["postal"]}
      Столица:       {infoList["capital"]}
                     
''')
        else:
            print(f'''{COLOR_CODE["GREEN"]}

      IP:           {infoList["ip"]}
      Success:      {infoList["success"]}
      Message:      {infoList["message"]}
                     
''')
    except Exception as e:
        print(f'{COLOR_CODE["GREEN"]}Произошла ошибка: {e}')

