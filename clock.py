import os, sys
import requests
import random
import time
import string

def req(uri, xapikey):
	headers = {
		"X-Api-Key": xapikey
	}
	return requests.post(uri, headers=headers, json={})

def clock(action, userid, xapikey):
	time.sleep(random.randint(0,220))

	uri = string.Template("https://api.everhour.com/users/$userid/timecards/clock-$action")
	if action == "in":
		res = req(uri.substitute(userid=userid, action="in"), xapikey)
	elif action == "out":
		res = req(uri.substitute(userid=userid, action="out"), xapikey)
	else:
		exit(1)

	print(res.json()['history'][-1])

if __name__ == '__main__':
	if len(sys.argv) < 2:
		exit(1)

	clock(sys.argv[1], os.environ['USERID'], os.environ['XAPIKEY'])
