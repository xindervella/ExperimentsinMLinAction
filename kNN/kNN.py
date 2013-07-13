from numpy import *
from os import listdir
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    # get the distance
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sum(sqDiffMat, axis=1)
    distance = sqDistance ** 0.5
    # print "distance:", distance
    # get the indices that sort the distance
    sortedDistanceIndicies = distance.argsort()
    # print "sortedDistanceIndicies:", sortedDistanceIndicies
    classCount = {}
    for i in xrange(k):
        voteIlable = labels[sortedDistanceIndicies[i]]
        # print "sortedDistanceIndicies[i]:", sortedDistanceIndicies[i]
        # print "voteIlable:", voteIlable
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
        # print "classCount:", classCount
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)
    # print "sortedClassCount:", sortedClassCount
    return sortedClassCount[0][0]


# group, labels = createDataSet()
# print classify0([0, 0], group, labels, 3)
# print classify0([1, 1], group, labels, 3)

def file2matrix(filename):
    f = open(filename)
    arrayOLines = f.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0: 3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

# Use Matplotlib create Scartter Img
# datingDateMat, datingLabels = file2matrix('datingTestSet.txt')
# print datingDateMat
# print datingLabels
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDateMat[:, 0], datingDateMat[:, 1], 15.0*array(datingLabels), array(datingLabels)-1)
# plt.show()


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
# normMat, ranges, minVals = autoNorm(datingDateMat)


def datingClassTest():
    hoRatio = 0.1
    datingDateMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDateMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in xrange(numTestVecs):
        classifierResult = classify0(normMat[i, :],
                                     normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print "the classifier come back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
        print "the total error rate is: %f" % (errorCount/float(numTestVecs))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year"))
    datingDateMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDateMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print "u will probably like this person: ", resultList[classifierResult-1]

# classifyPerson()


'''
handwriting class
'''


def img2vector(filename):
    returnVect = zeros((1, 1024))
    f = open(filename)
    for i in xrange(32):
        lineStr = f.readline()
        for j in xrange(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in xrange(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in xrange(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,
                                     trainingMat,
                                     hwLabels, 3)
        print "the classifier came back whit: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if classifierResult != classNumStr:
            errorCount += 1.0
            print 'X'
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))

# handwritingClassTest()
