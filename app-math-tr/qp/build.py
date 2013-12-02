import os, sys

import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape qp.tex")
    os.system("evince qp.pdf")
    exit()

