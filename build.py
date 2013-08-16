import os, sys

if sys.argv[1] == 'zip':
    os.system("zip ~/Dropbox/classnotes.zip -y -r * --exclude=.git/* --exclude=*.pdf --exclude=*.PDF --exclude=*.aux --exclude=*.log --exclude=*.pyc  --exclude=*/*/_region* . ")
if sys.argv[1] == 'clean':
    os.system("find . -name _region_* | xargs rm -rf ")
