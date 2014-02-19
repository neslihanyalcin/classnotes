import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("""
    pdftk stat_00/stat_00.pdf intro/intro.pdf stat_summary/stat_summary.pdf \
    stat_tests/stat_tests.pdf ./stat_sample_size/stat_sample_size.pdf \
    stat_mcmc/stat_mcmc.pdf stat_coal/stat_coal.pdf \
    stat_gauss_fusion/stat_gauss_fusion.pdf stat_pandas_ratings/ratings.pdf  \
    stat_factor/stat_factor.pdf stat_wells/stat_wells.pdf \
    stat_hadoop_patent/patent.pdf stat_hadoop_kmeans/kmeans.pdf \
    stat_hadoop_logreg/stat_hadoop_logreg.pdf \
    stat_hadoop_AtA_qr/stat_AtA_qr.pdf \
    stat_hadoop_rand_proj/stat_hadoop_rand_proj.pdf \
    stat_appendix/stat_normtable.pdf \
    output ~/Dropbox/Public/skfiles/stat.pdf
    """)
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("stat*")):
        print a
        os.chdir(a)
        os.system("pdflatex -shell-escape *.tex")
        os.chdir("..")
    
if sys.argv[1] == 'clean':
    os.system("find . -name '_region_*' | xargs rm  -rf")
    
