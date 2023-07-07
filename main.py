import sys
from tablepull import tablepuller

def main():
    if (len(sys.argv) < 2):
        print("Error: not enough arguments")
        quit()
    theTablePuller = tablepuller()  
    theTablePuller.pull(sys.argv[1])
main()