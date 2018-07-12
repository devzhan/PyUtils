# -*- coding: UTF-8 -*-
import os
import pathlib
from filecmp import cmp


def get_origin_dir():
    originPath = []
    currentCwd = os.getcwd()
    rootPath = os.path.join(currentCwd, "origin")
    dirList = os.listdir(rootPath)  # 列出文件夹下所有的目录与文件
    for dir in dirList:
        fileDir = os.path.join(rootPath, dir)
        if os.path.isdir(fileDir):
            filePath = os.path.join(fileDir, 'strings.xml')
            if os.path.exists(filePath):
                originPath.append(filePath)
    return originPath
    pass


def get_target_dir():
    targetPath = []
    currentCwd = os.getcwd()
    rootPath = os.path.join(currentCwd, "target")
    dirList = os.listdir(rootPath)  # 列出文件夹下所有的目录与文件
    for dir in dirList:
        fileDir = os.path.join(rootPath, dir)
        if os.path.isdir(fileDir):
            filePath = os.path.join(fileDir, 'strings.xml')
            if os.path.exists(filePath):
                targetPath.append(filePath)
    return targetPath
    pass


def read_string(param):
    file = open(param, 'r')
    lines = file.readlines()
    file.close()
    return lines
    pass


def write_string(path, param):
    print(path)
    lines = []
    with open(path) as f:
        lines = f.readlines()
    print(lines)
    f.close()
    del (lines[-1])
    contentLine = lines + param
    print(contentLine)
    fileWriter = open(path, 'w', encoding='utf-8')
    fileWriter.writelines(contentLine)
    fileWriter.close()
    pass


def main():
    originPaths = get_origin_dir()
    targetPaths = get_target_dir()
    for origin in originPaths:
        for target in targetPaths:
            tempTarget = target.replace('target', 'origin')
            if cmp(tempTarget, origin):
                if os.path.exists(origin) and os.path.exists(target):
                    originLines = read_string(origin)
                    originContent = originLines[1:]
                    write_string(target, originContent)

    pass


if __name__ == '__main__':
    main()
