from tree import Tree


class Huffman():
    frequencyTable: dict
    tree: Tree


    def __init__(self):
        self.initFrequencyTable()


    def initFrequencyTable(self):
        self.frequencyTable = {bytes([i]): 0 for i in range(256)}
    

    def fillFrequencyTable(self, bytesStr: bytes):
        for i in bytesStr:
            self.frequencyTable[bytes([i])] = bytesStr.count(i)
    

    def buildTree(self):
        self.tree = Tree(self.frequencyTable)


    def compress(self, symbol: bytes) -> str:
        # обход дерева в поисках кода переданного символа
        return self.tree.getCodeBySymbol(symbol)


    def getDecompressedSymbol(self, bitsStr: str) -> bytes:
        for i in range(1, len(bitsStr) + 1):
            # обход дерева в поисках символа переданного кода
            symbol = self.tree.getSymbolByCode(bitsStr[:i])
            # не дошли до конца дерева, надо взять больший код
            if symbol != None:
                return symbol, i


    def decompress(self, bitsStr: str) -> bytes:
        bytesStr = bytes()
        while len(bitsStr) > 0:
            byte, lenSymbol = self.getDecompressedSymbol(bitsStr)

            bytesStr += byte
            bitsStr = bitsStr[lenSymbol:]
        
        return bytesStr

