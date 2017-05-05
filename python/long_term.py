from spark_conf import Spark
from fetchSpecific import fetch
import sys
from pyspark.ml.linalg import Vectors
from pyspark.ml.regression import LinearRegression

ft=fetch()
spark=Spark()

#stockj=spark.sqlContext.read.json('data.json')

def transformdata(line):
	return line[0]
def transform(line):
	l=str(line[1])
	#print l[:4],l[4:6],l[6:8]
	return float(line[0]),Vectors.dense([float(l[:4]),float(l[4:6]),float(l[6:8])])


obj='{"quote":['

def evalt(label,stockqf,d):


	

	#close predict
    s1=stockqf.select(label,'Date').rdd

    #print s1.collect()
    #print "d",d
    testsr=[{'Date':d,label:25.6}]
    #testsr

    testst=spark.sqlContext.read.json(spark.sc.parallelize(testsr))
    #testst.show()

    sy=testst.select(label,'Date').rdd
    #sy.collect()

    test1=sy.map(transform)
    #test1.collect()
    
    test2=spark.sqlContext.createDataFrame(test1,["label","features"])
    #print "label and features test"
    #print test2.select("*").show(10)
   
   
    s2=s1.map(transform)
    #print "rdd"
    #print s2.collect()
    df=spark.sqlContext.createDataFrame(s2,["label","features"])
    #print "label and features"
    #print df.select("*").show(10)

 

	# Split the data into train and test
    #splits = df.randomSplit([0.9, 0.1])
    #train = splits[0]
    #test = splits[1]
    
    #print train.show(10)
    
    

# create object of linear regression
    lr= LinearRegression(maxIter=50).setSolver("l-bfgs")

# create model by fitting training dataset
    lrmodel=lr.fit(df)
    #print("Coeff"+str(lrmodel.coefficients))
    #print("Inter"+str(lrmodel.intercept))
    

# predict value by of testing data set
  
    prediction=lrmodel.transform(test2)

#print prediction value along with label and features
    #print "prediction"
    sr=prediction.select("prediction").rdd
    sw=sr.map(transformdata)
    sw.collect()
  	
  	
    js='{"'+label+'":"'+str(sw.collect())+'"},'
    tb=str(sw.collect())
    return  tb 
    #print "pred",pred.find("|",2)
  
    
   
targ =open('file.html', 'r')

tbl=targ.read()
import datetime

	
def predict(duration,interval):
	global obj,tbl
	#print duration," ",interval
	tbl=tbl+'<h1>'+duration+'('+interval+')</h1>'
	tbl=tbl+'<table><tbody><tr><th>close</th><th>open</th><th>high</th><th>low</th></tr></tbody>'

	obj=obj+'{"'+duration+'":['
	stockq=ft.fetchData(interval,sys.argv[1])
	target =open('data.json', 'w')
	target.write(stockq)
	target.close()
	now = datetime.datetime.now()
	d=10000000
	if duration == "short_term":
		d=(now.year+(now.month+3)/12)*10000+((now.month+3)%12)*100+now.day
		#d=(int(str(now.year))+((int(str(now.month)))+3)/12)*10000+(int(str(now.month)+3)%12)*100+int(str(now.day))
	if duration == "mid_term":
		d=(now.year+1)*10000+now.month+now.day
		#d=(int(str(now.year))+1)*10000+int(str(now.month))*100+int(str(now.day))
	if duration == "long_term":
		d=(now.year+3)*10000+now.month+now.day
		#d=(int(str(now.year))+3)*10000+int(str(now.month))*100+int(str(now.day))
	

	#print stockq
	
	jsn=spark.sqlContext.read.json('data.json')
	#print jsn.show()
	"""obj=obj+evalt("close",jsn,d)
	
	obj=obj+evalt("open",jsn,d)

	obj=obj+evalt("high",jsn,d)
	obj=obj+evalt("low",jsn,d)"""

	obj=obj[:len(obj)-1]+"]},"
	tbl=tbl+'<tr>'

	tbl=tbl+'<td>'+evalt("close",jsn,d)+'</td>'
	
	tbl=tbl+'<td>'+evalt("open",jsn,d)+'</td>'

	tbl=tbl+'<td>'+evalt("high",jsn,d)+'</td>'
	tbl=tbl+'<td>'+evalt("low",jsn,d)+'</td>'

	tbl=tbl+'</tr></table>'


	obj=obj[:len(obj)-1]+"]},"


predict("short_term","3m")
predict("mid_term","1y")
predict("long_term","3y")
obj=obj[:len(obj)-1]+"]}"

tbl=tbl+'</body></html>'

print tbl





