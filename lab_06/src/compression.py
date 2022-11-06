from bitarray import bitarray
from bitarray.util import hex2ba
from huffman import Huffman
from color import *


class Сompression():
    huffman: Huffman
    countBitsMsg: int 


    def __init__(self):
        self.huffman = Huffman()


    def multipleLength(self, bitsArr: bitarray, numb):
        return bitsArr + bitarray("0" * (len(bitsArr) % numb))


    def toBits(self, bytesStr: bytes):
        return hex2ba(bytesStr.hex())


    def toBytes(self, bitsArr: bitarray):
        return bitsArr.tobytes()


    def compress(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")
        
        # подсчет кол-ва разных символов в файле
        self.huffman.fillFrequencyTable(inputFile.read())
        # построения дерева от листьев к корню
        self.huffman.buildTree()
        # читать исходный файл сначала
        inputFile.seek(0)

        bitsStr = ""
        while True:
            byte = inputFile.read(1)
            if not byte:
                break
            
            bitsStr += self.huffman.compress(byte)

        self.countBitsMsg = len(bitsStr)
        bitsArr = self.multipleLength(bitarray(bitsStr), 8)

        outputFile.write(self.toBytes(bitsArr))

        inputFile.close()
        outputFile.close()

        print("\n{}Файл успешно сжат.{}".format(purple, base_color))


    def decompress(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")

        bytesStr = inputFile.read()
        if not bytesStr:
            return None
        
        bitsArr = self.toBits(bytesStr)
        bitsStr = bitsArr[:self.countBitsMsg].to01()

        decompressed = self.huffman.decompress(bitsStr)
        outputFile.write(decompressed)

        inputFile.close()
        outputFile.close()

        print("{}Файл успешно распакован.{}\n".format(purple, base_color))
