from math import log
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currrentLabel = featVec[-1]
        if currrentLabel not in labelCounts.keys():
            labelCounts[currrentLabel] = 0
        labelCounts[currrentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts.keys():
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

# test:
myData, labels = createDataSet()
# print calcShannonEnt(myData)


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# test:
# print splitDataSet(myData, 0, 1)
# print splitDataSet(myData, 1, 1)
# print splitDataSet(myData, 2, 'yes')


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in xrange(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

# test:
# print chooseBestFeatureToSplit(myData)


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classList.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    print dataSet
    print labels
    classList = [example[-1] for example in dataSet]
    print "classList: ", classList
    print "classList.count(classList[0]): ", classList.count(classList[0])
    print "classList[0]: ", classList[0]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    print "dataSet: ", dataSet
    if len(dataSet[0]) == 1:
        print "majorityCnt(classList): ", majorityCnt(classList)
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    print "bestFeat: ", bestFeat
    print "bestFeatLabel: ", bestFeatLabel
    myTree = {bestFeatLabel: {}}
    print "myTree: ", myTree
    del(labels[bestFeat])
    print "labels: ", labels
    featValues = [example[bestFeat] for example in dataSet]
    print "featValues: ", featValues
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        print "subLabels", subLabels
        myTree[bestFeatLabel][value] = createTree(
            splitDataSet(dataSet, bestFeat, value),
            subLabels)
    return myTree


