

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import pickle as pkl


class TokenizingTest:
    def __init__(self):
        self.dictionaryPrediksi="templateDictionaryPrediksi.pkl"

    #pembuatan dataframe test
    def __call__(self,documents) :
        arrIsi=documents[1]
        vectorTest=self.__makeVector(arrIsi)
        dataFrameTest=self.makeTestDataFrame(vectorTest)
        return dataFrameTest

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
    

    def __makeVector(self,arrIsi):
        
        #Tokenizing - pembuatan vector test tidak membutuhkan pengecekan idf dan stopword
        #karena ml tidak ditrain dengan stop words sehingga nantinya akan terbuang juga stopwordnya
        

        VectorWeight=TfidfVectorizer(
            input='content',
            encoding='latin-1',
            lowercase=True,
            analyzer = 'word'
            ) 
        TFxIDF=VectorWeight  .fit_transform(arrIsi)
        listAllFitur=VectorWeight.get_feature_names_out().tolist()
        
        denseTanpaHeader=TFxIDF.toarray()
        valueFiturDisemuaDokumen=denseTanpaHeader.transpose();
        return listAllFitur,valueFiturDisemuaDokumen
        
        

            



