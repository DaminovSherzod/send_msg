#Import library for telegram bot
import requests
from pprint import pprint
TOKEN = '5355192064:AAHeVCobTRAUsm0lsi9e_l_QZbfFMVuVFeM'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data={'chat_id': chat_id, 'text': text,'parse_mode': 'MarkdownV2'}
    answer = requests.post(url,data)
    return answer.json()

#Send keyboar

def send_keyboard(chat_id:int):
    button = {
        'text':'Button'
    }

    keyboard = [
        [button]
    ]

    reply_markup = {
        'keyboard':keyboard
    }
    data = {
        'chat_id':chat_id,
        'text':'TEST',
        'reply_markup':reply_markup
    }

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    answer = requests.post(url,json=data)

    return answer.json()




chat_id = '5575549228'

send_keyboard(chat_id=chat_id)