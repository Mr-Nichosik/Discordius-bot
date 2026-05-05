
import re

def clean(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) # убираем всё кроме букв, цифр и пробелов
    return text.strip()