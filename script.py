import urllib3
import json
from pprint import pprint
http = urllib3.PoolManager()
r = http.request('GET', 'http://chartapi.finance.yahoo.com/instrument/1.0/GOOG/chartdata;type=quote;range=1m/json')
#print r.status
#print str(r.data).index('(')
#print str(r.data)[str(r.data).index('(')+1:str(r.data).index(')')]
data=str(r.data)[str(r.data).index('(')+1:str(r.data).index(')')]
data=data.replace("\n","")
data1=json.loads(str(data))
d=data1["series"]
dr=str(d).replace("u\'","\'")
dr=dr.replace('\"',"\'")
dr=dr.replace('\'','\"')
#pprint(data)

print '{"data":',dr,'}'