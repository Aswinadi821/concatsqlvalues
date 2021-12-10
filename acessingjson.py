import json

with open("JSONFile.json") as access_json:
    read_content=json.load(access_json)

sqlfile=open("SQLFile .sql",'r')

def getvalueofdirectors():
     content1= read_content['info']
     content2 = content1['directors']
     return content2


def concatsqlfile(x,sqlfile):
     sql=("""SELECT * FROM movie WHERE directors = '%s' """%(x[0]))
     
     print(sql)
    



x = getvalueofdirectors()
concatsqlfile(x,sqlfile)


