'''
Method to return to contents of a text as a string
Input: A integer representing the paper to return as a string
Output: A string that contains the contents of the paper
'''
def textString(papernum):
    f = open('data/federalist_' + str(papernum) + '.txt')
    textString = f.read()
    f.close()
    return textString

'''
A method that splits a body of text into a list of sentences
Input: A string of text
Output: A list of sentences that are stripped of newline characters and trailing/leading spaces
'''
def splitIntoSentences(text):
    retSentences = []
    sentences = text.split('.')
    for sentence in sentences:
        sentence = sentence.replace('\n', ' ')
        sentence = sentence.strip(' ')
        retSentences.append(sentence)
    return retSentences

'''
A method that calculates the average words per sentence in a text
Input: A string of text
Output: A float representing the average words used in a sentence
'''
def averageWordsPerSentence(text):
    sentences = splitIntoSentences(text)
    wordCount = 0
    for sentence in sentences:
        words = sentence.split()
        wordCount += len(words)
    return wordCount/len(sentences)

'''
A method that calulates the frequency of words of length 2 in a text
Input: A string of text
Output: An integer representing the frequency of words of length 2 in the text
'''
def wordFrequencyOfLengthTwo(text):
    lengthTwoCount = 0
    sentences = splitIntoSentences(text)
    totalWords = 0
    for sentence in sentences:
        sentenceNoPunc = sentence.replace(',', '')
        sentenceNoPunc = sentenceNoPunc.replace(';', '')
        words = sentence.split()
        totalWords += len(words)
        for word in words:
            if len(word) == 2:
                lengthTwoCount += 1

    return round(lengthTwoCount/totalWords, 5)

'''
A method that calculates the number of semicolons in a piece of text
Input: A string of text
Output: A integer representing the count of the number of semicolons in the text
'''
def semicolonCount(text):
    return text.count(';')

'''
A method that creates the metric that the text will be tested on
Input: A string of text
Output: A float that is the sum of the semicolon count, the avg words per sentence, and the 
        frequnecy of words of length 2 * 100 in the text
'''
def createMetric(text):
    wordLengthTwoFreq = wordFrequencyOfLengthTwo(text)
    semiCount = semicolonCount(text)
    avgWordsSentence = averageWordsPerSentence(text)
    metric = wordLengthTwoFreq + semiCount + avgWordsSentence
    return metric

'''
A method that creates a 99% confidence interval using the t distribution
Input: A list of metrics that correspond to a text
Output: A tuple that denotes a 99% confidence interval for the population mean metric
        of the author
'''
def createConfidenceInt(metricList):
    #alpha = .05
    df = len(metricList) - 1
    critVals = {11: 3.106, 47: 2.704, 3: 5.841}

    sampleMean = sum([metric for metric in metricList]) / len(metricList)
    sampleSD = (sum([(metric-sampleMean)**2 for metric in metricList]) / df) ** .5
    critVal = critVals[df]
    error = critVal * sampleSD / (len(metricList)**.5)
    return (sampleMean - error, sampleMean, sampleMean + error)
