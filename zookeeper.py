__author__ = 'mohanchintamanapinna'
from kazoo.client import KazooClient
from kazoo.client import KeeperState
from kazoo.client import KazooState

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

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

def zkyst(path,data='none'):
    #if not zk.exists("/plang/"+str(hlist)):
     #   print "creating folder"
      #  zk.create("/plang/"+str(hlist))
    print path
    if zk.ensure_path(path):
        zk.set(path,data)
    data, stat = zk.get(path)
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

keys=('segment','simon')

f = open('data.yaml')
# use safe_load instead load
dataMap = yaml.safe_load(f)
for i in dataMap:
    hlist=i['range']
    for k in keys:
        path="/plang/"+str(hlist)+'/'+str(k)
        zkyst(path,i[k])
 #   path=["/plang/"+str(hlist)]
#    map(zkgetyst,path,keys)

