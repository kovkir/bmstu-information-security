import hashlib
from color import *
from rsa import Rsa


P = 46337
Q = 46327


class ElectronicSignature():
    rsa: Rsa

    def __init__(self):
        # p, q -- простые числа, по которым создаются открытый и секретный ключи
        self.rsa = Rsa(P, Q)


    def hashFile(self, inputFileName: str, outputFileName: str):
        '''
        Secure Hash Algorithm (SHA)
        SHA3 -- одна из нескольких криптографических хеш-функций, 
        которая принимает входные данные и выдает 512-битное (64-байтовое) значение хеш-функции. 
        Результат обычно отображается как шестнадцатеричное число длиной 128 цифр.
        '''
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "w")
        
        bytesStr = inputFile.read()
        
        hashedStr = hashlib.sha3_512(bytesStr).hexdigest()
        outputFile.write(hashedStr)

        inputFile.close()
        outputFile.close()

        print("{}\nФайл успешно захеширован.{}".format(purple, base_color))


    def encode(self, inputFileName: str, outputFileName: str):
        '''
        Постановка Электронной подписи.
        
        Ключ шифрования тут секретный, так как подпись может поставить только автор.
        Ключ расшифрования наоборот открытый.
        Поэтому ключи d и e меняются местами.
        '''
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")
        
        while True:
            bytesStr = inputFile.read(1)
            if not bytesStr:
                break
            
            encodedInt = self.rsa.decode(int.from_bytes(bytesStr, "little"))
            outputFile.write(encodedInt.to_bytes(4, byteorder="little"))

        inputFile.close()
        outputFile.close()

        print("{}Файл успешно зашифрован.{}".format(purple, base_color))


    def decode(self, inputFileName: str, outputFileName: str):
        '''
        Считывае фала с Электронной подписью.
        '''
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")
        
        while True:
            bytesStr = inputFile.read(4)
            if not bytesStr:
                break
            
            decodedInt = self.rsa.encode(int.from_bytes(bytesStr, "little"))
            outputFile.write(decodedInt.to_bytes(1, byteorder="little"))

        inputFile.close()
        outputFile.close()

        print("{}Файл успешно расшифрован.{}\n".format(purple, base_color))


    def verifyAuthenticity(self, authenticFileName: str, verifiableFileName: str):
        '''
        Проверка подлинности Электронной подписи.
        '''
        authenticFile = open(authenticFileName, "r")
        verifiableFile = open(verifiableFileName, "r")

        authenticStr = authenticFile.read()
        verifiableStr = verifiableFile.read()

        authenticFile.close()
        verifiableFile.close()

        if authenticStr == verifiableStr:
            print("{}Файл с подлинной Электронной подписью.{}\n".format(blue, base_color))
        else:
            print("{}Файл с поддельной Электронной подписью.{}\n".format(red, base_color))
    