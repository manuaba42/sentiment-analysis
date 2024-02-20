import pandas as pd
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from pandas.core.common import random_state 
from sklearn.model_selection import GridSearchCV 
from sklearn.svm import LinearSVC

            
df = pd.read_csv('tweets_OnePiece.csv')
                 

x = df['translated_text']
y = df['sentimen']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#Vectorization
vectorizer = CountVectorizer()
vectorizer.fit(df['translated_text'])
x = vectorizer.transform(df['translated_text'])
y = df['sentimen']
x_train = vectorizer.transform(x_train)
x_test = vectorizer.transform(x_test)

for c in [0.01, 0.05, 0.25, 0.5, 0.75, 1]:
    svm = LinearSVC(C=c)
    svm.fit(x_train, y_train)
    print('Akurasi untuk c = %s: %s' %(c, accuracy_score(y_test, svm.predict(x_test))))



parameters = { 'kernel' : ['rbf', 'poly'], 'C' : [0.5, 1, 10, 100], 'gamma' : [1, 0.1, 0.01, 0.001] } 
grid_search = GridSearchCV(estimator=SVC(random_state=0), param_grid=parameters, n_jobs=6, verbose=1, scoring='accuracy') 
grid_search.fit(x_train, y_train) 
print(f'Best Score: {grid_search.best_score_}') 
best_params = grid_search.best_estimator_.get_params() 
print(f'Best Parameters:') 
for param in parameters:
    73
    print(f'\t{param}: {best_params[param]}')

y_pred = grid_search.predict(x_test) 
print(classification_report(y_test, y_pred))
