class Rsa():
    n: int
    dKey: int # секретный ключ
    eKey: int # открытый ключ


    def __init__(self, p: int, q: int):
        self.n = p * q
        # fi - функция Эйлера от числа n
        fi = (p - 1) * (q - 1)

        self.dKey = self.calculateDKey(fi)
        self.eKey = self.calculateEKey(self.dKey, fi)
        

    def calculateGCD(self, a: int, b: int) -> int:
        '''
        Нахождение НОД "Алгоритм Евклида"
        '''

        while b != 0:
            tmp = b
            b = a % b
            a = tmp

        return a


    def multiplyMatrices(self, a: list, b: list):
        res = [[0, 0], [0, 0]]

        # вверхния строка
        res[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        res[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]

        # нижняя строка
        res[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        res[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]

        return res


    def bezout(self, a: int, b: int) -> int:
        '''
        Расширенный алгоритм Евклида (соотношение Безу)
        '''
        # Найдем такое t, что 
        # (a * t) mod b = 1

        # соотношение Безу
        # at + by = нод(a, b) = 1 

        bCopy = b
        e = [[0, 1],
             [1, 0]]
        
        r = a % b
        while r != 0:
            matrix = [[0, 1], 
                      [1, -(a // b)]]

            e = self.multiplyMatrices(e, matrix)
            
            tmp = b
            b = a % b
            a = tmp

            r = a % b

        t = e[1][1]
        if t < 0:
            t = bCopy + t

        return t
    

    def calculateDKey(self, fi: int) -> int:
        '''
        Вычисление секретного ключа
        '''
        # d и fi -- взаимно простые числа
        d = fi // 10
        nod = -1

        while nod != 1:
            d += 1
            nod = self.calculateGCD(fi, d)

        return d

    
    def calculateEKey(self, d: int, fi: int) -> int:
        '''
        Вычисление открытого ключа
        '''
        # (e * d) mod fi = 1

        # Переход к расширенному алгоритму Евклида
        # (e * d) = k * fi + 1
        # (e * d) - k * fi = 1 <=>
        # ax + by = нод(a, b) = 1, где a = d, b = fi

        return self.bezout(d, fi)

    
    def rapidExponentiation(self, num: int, degree: int, nMod: int) -> int:
        '''
        Алгоритм быстрого возведения в степень
        '''
        res = 1
        while degree > 0:
            # если степень четная
            if degree & 1:
                res = (res * num) % nMod

            degree = degree >> 1
            num = (num * num) % nMod

        return res


    def encode(self, m: int) -> int:
        '''
        Шифрование сообщения с помощью открытого ключа
        '''
        # с = (m ^ eKey) mod n
        return self.rapidExponentiation(m, self.eKey, self.n)


    def decode(self, c: int) -> int:
        '''
        Расшифровка сообщения с помощью секретного ключа
        '''
        # m = (c ^ dKey) mod n
        return self.rapidExponentiation(c, self.dKey, self.n)
