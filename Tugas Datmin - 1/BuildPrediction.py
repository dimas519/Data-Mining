from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB as NBC
from sklearn.naive_bayes import MultinomialNB as MNBC

from sklearn.tree import DecisionTreeClassifier as DT

from sklearn.metrics import confusion_matrix as CM
from sklearn import metrics
import pickle as pkl



class buildPrecition:
    def __call__(self, vectorDocuments):
        algorithm=self.trainTestClassifier(vectorDocuments)
        self.__makePickle(algorithm)

    def trainTestClassifier(self,vectorDocuments):
        jumlahKolom=len(vectorDocuments.columns)
        fitur=vectorDocuments.iloc[:, :jumlahKolom-1]
        xtrain, xtest, ytrain, ytest = train_test_split(fitur, vectorDocuments['konten'],test_size=0.3,random_state=1)
        nbc = NBC()
        nbc.fit(xtrain, ytrain)
        yPred = nbc.predict(xtest)
        self.__analizeClasifierQualitY(ytest, yPred)
        return nbc

    def __makePickle(self,algorithm):
        name= open("classifier.pkl","wb")
        pkl.dump(algorithm,name)

    def __analizeClasifierQualitY(self,ytest, yPred):
        akurasi=metrics.accuracy_score(ytest, yPred)
        print(akurasi)
        matriks = CM(ytest, yPred)
        print(matriks)
