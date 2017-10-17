# -*- coding: UTF-8 -*-
import os
import os.path
import shutil
import tinify

fromFilePath = "fileSources"
# limitCount 对于每一个免费的key 每个月的上限是500张图片。如果图片过多，将limitCount=500
limitCount = 2
dividerDirName = "image"
# 处理key,根据不同邮箱生成的不同key，需要填写不同的邮箱
keys = ["TWfJDegbr-6KHDa4uRUAeHRtD00Il8WJ", 'TWfJDegbr-6KHDa4uRUAeHRtD00Il8WJ', 'TWfJDegbr-6KHDa4uRUAeHRtD00Il8WJ']
dirs = []


def copyFile():
    # 拷贝文件到不同文件夹
    for root, dirs, files in os.walk(fromFilePath):
        for i in range(0, len(files)):
            nameIndex = (int)(i / limitCount)
            dirName = dividerDirName + str(nameIndex)
            if not os.path.exists(dirName):
                os.mkdir(dirName)
                file = files[i]
                filepath = root + "/" + file
                if file:
                    shutil.copy(filepath, dirName)
            else:
                file = files[i]
                filepath = root + "/" + file
                if file:
                    shutil.copy(filepath, dirName)

            if dirName not in dirs:
                dirs.append(dirName)

        return dirs

        pass


def processImage(fromFilePath, toFilePath, key):
    i = 0;
    print("startProcess")
    tinify.key = key
    for root, dirs, files in os.walk(fromFilePath):
        for name in files:
            fileName, fileSuffix = os.path.splitext(name)
            if fileSuffix == '.png' or fileSuffix == '.jpg':
                toFullPath = toFilePath + root[len(fromFilePath):]
                toFullName = toFullPath + '/' + name
                fromFullPath = fromFilePath + root[len(fromFilePath):]
                fromFullName = fromFullPath + '/' + name
                if os.path.isdir(toFullPath):
                    pass
                else:
                    os.mkdir(toFullPath)
                print("index....." + str(i))
                print("processing....." + str(name))
                source = tinify.from_file(fromFullName)
                source.to_file(toFullName)
                i = i + 1
    pass


if __name__ == '__main__':
    dirsN = copyFile()
    for i in range(0, len(dirsN)):
        fromFilePath = dirsN[i]
        toFilePath = "toSources" + str(i)
        key = keys[i]
        processImage(fromFilePath, toFilePath, key)
