import requests
import json
import urllib.request

apiTarget = "https://api.waqi.info/feed/geo:{0};{1}/?token=0daef5bc25531d763ff0adaf8f460153ecd3d004".format(lat, lon)
r = requests.get(apiTarget)
r.text
data = json.loads(r.text)

def GetAiq(lon,lat):
  #AIQ Levels: 0-50 Good, 51-100 Moderate, 101-150 Unhealthy for Sensitive Groups, 151-200 Unhealthy, 201-300 Very Unhealthy, 301-500 Hazardous
  fullURL = url_builder(lon, lat)
  info = data_fetch(fullURL)
  organizedData = organized(info)
  return organizedData

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
    aqi = raw_info.get('data').get('aqi')
    )
    return data

def data_print(data):
  print('AQI: {}'.format(data['aqi']))

def get_Aiq():
  return data['aiq']
