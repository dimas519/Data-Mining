# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:59:51 2022

@author: Kurni
"""
import os


class Input:
    def __init__(self):
        self.relativePath=os.path.dirname(__file__); 
        self.listOfCorpus=[]

    def __call__(self,path) :
        arrLS=[]
        for dirContent in os.listdir(path):
            arrLS.append(os.path.join(path,dirContent))

        self.__getFileRec(arrLS, self.listOfCorpus)
        documents=self.__readFile(self.listOfCorpus)
        return documents

    def __getFileRec(self,arrLS,listOfCorpus):
        for currentPath in arrLS:
            if os.path.isdir(currentPath):
                newArrLS=[]
                i=0;
                for dirContent in os.listdir(currentPath):
                        newArrLS.append(os.path.join(currentPath,dirContent))
                self.__getFileRec(newArrLS,listOfCorpus)
            else:
                self.listOfCorpus.append(currentPath)
    
    def __readFile(self,listOfCorpus):
        arrIsi=[]
        for path in listOfCorpus:
            isi=open(path,"r",encoding='latin-1').read();
            arrIsi.append(isi)
        return arrIsi

    def getFileName(self,idx):
        fileName=self.listOfCorpus[idx]
        return fileName