import subprocess

programFile = \
'''
import subprocess

def getWorkPurpose():
    print("Целью данной лабораторной работы является создание программы, которая запускается только на компьютере, на котором она была установлена.")

def getUUID():
    cmd = open('../IOPlatformUUID.txt', 'r').read()
    uuid = subprocess.getoutput(cmd)

    return uuid

def main():
    if (getUUID() == "{0}"):
        getWorkPurpose()
    else:
        print("Неправильный UUID")

if __name__ == "__main__":
    main()
'''

def getUUID():
    # universally unique identifier "универсальный уникальный идентификатор"
    # UUID аппаратного обеспечения
    cmd = open('../IOPlatformUUID.txt', 'r').read()
    uuid = subprocess.getoutput(cmd)
    print("Ваш универсальный уникальный идентификатор: ", uuid)

    return uuid

def createProgramFile(uuid: str):
    open('./program.py', 'w').write(programFile.format(uuid))

def main():
    uuid = getUUID()
    createProgramFile(uuid)

if __name__ == "__main__":
    main()
