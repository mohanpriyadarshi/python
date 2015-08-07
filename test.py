__author__ = 'mohanchintamanapinna'
import yaml
f = open('data.yaml')
# use safe_load instead load
dataMap = yaml.safe_load(f)
for i in dataMap:
    hlist=i['range']


f.close()