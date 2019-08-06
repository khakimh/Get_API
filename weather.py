import requests

kota = input('Masukkan Kota : ')
url = 'https://api.openweathermap.org/data/2.5/weather?q=' +kota +'&APPID=c2fa3fe0479948a389221ba0ce164ce7'
data = requests.get(url)
cuaca = data.json()
if data.status_code == 200:
    print('\nDetail cuaca hari ini di kota',cuaca['name'],'adalah :\n',cuaca['weather'][0]['main'],cuaca['weather'][0]['description'],'\n','Suhu         : ',round(cuaca['main']['temp']-273,2),'°C\n','Tekanan      : ',cuaca['main']['pressure'],'bar\n','Kelembapan   : ',cuaca['main']['humidity'],'%')
else:
    print('Maaf kota terdaftar')    