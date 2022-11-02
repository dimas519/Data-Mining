

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
class Tokenizing:
    def __init__(self,arrFile):
        self.arrFile=arrFile
        

    def __call__(self) :
        arr=self.arrFile
        arrIsi=[]
        for path in arr:
            konten= (path.split("\\")[-2])
            isi=open(path,"r").read();
            arrIsi.append(isi)


        VectorWeight=TfidfVectorizer(
            input='content',
            encoding=str,
            decode_error='ignore',#skip aja
            lowercase=True,
            norm='l2',
            use_idf=True,
            ) 
        TFxIDF=VectorWeight.fit_transform(arrIsi)

        first_vector_tfidfvectorizer=TFxIDF[1] 
        df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=VectorWeight.get_feature_names(), columns=["tfidf"]) 
        df=df.sort_values(by=["tfidf"],ascending=False)

        print(df)
        # vectorizer = TfidfVectorizer()
        # x=vectorizer.fit_transform(arrIsi)
        # y=vectorizer.get_feature_names;
        # df_countvect = pd.DataFrame(data =x .toarray(),index = ['Doc1','Doc2'],columns = y)
        # print(vectorizer.get_feature_names())
        

            



