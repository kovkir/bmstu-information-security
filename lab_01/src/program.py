
import subprocess

def getWorkPurpose():
    print("Целью данной лабораторной работы является создание программы, которая запускается только на компьютере, на котором она была установлена.")

def getUUID():
    cmd = open('../IOPlatformUUID.txt', 'r').read()
    uuid = subprocess.getoutput(cmd)

    return uuid

def main():
    if (getUUID() == "37E292B9-771B-5FC3-B68A-0383016BE0C6"):
        getWorkPurpose()
    else:
        print("Неправильный UUID")

if __name__ == "__main__":
    main()
