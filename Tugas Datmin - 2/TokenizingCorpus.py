

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle as pkl
import numpy as np


class TokenizingCorpus:
    def __init__(self,maxDF=2000,minDF=10):
        self.VectorWeight=TfidfVectorizer(
            input='content',
            encoding='latin-1',
            lowercase=True,
            stop_words='english',
            max_df=maxDF,
            min_df=minDF,
            analyzer = 'word',
            norm='l2',  #kalau vector sudah dinormalize
            use_idf=True
            ) 
        self.dictionaryPrediksi="templateDictionaryPrediksi.pkl"

    #pembuatan dataframe train
    def __call__(self,documents) :
        
        vectorTrain=self.__makeVectorCorpus(documents,self.VectorWeight)
        dataFrameTrain=self.__makeTrainDataFrame(vectorTrain)
        return dataFrameTrain

    def __makeVectorCorpus(self,arrIsi,VectorWeight):
        TFxIDF=VectorWeight.fit_transform(arrIsi)
        listAllFitur=VectorWeight.get_feature_names_out().tolist()
        
        denseTanpaHeader=TFxIDF.toarray()
        
        return denseTanpaHeader

    def __makeTrainDataFrame(self,VectorTrain):

        df=pd.DataFrame(VectorTrain)
        return df


            



