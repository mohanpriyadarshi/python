__author__ = 'mohanchintamanapinna'
from kazoo.client import KazooClient
from kazoo.client import KeeperState
from kazoo.client import KazooState
import pprint

pp=pprint.PrettyPrinter(indent=4)
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


@zk.add_listener
def watch_for_ro(state):
    if state == KazooState.CONNECTED:
        if zk.client_state == KeeperState.CONNECTED_RO:
            print("Read only mode!")
        else:
            print("Read/Write mode!")



zk.ensure_path("/my/favorite")
zk.set("/my/favorite/node", b"d value")

if zk.exists("/my/favorite/node"):
    print "data exist"


data, stat = zk.get("/my/favorite/node")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

import yaml

def zkset(path,key,data):
    #if not zk.exists("/plang/"+str(hlist)):
     #   print "creating folder"
      #  zk.create("/plang/"+str(hlist))
    pathk=str(path)+str(key)
    print pathk
    if zk.ensure_path(pathk):
        zk.set(pathk,data)
    data, stat = zk.get(pathk)
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
    children = zk.get_children(path)
    print("There are %s children with names %s" % (len(children), children))

def zkgetyst(path,key):
    pathk=str(path)+'/'+str(key)
    print pathk +"oook"
    #exit()
    try:
        zk.ensure_path(pathk)
        data, stat = zk.get(path)
        print("Super Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
    except:
        print "Not a valid path %s"%(pathk)



f = open('data.yaml')
# use safe_load instead load
dataMap = yaml.safe_load(f)
keys=dataMap['keys']
pp.pprint(dataMap)
for i in dataMap['datamodel']:
    pp.pprint(i)
    #print i
    hlist=i['range']
    for k in keys:
        #path="/plang/"+str(hlist)+'/'+str(k)
        path="/plang/"+str(hlist)+'/'
        print path,"\t",k,"\t",i[k],"oook"
        zkset(path,k,i[k])
 #   path=["/plang/"+str(hlist)]
#    map(zkgetyst,path,keys)

