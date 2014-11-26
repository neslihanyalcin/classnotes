## Turkce

ODE, Cok Degiskenli Calculus, Lineer Cebir, Hesapsal Bilim,
Istatistik, Fonksiyonel Analiz video derslerinden, ya da ders
kitaplarindan alinan notlarin Latex ile yazilmis ve PDF olarak
uretilmis dosyalari burada bulunabilir. Matematik ve Uygulamali
Matematik hakkinda yazilmis yazilarimiz da var. Ornek Python kodlari
gerektigi yerde yazi icinde ya da onunla beraber ayni dizinde
olacaktir.

Dokumanlarin icinde gorulen kod python/ipython ortami icinden
isletilebilir. ipython kurmak icin

```
http://ipython.org/install.html
```

Kurulum olarak en acisiz kurulum Anaconda uzerinden

```
http://continuum.io/downloads
```

Komut satirindan [1] ipython baslatmak icin

```
ipython notebook --pylab=inline
```

kullanilabilir. Tabii bu durumda belgelerde gorulen kodlar elle
girilecektir. Eger kodlari not defteri disinda, dosya bazli, pur
Python olarak isletmek isterseniz, import

```
import numpy as np
import matploblib.pylab as plt
```

ibarelerini script'in basina eklemek gerekir. Bu durumda kodlar
`dosya.py` gibi bir dosya icinde kaydedilir, ve `python dosya.py` ile
komut satirindan isletilir. 

Not: Cetrefil bir kullanim, Emacs / LaTeX dokumanlarin *icinden*
Python kodlarini pytexipy-notebook adli bir teknoloji uzerinden direk
belge icinde isletmek (arka planda ipython'a baglaniyor, yani ayni
temel yapi kullaniliyor). Bu durumda, pytexipy-notebook kuruldugunda
ve Emacs icinden cagirildiginda o gereken tum ipython ayarlari kendisi
yapiyor.


[1] Komut satiri nedir? Windows uzerindeyseniz `Start | All Programs |
Accessories | Command Prompt` ile baslatilir. Terminal usulu metin
bazli bir iletisim aracidir. Ubuntu uzerinde `Applications |
Accessories | Terminal` ile baslatilabilir. Kodlari ve dokumanlari
nereye actiysaniz, o dizine komut satirindan `cd [dizin ismi]` ile
gidebilirsiniz, ve buradan ipyton komutunu isletebilirsiniz.

## English

Here are lecture notes in ODE, Multivariate Calculus, Linear Algebra,
Computational Science, Statistics, Functional Analysis classes written
in Latex, in Turkish. There is also a small handbook of collected math,
applied math articles. All necessary Python code is also shared[ in
the same directory as the article / classnote.

--

Blog

http://sayilarvekuramlar.blogspot.com

Classnotes

https://dl.dropboxusercontent.com/u/1570604/skfiles/app-math-tr.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/ode_mattuck.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/compscieng1.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/compscieng2.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/linear_strang.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/multivar_calculus.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/stat.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/pde.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/functional_analysis.pdf

## Latex Format

The format of these documents, fonts, the pseudocode look-and-feel was
taken from Andrew Cotter's thesis called *Stochastic Optimization for
Machine Learning*.

