import json, sys, os
from pprint import pprint

home = os.path.expanduser("~")
sunroot =  "{home}/AppData/LocalLow/Failbetter Games/Sunless Sea".format(home=home)

l_sundata = os.listdir(sunroot)

def listdirs(path):
    o = []
    for i in os.listdir(path):
        if os.path.isdir("{p}/{i}".format(p=path, i=i)) == True:
            o.append("{p}/{i}".format(p=path, i=i))
        else:
            pass
    return o

sundirs = listdirs(sunroot)

assetdicts = {}

class sunjson:
    def __init__(self, path):
        self.isjson = 0
        if os.path.isfile(path):
            try:
                fileob = open(path)
                json.loads(fileob.read())
                fileob.close()
                self.name = os.path.basename(path)
                self.path = path
                self.status = "{path} is a json file".format(path=self.name)
                self.isjson = 1
            except ValueError as err:
                print("{path} is not a json file, or is corrupt\n{err}".format(path=path, err=err))
        else:
            if os.path.isdir(path):
                print('Provided path is a dir: {path}'.format(path=path))
            else:
                print('No such file/dir: {path}'.format(path=path))
    def readjson(self):
        try:
            fileob = open(self.path)
            fileout = json.loads(fileob.read())
            fileob.close()
            return fileout
        except Exception as err:
            return err

for i in sundirs:
    dict = {}
    assetdicts[os.path.basename(i)] = {'dir':i}
    for x in os.listdir(i):
        subdict = {}
        if ".json" in x:
            sunob = sunjson('{i}/{x}'.format(i=i, x=x))
            dict[x] = sunob
            assetdicts[os.path.basename(i)][x] = sunob
        else:
            pass

for i in assetdicts['entities']['qualities.json'].readjson():
    if (i['Id']) == 7198:
        print(i['Name'])