'''
AUTHOR: Danie Strijdom (d.strijdom@gmail.com)
Python 2.7.12

NOTES:

Scientific:
Classifier used is K Nearest neighbors.
K is approximated but not optimised due to time contraints.

Observations:
The confusion matrix shows an acceptable degree of accuracy. Noteworthy however there is an error cluster between the
models interpretation of the number 4, 8 and 9, which can be intuitively explained.
The experiment was done with both uniform and distance weightings and as suspected the distance weighting achieved
much higher accuracy.
Finally, even at 0.94 accuracy, the performance is perhaps a bit poor considering the images are fairly simple in nature
and that optimised models on similar datasets outperform this accuracy level. Optimising K and repeating the experiment
with variations of the KNN family of algorithms would likely improve results.
'''

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import MySQLdb
import math

'''
1: Get data from server
'''

HOST = '173.45.91.18'
USER = 'user04'
PASS = 'KHpz5M18Xkix'
DB_NAME = 'mnist04'

db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB_NAME)
c = db.cursor()

# train data NB: 44222 images
c.execute('SELECT * FROM mnist_train')
training_data = c.fetchall()

# test data
c.execute('SELECT * FROM mnist_test')
test_data = c.fetchall()

c.close()

print "\n- Data read..."


'''
2: Clean and sort data into training and test sets
'''

X_train = []
y_train = []

for image in training_data:
    y_train.append(image[1].split(',')[0])
    X_train.append(image[1].split(',')[1:])

X_test = []
y_test = []

for image in test_data:
    y_test.append(image[1].split(',')[0])
    X_test.append(image[1].split(',')[1:])

print "- Data sorted..."


'''
3: Choose classifier and parameters
'''

# NOTE: N can be optimised by running experiments through a number of N values and evaluating which
# the inflection point where accuracy is higheset and error rate lowest.
# In this instance I lack the time and processing power to run these experiments so I chose the log of the training
# sample size, which seems to be a fair compromise in the general case.

N = int(math.ceil(math.log10(len(X_test))))

# NOTE: distance weighted classifier has a higher precision
clf = KNeighborsClassifier(n_neighbors=N, weights='distance')
clf.fit(X_train, y_train)

print "- KNN model fitted, N: ", str(N)


'''
4: Use model to predict, construct confusion matrix
'''

# NOTE: Better result can be obtained from, in this case, doing leave-one-out cross validation (LOOCV).
# Once more because of time contrstaints I am skipping this step

print "\n- Prediction start..."

pred = clf.predict(X_test)
print "- Prediction done..."

accuracy = accuracy_score(y_true=y_test,y_pred=pred)

print '''\n
-----------
# RESULTS #
-----------

Accuracy:   {}

'''.format(accuracy)

print "\nClassification Report:"
print classification_report(y_true=y_test,y_pred=pred)

lables = [str(i) for i in range(10)]
print '\nConfusion Matrix:'
print confusion_matrix(y_true=y_test, y_pred=pred, labels=lables)

print '''\n
-------
# END #
-------
'''
