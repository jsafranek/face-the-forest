#!/usr/bin/env python3
import configparser
import requests

# Read from config file
config = configparser.ConfigParser()
config.read('etc/facetheforest.conf')

# Get credentials from config
try:
	access_token = config['facebook'].get('access_token')
except KeyError as e:
	print("Provide an access_token in 'etc/facetheforest.conf' file.")
	exit()

if access_token is None:
	print("access_token not defined in 'etc/facetheforest.conf'")
	exit()

print(access_token)
fb_url = 'https://graph.facebook.com'

try:
	r = requests.get('{}/{}'.format(fb_url, 'me'), params={'access_token': access_token})
	r.raise_for_status()
except requests.exceptions.RequestException as err:
	print(err)
	r = "nope"

try:
	data = r.json()
	print(data)
except:
	print('json parsing failure')
print(r)
