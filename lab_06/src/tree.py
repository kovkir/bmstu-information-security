class Node():
    symbols: bytes
    frequency: int
    value: str


    def __init__(self, symbols, frequency, left=None, right=None):
        self.symbols = symbols
        self.frequency = frequency
        self.value = ""

        self.left  = left
        self.right = right


class Tree():
    tree: Node


    def __init__(self, frequencyTable: dict):
        self.nodes: list[Node] = list()
        self.addNodes(frequencyTable)

        self.tree = self.buildTree()
        self.fillValueNode(self.tree)


    def addNodes(self, frequencyTable: dict):
        for key in frequencyTable.keys():
            if frequencyTable[key] > 0:
                self.nodes.append(
                    Node(key, frequencyTable[key])
                )


    def indexMinElem(self) -> int:
        iMinElem = 0
        for i in range(1, len(self.nodes)):
            if self.nodes[i].frequency < self.nodes[iMinElem].frequency:
                iMinElem = i

        return iMinElem


    def buildTree(self) -> Node:
        while len(self.nodes) > 1:
            firstNode = self.nodes.pop(self.indexMinElem())
            secondNode = self.nodes.pop(self.indexMinElem())

            self.nodes.append(
                Node(firstNode.symbols + secondNode.symbols, 
                     firstNode.frequency + secondNode.frequency,
                     firstNode, secondNode)
            )

        return self.nodes[0]


    def fillValueNode(self, node: Node):
        if node.left != None:
            node.left.value += node.value + "0"
            self.fillValueNode(node.left)
        
        if node.right != None:
            node.right.value += node.value + "1"
            self.fillValueNode(node.right)


    def searchCodeBySymbol(self, symbol: bytes, node: Node) -> str:
        if node.symbols == symbol:
            code = node.value 
        # есть ли искомый символ в левой части дерева
        elif node.left.symbols.find(symbol) > -1:
            code = self.searchCodeBySymbol(symbol, node.left)
        # есть ли искомый символ в правой части дерева
        else:
            code = self.searchCodeBySymbol(symbol, node.right)

        return code


    def getCodeBySymbol(self, symbol: bytes) -> str:
        return self.searchCodeBySymbol(symbol, self.tree)
       

    def searchSymbolByCode(self, code: str, node: Node) -> bytes:
        if len(code) == 0:
            # не дошли до конца дерева, надо взять больший код
            if node.left != None or node.left != None:
                symbol = None
            else:
                symbol = node.symbols 

        # есть ли искомый символ в левой части дерева
        elif node.left.value[-1] == code[0]:
            symbol = self.searchSymbolByCode(code[1:], node.left)
        # есть ли искомый символ в правой части дерева
        else:
            symbol = self.searchSymbolByCode(code[1:], node.right)

        return symbol


    def getSymbolByCode(self, code: str) -> bytes:
        return self.searchSymbolByCode(code, self.tree)

