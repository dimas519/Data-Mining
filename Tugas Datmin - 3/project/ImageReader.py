

import math
import pandas as pd
from sklearn.cluster  import KMeans





class ImageReader:
    def __init__(self,regionNnumber) :
        self.regionNnumber=regionNnumber

    def __call__(self,Pathgambar,cv):
        listOfGambar=self._reader(Pathgambar,cv)
        
        gambar=listOfGambar[0]
        label=listOfGambar[1]

        listGambarRegion=self._splitRegion(gambar)




        return listGambarRegion,label


    def _reader(self,listGambar,cv):
        listOfGambar=[]
        listOFLabel=[]
        for pathGambar in listGambar:

            gambar=cv.imread(pathGambar,cv.IMREAD_COLOR)
            label=pathGambar.split("/")[-2]
            listOfGambar.append(gambar)
            listOFLabel.append(label)
        return listOfGambar,listOFLabel
    


    def _splitRegion(self,listofGambar): #membagi gambar menjadi region region
        listOFGambar=[]
        for gambar in listofGambar:

            imageRegions=[]

            #corpus(?) sebenernya udh kotak  yg size 256 px
            sizeHorizontalGambar=len(gambar[0]) #ambil baris 0 karena jumlah kolom =lebar 
            sizeVertikalGambar=len(gambar) #banyak baris= vertikal

            pxHorizontalSekaliLoop=round(sizeHorizontalGambar/self.regionNnumber) #round karena kalau gk dia float, mending round/lower(typecast) ?
            pxVertiSekaliLoop=round(sizeVertikalGambar/self.regionNnumber)
            for baris in range(0,sizeVertikalGambar,pxVertiSekaliLoop):

                for kolom in range(0,sizeHorizontalGambar,pxHorizontalSekaliLoop):
                    region=gambar[baris:baris+pxVertiSekaliLoop ,
                                    kolom:kolom+pxHorizontalSekaliLoop, : ]
                   
                    imageRegions.append(region)
            listOFGambar.append(imageRegions)
        return listOFGambar
    




