
from Input import Input
from TokenizingCorpus import TokenizingCorpus
from Clustering import Clustering
import collections
import numpy as np



#untuk debug
import os
os.system('cls||clear')

#READ THE FILE
dataSetPath='corpus\\bbc'
input=Input()
documents=input(dataSetPath)


#BIKIN VECTOR
tokenizing=TokenizingCorpus()
DataFrameDocument=tokenizing(documents)
#print(DataFrameDocument.head())



klustering=Clustering();
clustering=klustering.buildCluster(DataFrameDocument,0.64)


listKlaster=clustering.labels_ 

 
idxNumberDocuments=5; #dimisalkan dokumen 5 yang dibaca oleh user
clusterDocument=listKlaster[idxNumberDocuments]
VectorYangDibaca=DataFrameDocument.loc[idxNumberDocuments,:]

listYangSatuKluster=[]  
for i in range(0,len(listKlaster)):
    if((listKlaster[i]==clusterDocument)and(i != idxNumberDocuments)):
        listYangSatuKluster.append(i)



dictSimilaritySaranDokument={}
for i in range(0, len(listYangSatuKluster)):
    idxDokumentSaran=listYangSatuKluster[i]
    vectorSaran=DataFrameDocument.loc[idxDokumentSaran,:]
    similarity=np.dot(VectorYangDibaca,vectorSaran) #tinggal dilakukan dot product karena vector sudah di normalize dapat dilihat dari parameter l2
    dictSimilaritySaranDokument[input.getFileName(idxDokumentSaran)]=similarity


sortedKeybyValue=sorted(dictSimilaritySaranDokument,key=dictSimilaritySaranDokument.get ,reverse=True)
    


numberDocumentShow=100 #misalkan 5 dokumen termirip yang ingin dikeluarkan
if(len(listYangSatuKluster)<numberDocumentShow):
    numberDocumentShow=len(listYangSatuKluster)


for i in range(0,numberDocumentShow):
    namafile=sortedKeybyValue[i]
    print(namafile+" : "+str(dictSimilaritySaranDokument[namafile]))


