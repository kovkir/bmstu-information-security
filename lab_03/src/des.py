from bitarray import bitarray
from bitarray.util import ba2int, int2ba
from permuter import Permuter


class Des():
    permuter: Permuter
    keys: list


    def __init__(self, key: bitarray):
        self.permuter = Permuter()
        self.keys = self.generateKeys(key)


    def generateKeys(self, key: bitarray):
        keys = list()

        c = self.permuter.permuteC0(key)
        d = self.permuter.permuteD0(key)

        for i in range(16):
            c = c << self.permuter.si[i]
            d = c << self.permuter.si[i]

            newKey = self.permuter.permuteCP(c + d)
            keys.append(newKey)

        return keys


    def funcFeistel(self, bits: bitarray, key: bitarray):
        e = self.permuter.permuteE(bits)
        z = e ^ key

        sBlocks = bitarray()
        for k in range(8):
            # берем поочередно 6 битов из 48
            bits = z[k * 6 : (k + 1) * 6]
         
            iBits = bits[:1] + bits[5:]
            jBits = bits[1:5]

            i = ba2int(iBits)
            j = ba2int(jBits)

            sBlocks += int2ba(self.permuter.permuteSBlock(k, i * 16 + j), length=4)
        
        return self.permuter.permuteP(sBlocks)


    def encode(self, bits: bitarray):
        bits = self.permuter.permuteIP(bits)

        lPart = bits[:32]
        rPart = bits[32:]

        for i in range(16):
            tmp   = lPart.copy()
            lPart = rPart.copy()
            rPart = tmp ^ self.funcFeistel(rPart, self.keys[i])

        return self.permuter.permuteIPInverse(lPart + rPart)


    def decode(self, bits: bitarray):
        bits = self.permuter.permuteIP(bits)

        lPart = bits[:32]
        rPart = bits[32:]

        for i in range(15, -1, -1):
            tmp = rPart.copy()
            rPart = lPart.copy()
            lPart = tmp ^ self.funcFeistel(lPart, self.keys[i])

        return self.permuter.permuteIPInverse(lPart + rPart)

