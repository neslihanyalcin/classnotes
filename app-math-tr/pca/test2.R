scale.cols <- function(x,s) {
  return(t(apply(x,1,function(x){x*s})))
}

nyt.frame.raw = read.csv("test.csv")
print (scale.cols(nyt.frame.raw,c(2,2,2,2,2)))

