from random import shuffle


class Reflector():
    alphabetReflector: dict

    def __init__(self, alphabet: list):
        self.alphabetReflector = self.generateAlphabetReflector(alphabet)

    def reflect(self, symbol):
        return self.alphabetReflector[symbol]

    def generateAlphabetReflector(self, alphabet):
        shuffle(alphabet)
        alphabetDict = dict()

        for i in range(0, len(alphabet), 2):
            alphabetDict[alphabet[i]] = alphabet[i + 1]
            alphabetDict[alphabet[i + 1]] = alphabet[i]

        return alphabetDict
