# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:59:51 2022

@author: Kurni
"""
import os


class Input:
    def __init__(self):
        self.corpus=[];
        relativePath=os.path.dirname(__file__); 
        self.path=os.path.join(relativePath,'corpus\\bbc')

    def __call__(self) :
        arrLS=[]
        for dirContent in os.listdir(self.path):
            arrLS.append(os.path.join(self.path,dirContent))
        self.__readFileRec(arrLS)
        return self.corpus

    def __readFileRec(self,arrLS):
        for currentPath in arrLS:
            if os.path.isdir(currentPath):
                newArrLS=[]
                i=0;
                for dirContent in os.listdir(currentPath):
                        newArrLS.append(os.path.join(currentPath,dirContent))
                self.__readFileRec(newArrLS)
            else:
                self.corpus.append(currentPath)
