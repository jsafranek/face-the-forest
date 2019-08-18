#!/usr/bin/env python3
import configparser

import facebook

# Read from config file
config = configparser.ConfigParser()
config.read('etc/facetheforest.conf')

# Get credentials from config
access_token = config['facebook']['access_token']

# Facebook SDK for Python
graph = facebook.GraphAPI(access_token=access_token, version="2.12")

print("hello, world! <3")
