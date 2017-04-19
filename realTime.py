#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:56:08 2017

@author: hatim
"""


import os
import sys

os.chdir("/home/hatim/Documents/workspace/pyspark")
os.curdir

if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME']='/usr/local/spark'
    
SPARK_HOME = os.environ['SPARK_HOME']

sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib"))   
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","py4j-0.10.1-src.zip"))

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext


from pyspark.ml.feature import StringIndexer
conf=SparkConf()
conf.set("spark.executer.memeory","1g")
conf.set("spark.cores.max","2")

conf.setAppName("My first")

sc=SparkContext('local',conf=conf)
ssc = StreamingContext(sc,2)
sqlContext=SQLContext(sc)




from yahoo_finance import Share
yahoo = Share('YHOO')
stockq=yahoo.get_historical('2016-03-1', '2017-02-28')
stockq

stockqf=sqlContext.read.json(sc.parallelize(stockq))
from pyspark.ml.linalg import Vectors

from decimal import Decimal



def evalt(label):
    
   


#close predict
    s1=stockqf.select(label,'Date').rdd

   # print s1.collect()

    def transform(line):
        l=str(line[1]).split('-')
    
   
        return float(line[0]),Vectors.dense([float(l[0]),float(l[1]),float(l[2])])

    testsr=[{'Date':'2018-04-13','Close':25.6}]
    testsr

    testst=sqlContext.read.json(sc.parallelize(testsr))
    testst.show()

    sy=testst.select('Close','Date').rdd
    sy.collect()

    test1=sy.map(transform)
    test1.collect()
    
    test2=sqlContext.createDataFrame(test1,["label","features"])
    print "label and features test"
    print test2.select("*").show(10)
   
    s2=s1.map(transform)
    print "rdd"
    print s2.collect()
    df=sqlContext.createDataFrame(s2,["label","features"])
    print "label and features"
    print df.select("*").show(10)

 

# Split the data into train and test
    splits = df.randomSplit([0.9, 0.1])
    train = splits[0]
    test = splits[1]
    
    train.show(10)
    
    from pyspark.ml.regression import LinearRegression

# create object of linear regression
    lr= LinearRegression(maxIter=50).setSolver("l-bfgs")

# create model by fitting training dataset
    lrmodel=lr.fit(train)
    print("Coeff"+str(lrmodel.coefficients))
    print("Inter"+str(lrmodel.intercept))
    

# predict value by of testing data set
  
    prediction=lrmodel.transform(test)

#print prediction value along with label and features
    print "prediction"
    prediction.select("prediction","label","features").show(prediction.select("prediction","label","features").count())
"""
    from pyspark.ml.evaluation import RegressionEvaluator
# accuracy evaluation
    evaluator=RegressionEvaluator(predictionCol="prediction",labelCol="label",metricName="rmse")

    print("Accuracy")
    print evaluator.evaluate(prediction)
"""


evalt("High")
