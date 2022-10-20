from bitarray import bitarray


# папки с данными о перестановках
KEYS_FOLDER     = "../data/keys/"
ENCODER_FOLDER  = "../data/encoder/"
FEISTEL_FOLDER  = "../data/feistel/"
S_BLOCKS_FOLDER = "../data/feistel/sBlocks/"


class Permuter():
    c0: list
    d0: list
    si: list
    cp: list

    ip: list
    ipInverse: list

    p: list
    e: list
    sBlocks: list


    def __init__(self):
        '''
        Для генерации раундовых ключей
        '''
        # Начальная перестановка B
        self.c0 = self.getPermutation(KEYS_FOLDER + "C0.txt")
        self.d0 = self.getPermutation(KEYS_FOLDER + "D0.txt")
        # Сдвиг Si
        self.si = self.getPermutation(KEYS_FOLDER + "Si.txt")
        # Сжимающая перестановка CP
        self.cp = self.getPermutation(KEYS_FOLDER + "CP.txt")
        
        '''
        Для шифрования и расшифрования
        '''
        # Начальная перестановка IP
        self.ip = self.getPermutation(ENCODER_FOLDER + "IP.txt")
        # Конечная перестановка IP^-1
        self.ipInverse = self.getPermutation(ENCODER_FOLDER + "IPInverse.txt")
        
        '''
        Для шифра Фейстеля
        '''
        # Расширяющая перестановка Е
        self.e = self.getPermutation(FEISTEL_FOLDER + "E.txt")
        # Завершающая перестановка в функции шифрования Р
        self.p = self.getPermutation(FEISTEL_FOLDER + "P.txt")
        # S-блоки
        self.sBlocks = self.createSBlocks()


    def getPermutation(self, path: str, reduceIndex=1):
        file = open(path, mode = "r", encoding = "utf-8-sig")
        strData = file.read()
        arrData = strData.split(" ")

        for i in range(len(arrData)):
            arrData[i] = int(arrData[i]) - reduceIndex
        
        return arrData
    

    def createSBlocks(self):
        sBlocks = list()
        for i in range(1, 9):
            sBlock = self.getPermutation(S_BLOCKS_FOLDER + str(i) + ".txt", reduceIndex=0)
            sBlocks.append(sBlock)

        return sBlocks


    def permute(self, bitsArr: bitarray, indexesArr: list):
        newBitsArr = bitarray()
        for i in indexesArr:
            newBitsArr.append(bitsArr[i])
        
        return newBitsArr

    
    def permuteC0(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.c0)

    def permuteD0(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.d0)
    
    def permuteSi(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.si)
    
    def permuteCP(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.cp)


    def permuteIP(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.ip)

    def permuteIPInverse(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.ipInverse)

    
    def permuteP(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.p)

    def permuteE(self, bitsArr: bitarray):
        return self.permute(bitsArr, self.e)

    
    def permuteSBlock(self, IndexBlock: int, IndexArr: int): 
        return self.sBlocks[IndexBlock][IndexArr]

