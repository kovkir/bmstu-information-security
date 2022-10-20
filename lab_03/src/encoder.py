from bitarray import bitarray
from bitarray.util import hex2ba
from des import Des


class Encoder():
    key: bitarray
    des: Des
    lengthMsg: list 


    def __init__(self, key: str):
        self.key = self.createBinaryKey(key)
        self.des = Des(self.key)
        self.lengthMsg = list()

    
    def createBinaryKey(self, key: str):
        return bitarray(self.toBits(bytes(key, 'utf-8')))


    def toBits(self, bytesStr: bytes):
        bitsArr = hex2ba(bytesStr.hex())
        return bitsArr + bitarray("0" * (64 - len(bitsArr)))

    
    def toBytes(self, bitsArr: bitarray):
        return bitsArr.tobytes()


    def encode(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")
        
        while True:
            bytesStr = inputFile.read(8)
            if not bytesStr:
                break
            
            self.lengthMsg.append(len(bytesStr))

            bits = self.toBits(bytesStr)
            encodedBits = self.des.encode(bits)
            encodedBytes = self.toBytes(encodedBits)

            outputFile.write(encodedBytes)

        inputFile.close()
        outputFile.close()


    def decode(self, inputFileName: str, outputFileName: str):
        inputFile = open(inputFileName, "rb")
        outputFile = open(outputFileName, "wb")

        while True:
            bytesStr = inputFile.read(8)
            if not bytesStr:
                break

            bits = self.toBits(bytesStr)
            decodedBits = self.des.decode(bits)
            decodedBytes = self.toBytes(decodedBits)

            outputFile.write(decodedBytes[:self.lengthMsg.pop(0)])

        inputFile.close()
        outputFile.close()
