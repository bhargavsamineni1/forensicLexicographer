#Bhargav and Gabe

from metricAnalysis import textString, createConfidenceInt, createMetric
trainingPapers = {
    'Madison': [10, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48],
    'Hamilton': [1, 6, 7, 9, 11, 12, 13, 15, 16, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
                32, 33, 34, 36, 59, 60, 61, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
                78, 79, 80, 81, 82, 84, 85, 21, 68, 83],
    'Jay': [64, 3, 5, 4]
}

testingPapers = [14, 41, 8, 35, 17, 2]
correctTestingPaperAuthors = ['Madison', 'Madison', 'Hamilton', 'Hamilton', 'Hamilton', 'Jay']

def createMetricList(papernums):
    metricList = []
    for papernum in papernums:
        text = textString(papernum)
        metric = createMetric(text)
        metricList.append(metric)
    return metricList

authorMetricInt = {}
for author in trainingPapers:
    metricList = createMetricList(trainingPapers[author])
    metricInt = createConfidenceInt(metricList)
    authorMetricInt[author] = metricInt
'''
'Madison': (74.4534594055913, 84.70798827948809, 94.96251715338488), 
'Hamilton': (70.60489240151361, 74.1884403386395, 77.77198827576538), 
'Jay': (52.06003084662156, 71.49156125161387, 90.92309165660619)
'''

testingPapersAuthors = []
for papernum in testingPapers:
    text = textString(papernum)
    metric = createMetric(text)
    possibleAuthorsAndDist = []
    for author in authorMetricInt:
        if authorMetricInt[author][0] <= metric <= authorMetricInt[author][-1]:
            distFromMean = abs(metric - authorMetricInt[author][1])
            possibleAuthorsAndDist.append([author, distFromMean])

    if len(possibleAuthorsAndDist) == 0:
        testingPapersAuthors.append('Cannot Determine')
    elif len(possibleAuthorsAndDist) > 1:
        distances = [author[1] for author in possibleAuthorsAndDist]
        minDist = distances[0]
        for dist in distances:
            if dist < minDist:
                minDist = dist
        minDistIndex = distances.index(minDist)
        testingPapersAuthors.append(possibleAuthorsAndDist[minDistIndex][0])
    else:
        testingPapersAuthors.append(possibleAuthorsAndDist[0][0])

print('Paper Num  Actual Author  Author Guess')
print('--------------------------------------')
accurateCount = 0
for i in range(len(testingPapersAuthors)):
    print(str(testingPapers[i]).ljust(11) + correctTestingPaperAuthors[i].ljust(15) + 
            testingPapersAuthors[i])
    if correctTestingPaperAuthors[i] == testingPapersAuthors[i]:
        accurateCount += 1
print('\nAccuracy:', accurateCount/len(testingPapersAuthors))

'''
Paper Num  Actual Author  Author Guess
--------------------------------------
14         Madison        Madison
41         Madison        Madison
8          Hamilton       Jay
35         Hamilton       Hamilton
17         Hamilton       Jay
2          Jay            Jay

Accuracy: 0.6666666666666666
'''

