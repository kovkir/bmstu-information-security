from random import randint, shuffle
from rotor import Rotor
from reflector import Reflector


class Enigma():
    rotorCount: int
    alphabet: list
    alphabetsRotors: list
    positions: list
    rotors: list
    reflector: Reflector

    def __init__(self, rotorCount: int):
        self.rotorCount = rotorCount
        self.alphabet = self.generateBinaryList()
        self.alphabetsRotors = self.generateAlphabetsRotors()
        self.positions = self.generateStartPositions()
        self.rotors = self.generateRotors()
        self.reflector = Reflector(self.alphabet.copy())

    def generateBinaryList(self):
        return [bytes([i]) for i in range(256)]

    def generateAlphabetsRotors(self):
        alphabetsRotors = list()

        for _ in range(self.rotorCount):
            alphabet = self.alphabet.copy()
            shuffle(alphabet)
            alphabetsRotors.append(alphabet)

        return alphabetsRotors       

    def generateStartPositions(self):
        positions = list()

        for _ in range(self.rotorCount):
            positions.append(randint(0, len(self.alphabet) - 1))

        return positions

    def generateRotors(self):
        rotors = list()

        for i in range(self.rotorCount):
            rotors.append(
                Rotor(self.alphabet, self.alphabetsRotors[i], self.positions[i]))

        return rotors

    def rotateRotors(self):
        for rotor in self.rotors:
            position = rotor.rotate()

            if position != 0:
                break

    def encodeProcess(self, symbol):
        for i in range(0, len(self.rotors)):
            symbol = self.rotors[i].getSymbolForwardRun(symbol)

        symbol = self.reflector.reflect(symbol)

        for i in range(len(self.rotors) - 1, -1, -1):
            symbol = self.rotors[i].getSymbolBackRun(symbol)

        self.rotateRotors()

        return symbol

    def encode(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")

        while True:
            byte = inputFile.read(1)
            if not byte:
                break

            encodedByte = self.encodeProcess(byte)
            outputFile.write(encodedByte)

        inputFile.close()
        outputFile.close()

    def reset(self):
        for i in range(len(self.rotors)):
            self.rotors[i].setPosition(self.positions[i])
