class Rotor():
    alphabet: list
    alphabetRotor: list
    position: int

    def __init__(self, alphabet: list, alphabetRotor: list, position: int):
        self.alphabet = alphabet
        self.alphabetRotor = alphabetRotor
        self.position = position

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def rotate(self):
        self.position = (self.position + 1) % len(self.alphabet)

        return self.position

    def getPositionOfSymbol(self, alphabet: list, symbol):
        return alphabet.index(symbol)

    def getSymbolForwardRun(self, symbol):
        position = (self.getPositionOfSymbol(self.alphabet, symbol) 
            + self.position) % (len(self.alphabet))

        return self.alphabetRotor[position]

    def getSymbolBackRun(self, symbol):
        position = (self.getPositionOfSymbol(self.alphabetRotor, symbol) 
            - self.position) % (len(self.alphabetRotor))

        return self.alphabet[position]
