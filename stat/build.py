import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk stat*/*.pdf output ~/Dropbox/Public/skfiles/stat.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("stat*")):
        os.chdir(a)
        os.system("pdflatex stat*.tex")    
        os.chdir("..")
    
    
