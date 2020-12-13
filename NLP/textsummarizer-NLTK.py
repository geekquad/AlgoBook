# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#download and install nltk, punkt as necessary packages 




#this is an extractive text summarization based on cosine similarity
#cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of angle between them
#angle will be zero if sentences are similar





#importing all the libraries

import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize



#inputting the text

text = """ Air pollution is nothing than a bit drop in the quality of air only.  The air quality comes in a bad stage through entering the solid, liquid and gas particles. This unexpected effect in the air comes due to the arrival of oxide, hydrocarbon and other toxic gases effect. The pollution can be classified according to their occurrence that kills the natural effect. However, it is seen that many pollutants come in air with the natural resource. There is no participation of the external material. The lists of this pollutant are dust, sea salt, volcanic ashes, and gases. So, there is no need to complain about external causes only. Some of the pollutants are human-made due to achieve the short term comfort. The human and natural being has adopted this pollutant.

The pollution is described as the primary and secondary pollutants. The primary pollutants are those that damage air quality and its index value directly.  The best example of the primary pollutants is that made from the exhaust fumes from the car, scooter, dust storm, thunder stroke and ash from the volcanic cell eruption. Secondary pollution is made from the chemical reaction and laboratory test for checking the quality of a certain object. To stay away from this problem, there is the utilization of the standard chemical laboratory test. """



#tokenizing the text

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

#frequency table for score of each word

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] +=1
    else:
        freqTable[word] =1



#score of each sentence

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
           if sentence in sentenceValue:
               sentenceValue[sentence] += freq
           else:
               sentenceValue[sentence] = freq


sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]



#average value

average = int(sumValues/len(sentenceValue))



#storing sentence in the summary
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2*average)):
        summary += " " + sentence
print(summary)



  



	
