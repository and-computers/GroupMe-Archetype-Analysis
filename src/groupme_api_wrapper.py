import requests
import json

f = open("../key.txt","r")
TOKEN = f.read().strip()
GROUPME_URL = "https://api.groupme.com/v3/"
GROUPS_API = "groups"



r = requests.get(GROUPME_URL+GROUPS_API,params={"token":TOKEN,"omit":"memberships","per_page":100})
#print json.loads(r.text)

for group_obj in json.loads(r.text)["response"]:
	group_name = group_obj["name"]
	group_id = group_obj["id"]
	spec_group_r = requests.get(GROUPME_URL+GROUPS_API+group_id)
	spec_group_r = json.loads(spec_group_r)
	