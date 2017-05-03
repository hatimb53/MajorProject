from spark_conf import spark
from fetchSpecific import fetch
import sys
ft=fetch()
stockq= ft.fetchData("1m",sys.argv[1])
print stockq

"""def predict(symbol):
	stockj=spark.sqlContext.read.json(sc.parallelize(stockq))
	stockj=stockj.select("data")
	stockj=stockj.select("quotes")



predict(symbol)

stockj=spark.sqlContext.read.json(sc.parallelize(stockq))
stockj=stockj.select("label")"""