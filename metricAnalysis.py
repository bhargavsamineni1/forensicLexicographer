def textString(papernums):
    textString = ''
    for num in papernums:
        f = open('data/federalist_' + str(num) + '.txt')
        textString += f.read()
        f.close()
    #print(textString)
    return textString

def splitIntoSentences(text):
    retSentences = []
    sentences = text.split('.')
    for sentence in sentences:
        sentence = sentence.replace('\n', ' ')
        sentence = sentence.strip(' ')
        retSentences.append(sentence)
    return retSentences

def averageWordsPerSentence(text):
    sentences = splitIntoSentences(text)
    wordCount = 0
    for sentence in sentences:
        words = sentence.split()
        wordCount += len(words)
    return wordCount/len(sentences)

def wordFrequencyByLength(text):
    wordLengthFreq = {}
    sentences = splitIntoSentences(text)
    totalWords = 0
    for sentence in sentences:
        sentenceNoPunc = sentence.replace(',', '')
        sentenceNoPunc = sentenceNoPunc.replace(';', '')
        words = sentence.split()
        totalWords += len(words)
        for word in words:
            if len(word) not in wordLengthFreq:
                wordLengthFreq[len(word)] = 1
            else:
                wordLengthFreq[len(word)] += 1
    
    for wordLen in wordLengthFreq:
        wordLengthFreq[wordLen] = round(wordLengthFreq[wordLen]/totalWords, 5)
    return wordLengthFreq

