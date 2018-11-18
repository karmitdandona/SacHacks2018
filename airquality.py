import requests
import json
import urllib.request

lat = 74.0060
lon = 40.7128

apiTarget = "https://api.waqi.info/feed/geo:{0};{1}/?token=0daef5bc25531d763ff0adaf8f460153ecd3d004".format(lat, lon)
r = requests.get(apiTarget)
r.text
data = json.loads(r.text)

def url_builder(lon, lat):
  return "https://api.waqi.info/feed/geo:{0};{1}/?token=0daef5bc25531d763ff0adaf8f460153ecd3d004".format(lat, lon)

def data_fetch(full_api_url):
  url = urllib.request.urlopen(full_api_url)
  output = url.read().decode('utf-8')
  raw_info = json.loads(output)
  url.close()
  return raw_info

def organized(raw_info):
    data = dict(
    aqi = raw_info.get('data')
    )
    return data

def data_print(data):
  print('AQI: {}'.format(data['aqi']))

if __name__ == '__main__':
    try:
        data_print(organized(data_fetch(url_builder(lat, lon))))
    except IOError:
        print('no internet')