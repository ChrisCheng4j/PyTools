#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

def getFileHashCode(filename, type):
    if not (os.path.exists(filename)):
        return [False, 'File is not existed!(%s)' %filename]

    try:
        nameSpace=__import__('hashlib')
    except:
        return [False, 'There is no module of hashlib on your system.']

    try:
        func = getattr(nameSpace, type)
    except:
        return [False, "Cannot find " + type]

    sign = func()
    file = open(filename, 'rb')
    
    while True:
        data = file.read(4096)
        if not data:
            break;
        sign.update(data)
    return [True, sign.hexdigest()]

if __name__=='__main__':
    filename = sys.argv[1]

    try:
        hash=sys.argv[2]
    except:
        hash='md5'

    result = getFileHashCode(filename, hash)

    if(result[0]):
        print (filename + " >> "  + result[1])
    else:
        print(result[1])
