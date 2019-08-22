#!/usr/bin/env python3
import configparser
import requests

# Read from config file
config = configparser.ConfigParser()
config.read('etc/facetheforest.conf')

# Get credentials from config
try:
	access_token = config['facebook'].get('access_token')
	user_access_token = config['facebook'].get('user_access_token')
except KeyError as e:
	print("Provide an access_token in 'etc/facetheforest.conf' file.")
	exit()

if access_token is None:
	print("access_token not defined in 'etc/facetheforest.conf'")
	exit()

fb_url = 'https://graph.facebook.com'

try:
	r = requests.get('{}/{}'.format(fb_url, 'me/feed'), params={'message':"ftf!",'access_token': user_access_token})
	print(r.status_code)
	r.raise_for_status()
	data = r.json()

print(data)

