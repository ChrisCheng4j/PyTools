#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import hashlib

def checkValid(filepath, type):
    if not (os.path.exists(filepath)):
        return [False, 'File is not existed!(%s)' %filepath]

    try:
        nameSpace=__import__('hashlib')
    except:
        return [False, 'There is no module of hashlib on your system.']

    try:
        func = getattr(nameSpace, type)
        sign = func()
        return [True, "Suc"]
    except:
        return [False, "Cannot find " + type]

def traversal(output, filepath, type):
    if (os.path.isfile(filepath)):
        saveHashToFile(output, filepath)
    if (os.path.isdir(filepath)):
        for filename in os.listdir(filepath):
            traversal(output, os.path.join(filepath, filename), type)

def saveHashToFile(output, filename):
    file = open(filename, 'rb')

    while True:
        data = file.read(4096)
        if not data:
            break;
        sign = hashlib.md5()
        sign.update(data)

    output.writelines(file.name.split('/')[-1] + " >>> " + sign.hexdigest() + '\r\n')
    file.close

if __name__=='__main__':
    filepath = sys.argv[1]

    try:
        hash=sys.argv[2]
    except:
        hash='md5'

    isValid = checkValid(filepath, hash)
    if (isValid[0]):
        with open('/home/chrischeng/TestHash.txt', 'w') as output:
            traversal(output, filepath, hash)
    else :
        print(result[1])
