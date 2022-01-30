"""
  Wordle Solver (or at least gives you some help)
"""

from typing import List

logFile = None
words = None


def valid(word: str, lettersThatArePresent: List, lettersThatAreNotPresent: List, lettersThatAreInAPosition: List, lettersThatAreNotInAPosition: List):
    '''
      Return true if the word passed in meets all the constraints we have found for it.
    '''

    if len(word) != 5:
        return False

    # All of these letters must be in the word
    for letter in lettersThatArePresent:
        if word.find(letter) == -1:
            return False

    # None of these letters should be in the word
    for letter in lettersThatAreNotPresent:
        if word.find(letter) != -1:
            return False

    # These letters must be in the position passed in
    for letter, index in lettersThatAreInAPosition:
        if word.find(letter) != index:
            return False
        
    # These letters are not in position passed in
    for letter, index in lettersThatAreNotInAPosition:
        if word.index(letter) == index:
            return False

    return True

    
def main():
    global logFile
    global words
    
    words = dict()
    
    with open('5LetterWords.txt', 'r') as f:
        for line in f:
            cleanLine = line.replace('\n', '')
            words[cleanLine] = 1
                
    numWords = 0
    freqDict = {}
    lettersThatArePresent = ['r', 'u', 'n']
    lettersThatAreNotPresent = ['t', 'e', 'a', 's', 'i', 'o', 'y', 'd', 'k']
    lettersThatAreInAPosition = [('r', 1), ('u', 2), ('n', 3)]
    lettersThatAreNotInAPosition = [('r', 3)]
    for word, _ in words.items():
        if valid(word, lettersThatArePresent, lettersThatAreNotPresent, lettersThatAreInAPosition, lettersThatAreNotInAPosition):

            for letter in word:
                if letter in freqDict:
                    freqDict[letter] += 1
                else:
                    freqDict[letter] = 1


            # if word.count('o') >= 1 and word.count('i') >= 1:
            print(word)
            numWords += 1

    print(f"{numWords} words found.")
    letterList = []
    for k, v in freqDict.items():
        if k not in lettersThatArePresent:
            letterList.append((v, k))
    letterList = sorted(letterList, reverse=True)[:10]
    print(letterList)

    
    
main()