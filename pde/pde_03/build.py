import os, sys, re

def run_command(command):
    result = []
    f = os.popen(command, "r")
    sys.stdout.flush()
    for l in f.xreadlines():
        result.append(l)
    return result

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    s = run_command("pdflatex pde*.tex")
    s = run_command("pdflatex pde*.tex")
    print s
    for ss in s: 
        f = re.search('There were multiply-defined labels', ss)
        if f: 
            print "---------------------------------------"
            print "There were multiply-defined labels"
            print "---------------------------------------"
            exit()
    os.system("evince pde*.pdf")    
