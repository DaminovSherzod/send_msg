#Import library for telegram bot
import requests

TOKEN = '5355192064:AAHeVCobTRAUsm0lsi9e_l_QZbfFMVuVFeM'

#Send message 
def send_message(text:str, chat_id:int):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data={'chat_id': chat_id, 'text': text,'parse_mode': 'MarkdownV2'}
    answer = requests.post(url,data)
    return answer.json()

#Send message with photo
def send_photo(chat_id:int, photo:str):
    """
    Send photo to telegram bot
    Args:
        chat_id: id of chat
        photo: path to photo
    Returns:
        answer from telegram bot
    """
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    data={'chat_id': chat_id, 'photo': photo}
    answer = requests.post(url,data)
    return answer.json()

#Send message some text with markdown
text = '*Hello* World'
chat_id = '5575549228'
send_message(text, chat_id)

#Some URL photo of cat
photo = 'https://www.princeton.edu/sites/default/files/styles/half_2x/public/images/2022/02/KOA_Nassau_2697x1517.jpg'

dog=send_photo(chat_id, photo)
print(dog)
