from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Get Customer total spend")
sc = SparkContext(conf=conf)


def parse_customer_order(line: str) -> (int, float):
    fields = line.split(",")
    return int(fields[0]), float(fields[2])


input = sc.textFile("data/customer-orders.csv")
customer_spends = input.map(parse_customer_order)
spend_totals = customer_spends.reduceByKey(lambda x, y:  x + y)
sorted_total = spend_totals.map(lambda x: (x[1], x[0])).sortByKey()

results = sorted_total.collect()
for spend, customer_id in results:
    print(f"{customer_id}\t\t\t " + "{:.2F}".format(spend))
