#This is a module that i will load and run from other file 

def myfunc():
    print('I am inside the mymodule.py !!!!')

if __name__ == '__main__':
    print('mymodulepy am getting executed as main file!!!')
else:
    print('I have been imported!!!')