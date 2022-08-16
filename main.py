#Import library for telegram bot
import requests

TOKEN = '5355192064:AAHeVCobTRAUsm0lsi9e_l_QZbfFMVuVFeM'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data={'chat_id': chat_id, 'text': text,'parse_mode': 'MarkdownV2'}
    answer = requests.post(url,data)
    return answer.json()



#Send message some text with markdown
text = '*Hello* World'
chat_id = '5575549228'
send_message(text, chat_id)