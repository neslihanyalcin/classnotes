import sys, os
if sys.argv[1] == "kf":
    file = "$HOME/Dropbox/Public/skfiles/campy/chessb-right.avi"
    os.system("python track-chess-kf.py %s" % file)
if sys.argv[1] == "pf":
    file = "$HOME/Dropbox/Public/skfiles/campy/chessb-right.avi"
    os.system("python track-chess-pf.py %s" % file)
