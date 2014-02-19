import os, sys

if sys.argv[1] == 'clean':
    os.system("find . -name _region_* | xargs rm -rf ")
    os.system("find . -name '*.log' | xargs rm -rf ")
    os.system("find . -name '*.aux' | xargs rm -rf ")
