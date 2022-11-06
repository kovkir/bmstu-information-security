import subprocess
from compression import Сompression
from color import *


INPUT_DATA_FOLDER = "../inputDate/"
OUTPUT_DATA_FOLDER = "../outputDate/"


def getInputFile():
    listFiles = subprocess.getoutput("cd " + INPUT_DATA_FOLDER + " && ls").split("\n")

    print("\n{0}Выберете входной файл для сжатия алгоритмом Хафмана:{1}"
        .format(yellow, base_color))

    for i in range(len(listFiles)):
        print("\t{0}{1}.{2} {3}"
            .format(blue, i + 1, base_color, listFiles[i]))

    try:
        fileNumber = input("\n{0}Номер выбранного файла: {1}"
            .format(green, base_color))

        if int(fileNumber) <= 0:
            print("\n{0}Номер команды должен быть > 0!{1}\n"
                .format(red, base_color))
        else:
            filePath = INPUT_DATA_FOLDER + listFiles[int(fileNumber) - 1]
            return filePath
    except:
        print("\n{0}Ввод некоректных данных!{1}\n"
            .format(red, base_color))


def startEncryption(filePath):
    compressor = Сompression()

    compressor.compress(
        filePath,
        OUTPUT_DATA_FOLDER + "compressed.bin")

    compressor.decompress(
        OUTPUT_DATA_FOLDER + "compressed.bin", 
        OUTPUT_DATA_FOLDER + "decompressed." + filePath.split(".")[3])


def main():
    filePath = getInputFile()

    if filePath != None:
        startEncryption(filePath)


if __name__ == "__main__":
    main()
