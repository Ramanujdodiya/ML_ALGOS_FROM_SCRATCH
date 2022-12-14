import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

class k_nearest_neighbours:
    
    
    def fit(self,X_train,y_train,k):
        """'fit' method takes X_train,y_train,k(no.of nearest neighbours) as arguments and saves them."""
        self.k = k
        self.X_train = X_train
        self.y_train = y_train

    
    def predict(self,X_test):
        """'predict' method takes X_test as input and returns the prediction y_pred as predicted by the trained model."""
        m_train = self.X_train.shape[0] 
        n = self.X_train.shape[1] 
        m_test = X_test.shape[0] 
        self.y_train.reshape(m_train,1)
        y_pred = np.zeros((m_test,1))
        for i in range(m_test):
          p = X_test[i,:]
          dis = np.sqrt(np.sum((p-self.X_train)**2,axis =1))         # calculating distance between training set and test example
          dis = dis.reshape(m_train,1)
          dis = np.hstack((dis,self.y_train))
          dis = dis[np.argsort(dis[:,0])]                            # sorting distances 
          near_neighbours = dis[0:self.k,1]                          # storing the first k indices
          y_pred[i][0] = stats.mode(near_neighbours)[0][0]           # finding mode of the indices
        return y_pred.flatten()
        
    # Computes Accuracy
    def accuracy(self,y_test,y_pred):
        m = len(y_test)
        sum1=0
        for i in range(m):
          if(y_test[i]==y_pred[i]):
              sum1+=1
        return (sum1/m)*100            

    def test_train_split(self,X,y,size):
        """Splits the dataset into trainig set and test set based on input split fraction.
        takes X,y,test_size as arguments and returns X_train,X_test,y_train,y_test."""
        m_test = int(X.shape[0]*size)
        X_test = X[0:m_test,:]
        y_test = y[0:m_test]
        X_train = X[m_test:,:]
        y_train = y[m_test:]
        return X_train,X_test,y_train,y_test   
