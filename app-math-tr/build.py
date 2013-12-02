import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    cmd = "pdftk ./cover/cover.pdf ./model/model.pdf ./bases/bases.pdf \
./karesel/karesel.pdf ./quotient/quotient.pdf ./invtrig/invtrig.pdf \
./pfractions/pfractions.pdf matmult/matmult2.pdf ratio/ratio.pdf compos/compos.pdf \
./series/series.pdf poldiv/poldiv.pdf ./fundamental/fundamental.pdf  \
./cauchy/cauchy.pdf ./integral-mult/integral-mult.pdf ./lhospital/lhospital.pdf ./euler/euler.pdf \
./intexp/intexp.pdf ./taylor/taylor.pdf ./taylor2d/taylor2d.pdf ./pca/pca.pdf \
 ./pca/pcaperf.pdf ./eig/eig.pdf ./logaritma/logaritma.pdf ./complexity/complexity.pdf \
./probsolve/probsolve.pdf ./id3/id3.pdf ./knn/knn.pdf ./turev/turev.pdf \
./totaldiff/totaldiff.pdf ./eigseg/eigseg.pdf ./rayleigh/rayleigh.pdf exp/exp.pdf \
./dagilimlar/dagilimlar2.pdf ./buyuk/buyuk.pdf ./cebisev/cebisev.pdf \
./spline/spline.pdf ./ml-tr/ml-tr.pdf ./logreg/logreg2.pdf ./kmeans/kmeans.pdf ./naive/naive2.pdf  \
./simplex/simplex.pdf ./qp/qp.pdf ./svm/svm2.pdf ./fem/fem.pdf ./fourier/fourier2.pdf \
./pde-wave-deriv/pde_01.pdf ./heat-deriv/heat-deriv.pdf ./heat/heat.pdf \
./curvature/curvature.pdf ./level/level.pdf ./lk/lk.pdf ./varcalc/varcalc.pdf \
./filter/filter.pdf ./svdcluster/svdcluster2.pdf ./rndsvd/rndsvd.pdf  ./svdrecom/svdrecom.pdf \
./regularization/regular.pdf ./mixbern/stat_mixbern2.pdf ./meanshift/meanshift.pdf ./phd/phd.pdf \
output ~/Dropbox/Public/skfiles/app-math-tr.pdf "
    os.system(cmd)
    exit()

if sys.argv[1] == 'all':
    print os.listdir(".")
    for a in os.listdir("."):
        if os.path.isdir(a):
            os.chdir(a)
            os.system("pdflatex *.tex")    
            os.chdir("..")
           
    
