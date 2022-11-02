from BuildPrediction import buildPrecition
from Input import Input
from TokenizingCorpus import TokenizingCorpus
from Prediksi import Prediction

#untuk debug
import os
os.system('cls||clear')

#READ THE FILE
dataSetPath='corpus\\bbc'
input=Input()
documents=input(dataSetPath)


minimumKemunculan=5


#BIKIN VECTOR
tokenizing=TokenizingCorpus(minimumKemunculan)
DataFrameDocument=tokenizing(documents)
# print(DataFrameDocument.head())

#build Prediction
bp=buildPrecition()
bp(DataFrameDocument)


#TEST DATA
testSetData='Tester'
documentTest=input(testSetData)


#BIKIN VECTOR tess
dataFrameTest=tokenizing.tokenizingTest(documentTest)
print(dataFrameTest.head())

prediction=Prediction()
hasil=prediction(dataFrameTest)
print(hasil)
