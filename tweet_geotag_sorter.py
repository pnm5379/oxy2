import networkx as nx
import json
import pickle

tweets_file = file("1year_filtered.json")

count = 0
count1 = 0
file = open("Tweet_Geotags.txt",'w')
file.write(str("Latitude, Longitude"))
file.write(str("\n"))
while True:
    line = tweets_file.readline()
    if line == "":
        break
    try:
        j = json.loads(line)
        count1 = count1 + 1
        try:
            if j["user"]["geo_enabled"]:
                try:
                    #file.write(str("["))
                    file.write(str(j["geo"]["latitude"]))
                    file.write(str(", "))
                    file.write(str(j["geo"]["longitude"]))
                    #file.write(str("]"))
                    file.write(str("\n"))
                    count = count + 1
                except KeyError:
                            pass
        except KeyError:
                    pass
    except ValueError:
        pass
tweets_file.close()

print "Number of Tweets:"
print count1
print "Number of Tweets with Geotags:"
print count 