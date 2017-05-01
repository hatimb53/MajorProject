import urllib3
import json
from pprint import pprint
http = urllib3.PoolManager()

import random
import csv
with open('companylist.csv', 'rb') as csvfile:
	
	sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	b=False
	dt=""
	count=0
	
	for record in sreader:

		#print record[0]
		count=count+1
		if count>50:
			break
		#print count
		if(b):
			#r=str(record[0])
			#print type(record[0]),type(str(record[0]))
			#r=str(record[0])
			rt=record[0].replace("\"","")
			try:
				r = http.request('GET', 'http://chartapi.finance.yahoo.com/instrument/1.0/'+rt+'/chartdata;type=quote;range=1d/json')

				data=str(r.data)[str(r.data).index('(')+1:str(r.data).index(')')]
				data=data.replace("\n","")
				data1=json.loads(str(data))
				d=data1["series"][len(data1["series"])-1]
	
				dr=str(d).replace("u\'","\'")
				dr=dr.replace('\"',"\'")
				dr=dr.replace('\'','\"')
				#pprint(data)
				dt=dt+str('{"quotes":[{"Symbol":')+record[0]+str('},')+dr+str("]},")
				#print dt
				
				
				
				continue
			except:
				#print "error"
				continue
		if count<10:
			b=True
		#break
		

	print '{"data":[',dt[:len(dt)-1],']}'

