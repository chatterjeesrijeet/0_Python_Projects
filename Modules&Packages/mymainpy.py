
from mymodule import myfunc

# the moment we import a module all the indentetion level 0 codes will run 
# so here mymoodule has __name__ == __main__ check at indentation level 0  which runs 

print("I am at indentation 0 ")

myfunc()

if __name__ == '__main__':
    print("mymainpy am getting executed as main file")
    #myfunc()