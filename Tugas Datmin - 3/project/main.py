
import cv2
from Input import Input
from ImageReader  import ImageReader
from processingWrap  import ImageProcessing
from ImageProcessing  import ImageProcessing 

import os
os.system('clear')
pathDaun ="../res/strawberry/"

import warnings
warnings.filterwarnings("ignore")

input=Input()
print("get path done")
pathGambarDaun=input(pathDaun)


Reader=ImageReader(8)
listGambarPerRegion=Reader(pathGambarDaun,cv2)
print("read image done")


ImageProcessing=ImageProcessing()

ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=4)

ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=5)

ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=6)

ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=6)

ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=7)

ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=8)


# ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=9)

# ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=10)

# ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=11)

# ImageProcessing(listGambarPerRegion=listGambarPerRegion,start=0,stop=2000000,threshold=12)
# process=ImageProcessing()
# process(listGambarPerRegion,10)


# from ImageProcessing  import ImageProcessing as IP
# ip=IP()
# ip(listGambarPerRegion=listGambarPerRegion,start=0,stop=231434314)


