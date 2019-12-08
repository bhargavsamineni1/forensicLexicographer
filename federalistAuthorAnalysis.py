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
Madison:  (54.2148893440141, 64.2363557794881, 74.25782221496209),
Hamilton: (48.683819355690446, 52.17220158863949, 55.66058382158853),
Jay:      (34.0915941681783, 52.089046251613894, 70.0864983350495)
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


