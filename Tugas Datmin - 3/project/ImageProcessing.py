
import math
import pandas as pd
from sklearn.cluster  import KMeans
from sympy import total_degree
import pickle
import tools

import datetime
class ImageProcessing:


    def __call__(self,listGambarPerRegion,start=0,stop=-1,num='',threshold=7):
        listImage=listGambarPerRegion[0]
        listLabel=listGambarPerRegion[1]
        model=pickle.load(open("predictionModel"+num+".pkl","rb"))


        if stop ==-1:
            stop=len(listImage)
        else:
            stop=start+stop
            if(stop>len(listImage)):
                stop=len(listImage)


        salah=0
        listOFSalah=[]

        for i in  range(start,stop,1):
            

            currImage=listImage[i]
            currLabel=listLabel[i]
            numOfSakit=0;
            dfGambar=self.image_process(currImage)
            predictedAllRegion=model.predict(dfGambar)

            msgList=tools.listToString(predictedAllRegion)
            keputusan='sehat'

            for hasil in predictedAllRegion:
                if(hasil=='sakit'):
                    numOfSakit+=1
                if(numOfSakit>threshold):
                    keputusan='sakit'
                    break;

            txt = open("output-"+str(threshold)+".txt",'a')
            
            if (keputusan=='sehat' and currLabel=='Strawberry___Leaf_scorch') or(keputusan=='sakit' and currLabel=='Strawberry___healthy'):
                salah+=1
                txt.write(str(i)+" "+str(salah))
                listOFSalah.append(str(i))
            else:
                txt.write(str(i))

            print(i ,salah, datetime.datetime.today())
            txt.write("\n")
            txt.write( str(datetime.datetime.today()))
            txt.write("\n")
            txt.write("hasil :"+keputusan)
            txt.write("\n")
            txt.write("actual :"+currLabel)
            txt.write("\n")
            txt.write("debug : "+ msgList)
            txt.write("\n\n")
            txt.close()

        msg=tools.listToString(listOFSalah)

        txt = open("output-"+str(threshold)+".txt",'a')
        txt.write("\n\n")
        txt.write(str(salah))
        txt.write("\n\n")
        txt.write(msg)
        txt.close()
        print(salah)
            
                    




            

       
            

        #return dfImages



    
    def image_process(self,image):
        dfbaru=pd.DataFrame()
        for region in image:
            dictImage={}
            dominance=self._dominanceClustering(region)
            # [16,[rgb], [8,[rgb],[1,[rgb]]]]
            total=len(image[0]) * len(image[0][0])


            dictImage['B1']=dominance[2][1][0]
            dictImage['G1']=dominance[2][1][1]
            dictImage['R1']=dominance[2][1][2]
            dictImage['value1']=(dominance[2][0]/total)



            dictImage['B2']=dominance[1][1][0]
            dictImage['G2']=dominance[1][1][1]
            dictImage['R2']=dominance[1][1][2]
            dictImage['value2']=(dominance[1][0]/total)



            dictImage['B3']=dominance[0][1][0]
            dictImage['G3']=dominance[0][1][1]
            dictImage['R3']=dominance[0][1][2]
            dictImage['value3']=(dominance[0][0]/total)



            dfbaru=dfbaru.append(dictImage,ignore_index=True)

        return dfbaru








    def _dominanceClustering(self,gambar):
        normalizeRegion=self._normalize(gambar)
        new_df=pd.DataFrame(columns=['b','g','r'],data=normalizeRegion)
        kmeansModels=KMeans(n_clusters=3) #3 cluster karena asumsi 1 cluster untuk daun sakit, daun sehat(hijau ?), dan bg 
        kmeansModels.fit(new_df)
        
        counterList=[0,0,0] #list ukuran 3 untuk mencari 1 buah cluster dengan anggota terbanyak
        clusteringResult=kmeansModels.labels_


        for idxCluster in clusteringResult:
            counterList[idxCluster]=counterList[idxCluster]+1


        
        ClusterCounterWarna=[]
        for i in range(0,len(counterList),1) :
            numberMemberOFCluster= counterList[i]
            Cluster=[numberMemberOFCluster,kmeansModels.cluster_centers_[i]]
            ClusterCounterWarna.append(Cluster)
            
        sortedDominanceColor=sorted(ClusterCounterWarna,key=lambda x:x[0])
        return sortedDominanceColor



    def _normalizePixel(self,pixel):
        panjang=self.panjangVector(pixel)
        colorSpace=[]
        if panjang==0:
            colorSpace=[0.0,0.0,0.0] #karena normalisasi membagi dengan panjang vector jika |v| =0 maka td
        else :
            for color in pixel:
                norm=color/panjang
                colorSpace.append(norm)
        return colorSpace
    

    
    def _normalize(self,region):
        normalizeRegion=[]
        for baris in region:
            for kolom in baris:
                normPixel=self._normalizePixel(kolom)
                normalizeRegion.append(normPixel)
        return normalizeRegion

    def panjangVector(self,px):
        count=0

        for color in px:
            if(type(color)!=int):
                color=color.astype(int) #tipe data sebelumnya numpy.uint8
            count+=((color*color))
        panjang=math.sqrt(count)
        return panjang

    def countDistance(self,vector1,vector2):
        distance=0;
        for fitur in range(0,len(vector1),1):
            selisih=(vector1[fitur]-vector2[fitur])
            selisih=selisih*selisih
            distance+=selisih
        distance=math.sqrt(distance)
        return distance