import sys

file_name = sys.argv[1]             #stores the file name from the command line

[print(','.join(x.split())) for x in open(file_name).readlines() if len(x.split())>0] 
                                    #Looks for whitespace to tokenize at and inserts the ","

