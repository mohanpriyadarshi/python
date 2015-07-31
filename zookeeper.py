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
#zk.create("/my/favorite/node1", b"c value")

if zk.exists("/my/favorite/node"):
    print "data exist"


data, stat = zk.get("/my/favorite/node1")
#print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

import yaml
f = open('data.yaml')
# use safe_load instead load
dataMap = yaml.safe_load(f)
for i in dataMap:
    hlist=i['range']
    #if not zk.exists("/plang/"+str(hlist)):
     #   print "creating folder"
      #  zk.create("/plang/"+str(hlist))
    if zk.ensure_path("/plang/"+str(hlist)):
        zk.set("/plang/"+str(hlist), 'Segment'" "+str(i['segment']))
    data, stat = zk.get("/plang/"+str(hlist))
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

