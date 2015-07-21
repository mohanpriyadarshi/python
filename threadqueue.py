__author__ = 'mohanchintamanapinna'
#refer http://www.tutorialspoint.com/python/python_multithreading.htm  http://pymotw.com/2/threading/
from Queue import Queue
import time
#import Queue
from threading import Thread
import random

class DownloadWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue
       #print queue

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           name, link = self.queue.get()
           wait=random.randint(1,1)
           #print wait
           time.sleep(wait)
           print "start%s\t%s\n" %(name,link)
           print link
           self.queue.task_done()


# Create a queue to communicate with the worker threads
queue = Queue()
# Create 8 worker threads
for x in range(3):
    worker = DownloadWorker(queue)
    print  "Setting daemon to True will let the main thread exit even though the workers are blocking\n"
    worker.daemon = True
    worker.start() # worker.start()  method starts a thread by calling the run method.
   # tout=worker.join()
    #print tout
links=('yahoo.com','google.com','msn.com')
name=0
for link in links:
    name+=1
    #print link
    #print "forloop",name
    queue.put((name, link))

# Causes the main thread to wait for the queue to finish processing all the tasks
queue.join()
