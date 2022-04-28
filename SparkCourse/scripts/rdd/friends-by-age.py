from pyspark import SparkConf, SparkContext



conf = SparkConf().setMaster("local").setAppName('Friends by Age Example')
sc = SparkContext(conf=conf)

def parseLine(line):
    fields = line.split(',')
    age = fields[2]
    numFriends = fields[3]
    return (age, numFriends)


if __name__ == "__main__":
    print('Hello')
    lines = sc.textFile('file:///Volumes/aadi/workspace/SparkCourse/data/fakefriends.csv')
    # print(lines)
    rdd = lines.map(parseLine)
    print('Hello')
