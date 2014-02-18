import os, sys

if sys.argv[1] == 'clean':
    os.system("find . -name _region_* | xargs rm -rf ")
