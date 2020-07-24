
from MainPackage import mainpackage
from MainPackage.SubPackage import subpackage

mainpackage.mainpackagefunc1()
subpackage.subpackagefunc1()

if __name__ == '__main__':
    print("mymainpy am getting executed as main file")
    #myfunc()
else:
    print("I have been imported")