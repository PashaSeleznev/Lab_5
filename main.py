import requests
import json
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk


# Дополнительное задание

def show_image():
    url = 'https://aws.random.cat/meow'
    res = requests.get(url)
    res_1 = res.json()
    url_1 = res_1['file']
    response = requests.get(url_1)
    image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)).resize((700, 700), Image.Resampling.LANCZOS))
    label.config(image=image)
    label.image = image


window = Tk()
window.title("Добро пожаловать в генератор котов")
window.geometry('700x700')
Button(window, text='Сгенерировать картинку', command=show_image).pack()
label = Label(window)
label.pack()

window.mainloop()

# Задание 1
print('1 задание')

response = requests.get('http://steamcommunity.com')
print(response.status_code)
print()

# Задание 2
print('2 задание')

print('Введите название города на английском языке:')
city_name = input()

print('Введите код страны:')
country_code = input()
city_name = city_name + ',' + country_code

api = '62a3dad1af9bb8175529539ddc6a79d6'
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': city_name, 'units': 'metric', 'lang': 'ru', 'APPID': api})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("humidity:", data['main']['humidity'])
    print("pressure:", data['main']['pressure'])
except Exception as e:
    print("Exception (weather):", e)
    pass
print()

# Задание 3
print('3 задание')

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
res = response.json()
print('Введите валюту, про которую вам нужна информация. Например, для американского доллара - USD')
good_val = input()
bad_val = 1

if good_val in res['Valute']:
    print('Date:', res['Date'])
    print('PreviousDate:', res['PreviousDate'])
    print('Timestamp:', res['Timestamp'])
    print('ID:', res['Valute'][good_val]['ID'])
    print('NumCode:', res['Valute'][good_val]['NumCode'])
    print('CharCode:', res['Valute'][good_val]['CharCode'])
    print('Nominal:', res['Valute'][good_val]['Nominal'])
    print('Name:', res['Valute'][good_val]['Name'])
    print('Value:', res['Valute'][good_val]['Value'])
    print('Previous:', res['Valute'][good_val]['Previous'])
else:
    print('Такой валюты на сайте cbr.ru нет:(')
