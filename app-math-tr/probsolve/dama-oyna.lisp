(load "dama-deger.lisp")

(oyuna-basla *beyaz*)

(loop
 (goster *tahta*)
 (print "Hamlenizi giriniz")
 (setq insan-hamlesi (eval (read)))
 (cond ((equal (hamle-kurallara-uygunmu insan-hamlesi *tahta* "b") t)
	(progn
	  (tas-oynat insan-hamlesi *tahta*)
	  (print "su hareketi yaptiniz")
	  (print insan-hamlesi)
	  (goster *tahta*) 
	  (setq bilgisayar-hamlesi (cadr (altust-arama *tahta*)))
	  (print "bilgisayarin hareketi")
	  (print bilgisayar-hamlesi)
	  (tas-oynat bilgisayar-hamlesi *tahta*)
	  (setf bilgisayar-hamle-sayisi (+ bilgisayar-hamle-sayisi 1))
	  ))
	(t (print "HATALI HAREKET")))
 )

