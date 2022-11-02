

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle as pkl
import numpy as np


class TokenizingCorpus:
    def __init__(self,minDF=0.0,maxDF=1.0):
        self.VectorWeight=TfidfVectorizer(
            input='content',
            encoding='latin-1',
            lowercase=True,
            stop_words='english',
            max_df=maxDF,
            min_df=minDF,
            analyzer = 'word',
            use_idf=True,
            ngram_range=(2,2)
            ) 
        self.dictionaryPrediksi="templateDictionaryPrediksi.pkl"

    #pembuatan dataframe train
    def __call__(self,documents) :
        arrIsi=documents[1]
        arrKonten=documents[0]
        vectorTrain=self.__makeVectorCorpus(arrIsi,self.VectorWeight)
        dataFrameTrain=self.__makeTrainDataFrame(vectorTrain,arrKonten)
        self.__makeTemplateDictionaryPrediction(vectorTrain[0]) #dictionary untuk prediksi agar tinggal di isi dan dipakai
        return dataFrameTrain

    def __makeVectorCorpus(self,arrIsi,VectorWeight):
        TFxIDF=VectorWeight.fit_transform(arrIsi)
        listAllFitur=VectorWeight.get_feature_names_out().tolist()
        
        denseTanpaHeader=TFxIDF.toarray()
        valueFiturDisemuaDokumen=denseTanpaHeader.transpose();
       # print(TFxIDF.idf_)
        return listAllFitur,valueFiturDisemuaDokumen

    def __makeTrainDataFrame(self,VectorTrain,arrkonten):
        listAllFitur=VectorTrain[0]
        valueFiturDisemuaDokumen=VectorTrain[1]
        groupPerbobot={}
        for i in range(0,len(listAllFitur)):
            groupPerbobot[listAllFitur[i]]=valueFiturDisemuaDokumen[i]

        #masukin kontentnya dibelakang
        groupPerbobot['konten']=arrkonten
        df=pd.DataFrame(groupPerbobot)
        return df

    def __makeTemplateDictionaryPrediction(self,listAllFitur):
        templateDense={}
        for i in range(0,len(listAllFitur)):
            templateDense[listAllFitur[i]]=0
        pickle= open(self.dictionaryPrediksi,"wb")
        pkl.dump(templateDense,pickle) 
        







            #pembuatan dataframe test
    def makeTestDataFrame(self,vectorTest):
        listAllFitur=vectorTest[0]
        valueFiturDisemuaDokumen=vectorTest[1]
        pickle= open(self.dictionaryPrediksi,"rb")
        dictionaryPrediksi=pkl.load(pickle)
        for i in range(0,len(listAllFitur)):
            if(dictionaryPrediksi.get(listAllFitur[i]) is not None):
                dictionaryPrediksi[listAllFitur[i]]=valueFiturDisemuaDokumen[i]
        dfUntukPrediksi=pd.DataFrame(dictionaryPrediksi)
        return dfUntukPrediksi
    

    def __makeVectorTest(self,arrIsi,VectorWeight):
        #idfSebeloMTest=np.copy(VectorWeight.idf_)

        
        TFxIDF=VectorWeight.transform(arrIsi)
        #print(np.array_equal(idfSebeloMTest,VectorWeight.idf_))


        listAllFitur=VectorWeight.get_feature_names_out().tolist()
        denseTanpaHeader=TFxIDF.toarray()
        valueFiturDisemuaDokumen=denseTanpaHeader.transpose();
        return listAllFitur,valueFiturDisemuaDokumen
        
    def tokenizingTest(self,documents):
        arrIsi=documents[1]
        arrKonten=documents[0]
        vectorTrain=self.__makeVectorTest(arrIsi,self.VectorWeight)
        dataFrameTrain=self.makeTestDataFrame(vectorTrain)
        return dataFrameTrain




    #DEBUG
    

            



