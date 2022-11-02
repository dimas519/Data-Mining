from tracemalloc import start
from ImageProcessing  import ImageProcessing as IP
import threading
import math
import datetime
import time


class ImageProcessing:
    def __call__(self,listGambarPerRegion,numOfParalel=1):
        today = datetime.datetime.today()
        print(today)
        banyak=len(listGambarPerRegion[0])
        oneBatch=math.ceil(banyak/numOfParalel)
        curr=0;
        for i in range(0,numOfParalel,1):
            thread1 =myThread(i,curr,curr+oneBatch,listGambarPerRegion)
            thread1.start()
            curr+=oneBatch+1
        print(len(threading.enumerate()))
        # thread1.join()
        print(today)
        print(datetime.datetime.today())
        





class myThread (threading.Thread):
    def __init__(self, counter,idxStart,stop,listGambarPerRegion):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.idxStart=idxStart
        self.stop=stop
        self.listGambarPerRegion=listGambarPerRegion

    def run(self):
        import shutil
        shutil.copy2("predictionModel.pkl","predictionModel"+str(self.threadID)+".pkl")
        ip=IP()
        ip(listGambarPerRegion=self.listGambarPerRegion,start=self.idxStart,stop=self.stop,num=str(self.threadID))