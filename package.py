# -*- coding: utf-8 -*-

import os
import sys
import zipfile
import shutil

if __name__ == '__main__':
    apkFile = sys.argv[1]
    apk = apkFile.split('.apk')[0]
    emptyFile = 'empty.txt'
    f = open(emptyFile, 'w')
    f.close
    with open('/home/chrischeng/channels.txt', 'r') as f:
        contents = f.read()
    lines = contents.split('\n')
    os.mkdir('./release')

    for channel in lines:
        destfile = './release/%s_%s.apk' % (apk, channel)
        shutil.copy(apkFile, destfile)
        zipped = zipfile.ZipFile(destfile, 'a')
        channelFile = "META-INF/{channelname}".format(channelname=channel)
        zipped.write(emptyFile, channelFile)
        zipped.close()
    os.remove('./empty.txt')
