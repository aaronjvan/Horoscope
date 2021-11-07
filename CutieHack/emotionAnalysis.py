import string
from collections import Counter

import matplotlib.pyplot as plt

def analyzeText(readFile, emotionFile):
    text = readFile

    # converting to lowercase
    lower_case = text.lower()

    # Removing punctuations
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # splitting text into words
    tokenized_words = cleaned_text.split()

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # Removing stop words from the tokenized words list
    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    # NLP Emotion Algorithm
    # 1) Check if the word in the final word list is also present in emotion.txt
    #  - open the emotion file
    #  - Loop through each line and clear it
    #  - Extract the word and emotion using split

    # 2) If word is present -> Add the emotion to emotion_list
    # 3) Finally count each emotion in the emotion list

    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)

    w = Counter(emotion_list)

    # split dictionary into keys and values
    keys = list(w.keys())
    values = list(w.values())

    print(keys)
    #gets the max value of the emotion count
    if(sum(values) == 0):
        print("hmm can't tell how you're feeling...listen to the happy playlist :)")
        return ' happy'

    max_value = max(values)
    #gets the iterator for the keys
    for iter in range(0, len(keys)):
        if(values[iter] == max_value):
            index = iter
            
    return keys[index]


def getStarSign(birthMonth, birthDay):
    if(birthMonth == 'January'):
        if(birthDay >= 1 and birthDay <= 19):
            return 'capricorn'
        elif(birthDay >= 20 and birthDay <= 31):
            return 'aquarius'
    elif(birthMonth == 'Feburary'):
        if(birthDay >= 1 and birthDay <= 18 ):
            return 'aquarius'
        elif(birthDay >= 19 and birthDay <= 29):
            return 'pisces'
    elif(birthMonth == 'March'):
        if(birthDay >= 1 and birthDay <= 20):
            return 'pisces'
        elif(birthDay >= 21 and birthDay <= 31):
            return 'aries'
    elif(birthMonth == 'April'):
        if(birthDay >= 1 and birthDay <= 19 ):
            return 'aries'
        elif(birthDay >= 20 and birthDay <= 30):
            return 'taurus'
    elif(birthMonth == 'May'):
        if(birthDay >= 1 and birthDay <= 20 ):
            return 'taurus'
        elif(birthDay >= 21 and birthDay <= 31):
            return 'gemini'
    elif(birthMonth == 'June'):
        if(birthDay >= 1 and birthDay <= 20 ):
            return 'gemini'
        elif(birthDay >= 21 and birthDay <= 30):
            return 'cancer'
    elif(birthMonth == 'July'):
        if(birthDay >= 1 and birthDay <= 22 ):
            return 'cancer'
        elif(birthDay >= 23 and birthDay <= 31):
            return 'leo'
    elif(birthMonth == 'August'):
        if(birthDay >= 1 and birthDay <= 22):
            return 'leo'
        elif(birthDay >= 23 and birthDay <= 31):
            return 'virgo'
    elif(birthMonth == 'September'):
        if(birthDay >= 1 and birthDay <= 22 ):
            return 'virgo'
        elif(birthDay >= 23 and birthDay <= 30):
            return 'libra'
    elif(birthMonth == 'October'):
        if(birthDay >= 1 and birthDay <= 22 ):
            return 'libra'
        elif(birthDay >= 23 and birthDay <= 31):
            return 'scorpio'
    elif(birthMonth == 'November'):
        if(birthDay >= 1 and birthDay <= 21 ):
            return 'scorpio'
        elif(birthDay >= 22 and birthDay <= 30):
            return 'sagittarius'
    elif(birthMonth == 'December'):
        if(birthDay >= 1 and birthDay <= 21 ):
            return 'sagittarius'
        elif(birthDay >= 22 and birthDay <= 31):
            return 'capricorn' 