import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
import requests
import socket
import getpass
import colorama

blue = colorama.Fore.LIGHTBLUE_EX
red = colorama.Fore.LIGHTRED_EX
green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.LIGHTCYAN_EX
device_name = socket.gethostname()

# r = requests.get("https://pastebin.com/wTCRZb7Y")
# if str(device_name) in r.text:
senders = {
    "vladlord444@gmail.com": "edsl kboc pgoc yzib",
    "IvanKarma2000@gmail.com": "irlr cggo xksq tlbb",
    "misha28272727@gmail.com": "kgwq xvkg jycc ibkm",
    "edittendo0@gmail.com": "mzdl lrmx puyq epur",
    "shshsbsbsbwbwvw@gmail.com": "jqrx qivo qxjy jejt",
    "d6325841@gmail.com": "xuzq ztyx jzvb rant",
    "desireelinnert0@gmail.com": "xwzb lzla ppve hevz",
    "veterovseverov@gmail.com": "jubm pkhe udpr gkze",
    "Ivan27727272hwhs@gmail.com": "ozcu edfd gmgk rkqg",
    "dlyabravla655@gmail.com": "kprn ihvr bgia vdys",
    "topzone6400@gmail.com": "laum lkuc thvi lsol",
    "sanyaravanov@gmail.com ": "xqvh vmmh omcy oata",
    "volkborz2022@gmail.com": "cdzp ghoo xhaj gegd",
    "borzghost2024@gmail.com": "tmnx xtka nsas soqb",
    "dlatt6677@gmail.com": "usun ruef otzx zcrh",
    "hujnadadada@gmail.com": "ydwe writ tlyf dxnl",
    "editt1345@gmail.com": "hezf xuel hzvz jzur",
    "ghostchat2023@gmail.com": "dezs aqvy mouq lfja"
}

recievers = {
    "support@telegram.org",
    "dmca@telegram.org",
    "security@telegram.org",
    "sms@telegram.org",
    "info@telegram.org",
    "marta@telegram.org",
    "spam@telegram.org",
    "alex@telegram.org",
    "abuse@telegram.org",
    "pavel@telegram.org",
    "durov@telegram.org",
    "elies@telegram.org",
    "ceo@telegram.org",
    "mr@telegram.org",
    "levlam@telegram.org",
    "perekopsky@telegram.org",
    "recover@telegram.org",
    "germany@telegram.org",
    "hyman@telegram.org",
    "qa@telegram.org",
    "stickers@telegram.org",
    "ir@telegram.org",
    "vadim@telegram.org",
    "shyam@telegram.org",
    "stopca@telegram.org",
    "u003esupport@telegram.org",
    "ask@telegram.org",
    "125support@telegram.org",
    "me@telegram.org",
    "enquiries@telegram.org",
    "api_support@telegram.org",
    "marketing@telegram.org",
    "ca@telegram.org",
    "recovery@telegram.org",
    "http@telegram.org",
    "corp@telegram.org",
    "corona@telegram.org",
    "ton@telegram.org",
    "sticker@telegram.org"
}

def clear():
    os.system("clear")

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(red + f"Ошибка при отправке письма: {e}")
        return False

def handle_complaint(senders, receivers):
    total_emails = len(senders) * len(receivers)
    sent_emails = 0

    snoschannel = blue + """
[1] Снос за продажу запрещенных услуг/товаров
[2] Снос за слив личных данных
[3] Снос за ЦП
[4] Снос за живодерство
[5] Снос за слишком вызывающий контент
    """
    print(snoschannel)
    complaint_choice = input(blue + "[?] Выберите причину сноса -> ")

    if complaint_choice in ["1", "2", "3", "4", "5"]:
        clear()
        channellink = input(str(blue + "[?] Введите ссылку на канал -> "))
        violation_chat_link = input(str(blue + "[?] Введите ссылку на нарушение -> "))
        complaint_texts = {
            "1": f"Здравстуйте, я обнаружил telegram канал: {channellink}, данный telegram канал создан для продажи запрещенных улсуг и товаров, ссылка на нарушение: {violation_chat_link}",
            "2": f"Приветствую, я заметил канал на вашей площадке: {channellink}, канал создан для того чтобы выкладывать данные и деанонамизировать простых пользователей телеграма, ссылка на нарушение: {violation_chat_link}",
            "3": f"Уважаемая поддержка, на вашей площадке присутствует в котором выкладывается детская порнография, ссылка на канал: {channellink}, ссылка на нарушение: {violation_chat_link}",
            "4": f"Здравствуйте, на вашей площадке telegram был обнаружен telegram канал {channellink}, данный канал занимается живодерством, ссылка на нарушение: {violation_chat_link}",
            "5": f"Я обнаружил канал: {channellink} в данном канале выкладывается слишком вызывающий контент что запрещается на вашей площадке, ссылка на нарушение: {violation_chat_link}"
        }

        for _ in range(len(senders) * len(receivers)):
            sender_email, sender_password = random.choice(list(senders.items()))
            receiver_email = random.choice(list(receivers))
            complaint_text = complaint_texts[complaint_choice]
            complaint_body = complaint_text.format(channellink=channellink, violation_chat_link=violation_chat_link.strip())
            if send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram канал", complaint_body):
                print(green + "[!] Успешно отправлено")
                sent_emails += 1
            else:
                print(red + "[!] Ошибка при отправке")
                getpass.getpass(blue + "Нажмите ENTER для возврата в главное меню\n")
                os.system("python main.py")
    else:
        getpass.getpass(red + "[!] Произошла ошибка, перепроверьте вводимые данные и нажмите ENTER для возврата в главное меню\n")
        clear()
        os.system("python main.py")

if __name__ == "__main__":
    handle_complaint(senders, recievers)