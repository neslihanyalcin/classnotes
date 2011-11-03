import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk stat*/stat*.pdf output ~/Dropbox/Public/skfiles/stat.pdf")
    exit()
    
    
