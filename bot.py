#!/usr/bin/env python

import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = '1234567890'
CONSUMER_SECRET = '1234567890'
ACCESS_KEY = '1234567890'
ACCESS_SECRET = '1234567890'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)

api = tweepy.APY(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
  api.update_status(line)
  time.sleep(900) # same as 15 minutes
