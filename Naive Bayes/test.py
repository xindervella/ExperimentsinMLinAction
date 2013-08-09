# -*- coding:utf-8 -*-
from numpy import *
import bayes
import feedparser

listOPosts, listClasses = bayes.loadDataSet()
# print listOPosts
# print listClasses
myVocabList = bayes.createVocabList(listOPosts)
# print myVocabList
# print bayes.setOfWords2Vec(myVocabList, listOPosts[0])
# print bayes.setOfWords2Vec(myVocabList, listOPosts[3])
trainMat = []
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
# print trainMat
p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
# print 'p0V:\n', p0V
# print 'p1V:\n', p1V
# print 'pAb:\n', pAb
testEntry = ['love', 'my', 'dalmation']
thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
# print testEntry, 'classify as: ', bayes.classifyNB(thisDoc, p0V, p1V, pAb)
testEntry = ['stupid', 'garbage']
thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
# print testEntry, 'classify as: ', bayes.classifyNB(thisDoc, p0V, p1V, pAb)
# bayes.spamTest()
# bayes.spamTest()

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
#vocabList, pSF, pNY = bayes.localWords(ny, sf)
#bayes.getTopWords(ny, sf)
