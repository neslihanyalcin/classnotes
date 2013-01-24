scale.cols <- function(x,s) {
  return(t(apply(x,1,function(x){x*s})))
}

idf.weight <- function(x) {
  # IDF weighting
  doc.freq <- colSums(x>0)
  print (doc.freq)
  doc.freq[doc.freq == 0] <- 1
  print (doc.freq)
  w <- log(nrow(x)/doc.freq)
  print (w)
}
nyt.frame.raw = read.csv("test.csv")
nyt.frame <- idf.weight(nyt.frame.raw)

print (scale.cols(nyt.frame.raw))

