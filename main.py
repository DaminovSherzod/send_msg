#Import library for telegram bot
import requests

TOKEN = '5446020024:AAHcDq0gInuUnVWolbamoUNoqbFA490U4N8'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data={'chat_id': chat_id, 'text': text}
    answer = requests.post(url,data)
    return answer.json()


