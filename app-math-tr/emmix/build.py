import os, sys, re

def run_command(command):
    result = []
    f = os.popen(command, "r")
    sys.stdout.flush()
    for l in f.xreadlines():
        result.append(l)
    return result

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    s = run_command("pdflatex emmix*.tex")
    os.system("evince emmix*.pdf")    
