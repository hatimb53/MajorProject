#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:28:38 2017

@author: hatim
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:36:54 2017

@author: hatim
"""

#given program predict open price when it give features variable (close,high,low,date,ticker symbol) 

# stock.csv file in current directory where current program run

import os
import sys

#change curent directory 
os.chdir("/home/hatim/Documents/workspace/pyspark")
os.curdir

# set spark home
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME']='/usr/local/spark'
    
SPARK_HOME = os.environ['SPARK_HOME']

# set pyspark library path
sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib"))   
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","py4j-0.10.1-src.zip"))


from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext,Row


#configure spark context
conf=SparkConf()
conf.set("spark.executer.memeory","1g")
conf.set("spark.cores.max","2")

conf.setAppName("My first")

#creating spark context
sc=SparkContext('local',conf=conf)
sc.setLogLevel('WARN')

#creating sql context
sqlContext=SQLContext(sc)



#sqlContext.setLogLevel('ERROR')
from pyspark.ml.linalg import Vectors

from pyspark.ml.feature import StringIndexer


# load data from file

from yahoo_finance import Share
yahoo = Share('YHOO')
stcVector=yahoo.get_historical('2017-03-1', '2017-03-28')


# print loaded data
print "file data"
print stcVector.collect()

# count number of data 
print "number of data in file"
print stcVector.count()

# transform into array individual data 
def cleanse(line):
    attrib=line.split(',')
   
    return (float(attrib[3][2:]),float(attrib[4][2:]),float(attrib[5][2:]),float(attrib[6][2:]),str(attrib[1]),str(attrib[2]))

stcVector=stcVector.map(cleanse)

print "array"
print stcVector.collect()


# create  data frame
autoDf=sqlContext.createDataFrame(stcVector,["open","high","low","close","ticker","date"])
print "data frame"
print autoDf.select("open","high","low","close","ticker","date").show()

# map to index ticker and date  value 
indexer = StringIndexer(inputCol="ticker", outputCol="indexed")
indexerModel = indexer.fit(autoDf)
indexData = indexerModel.transform(autoDf)



indexer = StringIndexer(inputCol="date", outputCol="indexDate")
indexerModel = indexer.fit(autoDf)
indexData = indexerModel.transform(indexData)
print indexData.collect()

# convert back  to rdd 
indexRDD=indexData.rdd.map(list)
print indexRDD.collect()
indexRDD.persist()

# transform rdd into label and features
def transforms(ln):
  
    
    return (ln[0],Vectors.dense([ln[1],ln[2],ln[3],ln[6],ln[7]]))

indexR=indexRDD.map(transforms)
print indexR.collect()

# create data frame 
df=sqlContext.createDataFrame(indexR,["label","features"])
print "label and features"
print df.select("*").show(10)

# Split the data into train and test
splits = df.randomSplit([0.6, 0.4])
train = splits[0]
test = splits[1]



from pyspark.ml.regression import LinearRegression

# create object of linear regression
lr= LinearRegression(maxIter=10)

# create model by fitting training dataset
lrmodel=lr.fit(train)
print("Coeff"+str(lrmodel.coefficients))
print("Inter"+str(lrmodel.intercept))


# predict value by of testing data set
prediction=lrmodel.transform(test)

#print prediction value along with label and features
print "prediction"
prediction.select("prediction","label","features").show(prediction.select("prediction","label","features").count())

from pyspark.ml.evaluation import RegressionEvaluator
# accuracy evaluation
evaluator=RegressionEvaluator(predictionCol="prediction",labelCol="label",metricName="r2")

print("Accuracy")
print evaluator.evaluate(prediction)
