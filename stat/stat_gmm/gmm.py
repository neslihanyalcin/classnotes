import numpy as np
from sklearn.preprocessing import normalize
from sklearn.cross_validation import train_test_split
from sklearn.metrics import roc_curve, auc
from sklearn.mixture import GMM
from sklearn.metrics import roc_auc_score, matthews_corrcoef, accuracy_score
import pandas as pd

class GMMClassifier():
   def __init__(self,k,var):
       self.clfs = [GMM(n_components=k,covariance_type=var) for i in range(2)]

   def fit(self,X,y):
       self.clfs[0].fit(X[y==0])
       self.clfs[1].fit(X[y==1])

   def predict(self,X):
       res0 = self.clfs[0].score(X)
       res1 = self.clfs[1].score(X)
       return (res1 > res0).astype(float)

def main():
   df = pd.read_csv('./skin.csv')
   y = (df['skin'] == True).astype(float)
   X = df[['h','s','v','r']]

   res = []
   for i in range(4):
      clf = GMMClassifier(k=5,var='full')
      x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=2000)
      clf.fit(x_train,y_train)
      preds = clf.predict(x_test)

      fpr, tpr, thresholds = roc_curve(y_test, preds)

      break

      s = []
      s.append( matthews_corrcoef(y_test,preds) )
      s.append( accuracy_score(y_test,preds) )
      s.append( auc(fpr, tpr) )

      res.append( s )

      #res.append(roc_auc)

   return np.asarray(res)

