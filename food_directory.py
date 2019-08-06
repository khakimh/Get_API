import requests
import locale
locale.setlocale(locale.LC_ALL, '')

cari = input('Masukkan makanan : ')
url = 'https://developers.zomato.com/api/v2.1/search?entity_id=74&q=' + cari
headers = {'user-key': '97868952df491d79827a0c59ab0bdb85'}
data = requests.get(url, headers=headers)
restoran = data.json()['restaurants']

print('Daftar makanan',cari,'di Jakarta adalah sebagai berikut : ')
for item in restoran:
    print('*',item['restaurant']['name'],'-- Harga rata-rata Rp. {:n}'.format(item['restaurant']['average_cost_for_two']), '--', item['restaurant']['location']['locality'],'-', item['restaurant']['location']['address'])