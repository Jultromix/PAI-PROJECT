#Email:juliomoreno7217@gmail.com
#Github´s link repository: https://github.com/Jultromix/PAI-PROJECT.git  
#File´s creation date: 07/11/2022

#Context:
#From an Udacity course (Machine Learning) the scikit-learn library there are some basic tools to make classifiers
#(supervised learning) take into account features/attributes and assign a label.

import numpy as np
features = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
labels = np.array([1,1,1,2,2,2])

from sklearn.naive_bayes import GaussianNB
classifer = GaussianNB()
classifer.fit(features,labels)
print(classifer.predict([[.8,-1]]))         #result: [1]

#classifier .score(feature_test, label_test)