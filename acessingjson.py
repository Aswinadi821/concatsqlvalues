import json

with open("JSONFile.json") as access_json:
    read_content=json.load(access_json)

sqlfile=open("SQLFile .sql",'r')

def getvalueofdirectors():
     content1= read_content['info']
     content2 = content1['directors']
     return content2


def concatsqlfile(x,sqlfile):
     sql=("""SELECT * FROM movie WHERE directors = '%s' directors_rating = 5 """%(x[0]))
     sql2=("""SELECT * FROM movie WHERE directors = '%s' directors_rating = 3 """ %(x[1]))
     print(sql)
     print(sql2)



x = getvalueofdirectors()
concatsqlfile(x,sqlfile)


