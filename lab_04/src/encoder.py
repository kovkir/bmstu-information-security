from color import *
from rsa import Rsa


class Encoder():
    rsa: Rsa

    def __init__(self, max_number: str):
        # p, q -- простые числа, по которым создаются открытый и секретный ключи
        p, q = self.calculatePQ(max_number)
        self.rsa = Rsa(p, q)
        

    def calculatePQ(self, max_number: int):
        '''
        Алгоритм поиска простых чисел "Решето Эратосфена"
        '''
        arrNumb = list(numb for numb in range(2, max_number))
        lenArrNumb = len(arrNumb)

        for i in range(lenArrNumb):
            if arrNumb[i] == 0:
                continue
            
            step = arrNumb[i]
            for j in range(i + step, lenArrNumb, step):
                arrNumb[j] = 0
        
        p = 0
        q = 0
        # выбор двух последних ненулевых элементов массива
        for i in range(lenArrNumb - 1, -1, -1):
            if arrNumb[i] != 0:
                if p == 0:
                    p = arrNumb[i]
                else:
                    q = arrNumb[i]
                    break
        
        return p, q


    def encode(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")
        
        while True:
            bytesStr = inputFile.read(1)
            if not bytesStr:
                break
            
            encodedInt = self.rsa.encode(int.from_bytes(bytesStr, "little"))
            outputFile.write(encodedInt.to_bytes(4, byteorder="little"))

        inputFile.close()
        outputFile.close()

        print("{}\nФайл успешно зашифрован.{}".format(purple, base_color))


    def decode(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")
        
        while True:
            bytesStr = inputFile.read(4)
            if not bytesStr:
                break
            
            decodedInt = self.rsa.decode(int.from_bytes(bytesStr, "little"))
            outputFile.write(decodedInt.to_bytes(1, byteorder="little"))

        inputFile.close()
        outputFile.close()

        print("{}Файл успешно расшифрован.{}\n".format(purple, base_color))
