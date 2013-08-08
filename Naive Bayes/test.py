# -*- coding:utf-8 -*-
import bayes

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
print 'p0V:\n', p0V
print 'p1V:\n', p1V
print 'pAb:\n', pAb
