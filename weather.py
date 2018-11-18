import requests
import json
import urllib.request


r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=2440fec8f48e37487c9181679ff3e1af")
r.text
data = json.loads(r.text)

def url_builder(lon, lat):
    user_api = '2440fec8f48e37487c9181679ff3e1af'
    unit = 'imperial'
    api = ('http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon))
    full_api_url = api + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url

def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_info = json.loads(output)
    url.close()
    return raw_info

def organized(raw_info):
    data = dict(
    temp = raw_info.get('main').get('temp'),
    pressure = raw_info.get('main').get('pressure'),
    climate = raw_info['weather'][0]['main'],
    weathertype = raw_info['weather'][0]['description'],
    )
    return data

def data_print(data):
    print('Pressure: {}'.format(data['pressure']))
    print('Temp: {}'.format(data['temp']))
    print('Climate: {}'.format(data['climate']))
    print('Weather: {}'.format(data['weathertype']))


def get_Climate():
    return data['climate']
    
def get_Temp():
    return data['temp']
