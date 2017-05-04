import urllib3
import json



import random
import csv

class fetch:
	def fetchData(self,duration,ticker):
		http = urllib3.PoolManager()
		dt=""
		if True:
			req = http.request('GET', 'http://chartapi.finance.yahoo.com/instrument/1.0/'+ticker+'/chartdata;type=quote;range='+duration+'/json')

			data=str(req.data)[str(req.data).index('(')+1:str(req.data).index(')')]
			data=data.replace("\n","")
			data1=json.loads(str(data))
			for i in range(0,len(data1["series"])):
				d=data1["series"][i]
				#print d
				dr=str(d).replace("u\'","\'")
				dr=dr.replace('\"',"\'")
				dr=dr.replace('\'','\"')
				#pprint(data)
				dt=dt+dr+str("\n")
				#print dt
				#print dt
				
		
	
		
		
		return dt[:len(dt)-1]



