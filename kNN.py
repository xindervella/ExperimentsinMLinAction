from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0.0, 0.0], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    '''inX: input vector, dataSet: input sample set,
    labels: label vector, k: number of nearest neighbors'''
    #get the distance
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sum(sqDiffMat, axis=1)
    distance = sqDistance ** 0.5
    print "distance:", distance
    #get the indices that sort the distance
    sortedDistanceIndicies = distance.argsort()
    print "sortedDistanceIndicies:", sortedDistanceIndicies
    classCount = {}
    for i in xrange(k):
        voteIlable = labels[sortedDistanceIndicies[i]]
        print "sortedDistanceIndicies[i]:", sortedDistanceIndicies[i]
        print "voteIlable:", voteIlable
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
        print "classCount:", classCount
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "sortedClassCount:", sortedClassCount
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

datingDateMat, datingLabels = file2matrix('datingTestSet.txt')
print datingDateMat, datingLabels
