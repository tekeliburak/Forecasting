# -------------------------------------------------------------------------
# Pv Data From Ninja
# -------------------------------------------------------------------------
from time import sleep, time
import requests
import pandas as pd
from geopy import Here
# -------------------------------------------------------------------------
# knowledge of latitude and longitude
# -------------------------------------------------------------------------
here_app_id = "DvUd1DUSITHMgMbPVpEb"
here_api_key = "kfNr0mAwPMOAjgzMdl33Z_imO1geXCeTdhLk6U1B6Ac"
locator = Here(apikey=here_api_key, app_id=here_app_id)
location = locator.geocode(input("Enter your location, please:"))
print(f"latitude : {location.latitude}", f"longitude: {location.longitude}")
token = 'Your Special token'
api_base = 'https://www.renewables.ninja/api/'
s = requests.session()
s.headers = {'Authorization': 'Token ' + token}
capacity = input("enter the capacity, please: ")
year = [2015, 2016, 2017, 2018, 2019]
# -------------------------------------------------------------------------
# pv data for the selection location
# -------------------------------------------------------------------------
url = api_base + 'data/pv'
var_val = 0.1
y = ""
new_latitude = location.latitude - var_val
new_longitude = location.longitude - var_val
for i in range(3):
 for k in range(3): 
  for j in range(4):
   args = {
   'lat': new_latitude, # 34.125,
   'lon': new_longitude, # 39.814,
   'date_from': f'{year[j]}-01-01',
   'date_to': f'{year[j]}-12-31',
   'dataset': 'merra2',
   'capacity': capacity,
   'system_loss': 0.1,
   'tracking': 0,
   'tilt': 35,
   'azim': 180,
   'format': 'csv',
   'raw': True,
    }
   r = s.get(url, params=args)
   y += r.text[742+len(str(capacity))+len(str(new_latitude))+len(str(new_longitude)):len(r.text)]
   time.sleep(11)
  new_longitude += var_val
  new_latitude += var_val
 new_longitude = location.longitude - var_val
ths = open("pv9dot.csv", "w")
ths.write(y)
ths.close()
t = ""
new_latitude = location.latitude - var_val
new_longitude = location.longitude - var_val
for i in range(3):
 for k in range(3):
  args = {
 'lat': new_latitude, # 34.125,
 'lon': new_longitude, # 39.814,
 'date_from': '2019-01-01',
 'date_to': '2019-12-31',
 'dataset': 'merra2',
 'capacity': capacity,
'system_loss': 0.1,
 'tracking': 0,
 'tilt': 35,
 'azim': 180,
 'format': 'csv',
 'raw': True,
  }
  r = s.get(url, params=args)
  t += r.text[742+len(str(capacity))+len(str(new_latitude))+len(str(new_longitude)):len(r.text)]
  time.sleep(11)
  new_longitude += var_val
 new_latitude += var_val
 new_longitude = location.longitude - var_val
ths = open("pv9dot_2019.csv", "w")
ths.write(t)
ths.close()
# -------------------------------------------------------------------------
# Weather Data 9 dots
# -------------------------------------------------------------------------
url = api_base + 'data/weather'
new_latitude = location.latitude - var_val
new_longitude = location.longitude - var_val
z = ""
for i in range(3):
 for j in range(3):
  for k in range(4):
   args = {
 'lat': new_latitude,
 'lon': new_longitude,
 'date_from': f'{year[k]}-01-01',
 'date_to': f'{year[k]}-12-31',
 'dataset': 'merra2',
 'format': 'csv',
 'raw': True,
 'var_t2m': True,
 'var_prectotland': True,
 'var_precsnoland': True,
 'var_snomas': True,
 'var_rhoa': True,
 'var_swgdn': True,
 'var_swtdn': True,
 'var_cldtot': True,
   }
   r = s.get(url, params=args)
   z += r.text[1041+len(str(new_latitude))+len(str(new_longitude)):len(r.text)]
   time.sleep(11)
  new_longitude += var_val
 new_latitude += var_val
 new_longitude = location.longitude - var_val
w_file = open("weather9.csv", "w")
w_file.write(z)
w_file.close()
new_latitude = location.latitude - var_val
new_longitude = location.longitude - var_val
x = ""
for i in range(3):
 for j in range(3):
  args = {
 'lat': new_latitude,
 'lon': new_longitude,
 'date_from': '2019-01-01',
 'date_to': '2019-12-31',
 'dataset': 'merra2',
 'format': 'csv',
 'raw': True,
 'var_t2m': True,
 'var_prectotland': True,
 'var_precsnoland': True,
 'var_snomas': True,
 'var_rhoa': True,
 'var_swgdn': True,
 'var_swtdn': True,
 'var_cldtot': True,
  }
  r = s.get(url, params=args)
  x +=r.text[1041+len(str(new_latitude))+len(str(new_longitude)):len(r.text)]
  time.sleep(11)
  new_longitude += var_val
 new_latitude += var_val
 new_longitude = location.longitude - var_val
w_file = open("weather9_2019.csv", "w")
w_file.write(x)
w_file.close()