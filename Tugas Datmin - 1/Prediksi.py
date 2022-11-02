
import pickle
class Prediction:
    def __call__(self,DataFrameTest):
        modelPrediksi= pickle.load(open("classifier.pkl", 'rb'))
        hasilPrediksi=modelPrediksi.predict(DataFrameTest)
        return hasilPrediksi