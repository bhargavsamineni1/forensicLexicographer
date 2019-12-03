'''
Method to compile all the text in a list of papernumbers into one string
Input: A list of the papernumbers to be combined
Output: A string that contains the contents of each paper in the input list
'''
def textString(papernums):
    textString = ''
    for num in papernums:
        f = open('data/federalist_' + str(num) + '.txt')
        textString += f.read()
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
A method that calulates the frequency distribution of word lengths in a text
Input: A string of text
Output: A dictionary where the keys are the different word lenghts and the values are the 
        frequencies of each word length relative to lengths of words in the entire text
'''
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

'''
A method that calculates the number of semicolons in a piece of text
Input: A string of text
Output: A integer representing the count of the number of semicolons in the text
'''
def semicolonCount(text):
    return text.count(';')
