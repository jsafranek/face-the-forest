#!/usr/bin/env python3
import configparser

import facebook

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

# Facebook SDK for Python
graph = facebook.GraphAPI(access_token=access_token, version="2.12")

print("\n## put_object():\n")
# Write 'Hello, world' to the active user's wall.
graph.put_object(parent_object='me', connection_name='feed', message='face-the-forest')
