# -*- coding: utf-8 -*-
"""Stock Market Prediction Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16B1JqUOd8ZUQrqnJOqQr-U8LkaADcR5D
"""

!pip install yfinance --upgrade --no-cache-dir
!pip install pandas_datareader
!pip install scrapy
!pip install shub
!pip install praw

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pandas_datareader import data as pdr
import requests, json
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer


yf.pdr_override()
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")


data['indicator']=((data['Open']-data['Close'])>0)*1

#print(data)

aapl=yf.Ticker("AAPL")
tsla=yf.Ticker("TSLA")

def dump_Pandas_Timestamp (ts):
    return datetime(ts.year, ts.month,ts.day).date()

aapl_history=aapl.history(start="2000-01-01")
tsla_history=tsla.history(start="2000-01-01")
DATA_SIZE=len(tsla_history)
print(tsla_history)
print(DATA_SIZE)

indicator = [] #0 down 1 up
date = [] #which date is it
last=0
for i in range(DATA_SIZE-1):
  indicator.append((int)(tsla_history['Open'][i+1]>tsla_history['Open'][i]))
for i in tsla_history.index:
  date.append(dump_Pandas_Timestamp(i))

date.pop() #get rid of last date because we dont know if it went up or down
df=pd.DataFrame({'date':date, 'indicator':indicator})
df=df.iloc[::-1]
df

"""# HELPER FUNCTIONS """

import praw
import re
from sklearn.feature_extraction.text import TfidfTransformer
 
def getData(stockName):  
  reddit = praw.Reddit(client_id='78xDxjnFWtr-grWN6gSYJQ', client_secret='-ZpQ0YJ_oO0BWeyDqWVYa9DHSpI3CA', user_agent='Jay')
  posts = []

  ml_subreddit = reddit.subreddit(stockName)
  for post in ml_subreddit.hot(limit=None):
      posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.utcfromtimestamp(post.created).date()])
  posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'date'])
  posts 

  unique_date=[]
  for i in range(len(posts)):
    if(posts['date'][i] not in unique_date):
      unique_date.append(posts['date'][i])

  unique_date=sorted(unique_date)

  new_df_date=[]
  new_df_title=[]
  new_df_indicator=[]

  for i in unique_date:
    s=""
    index=0
    found=False
    for j in range(len(posts)):
      if(posts['date'][j]==i):
        s+=(posts['title'][j]+" ")
        for k in range(len(df)):
          if(df['date'][k]==i):
            index=k
            found=True
            break
    if(found):
      new_df_date.append(i)
      new_df_title.append(s)
      new_df_indicator.append(df['indicator'][index])

    
  new_df=pd.DataFrame({'date':new_df_date, 'title':new_df_title, 'indicator':new_df_indicator})
  new_df_history=[]
  LEN_HISTORY=5

  for i in range(LEN_HISTORY):
    new_df_history.append([0,0,0,0,0])
  for i in range(LEN_HISTORY, len(new_df)):
    temp=[]
    for j in range(i-LEN_HISTORY, i):
      temp.append(new_df['indicator'][j])
    new_df_history.append(temp)
  new_df['history']=new_df_history
  #new_df
  posts=posts.sort_values(by=['date'])
  #posts
  
  better_title=[]
  nltk.download('punkt')
  nltk.download('stopwords')
  stemmer = PorterStemmer()

  for i in new_df['title']:
    sms=re.sub('[^A-Za-z]', ' ', i).lower()
    tokenized_sms = word_tokenize(sms)
    for word in tokenized_sms:
      if word in stopwords.words('english'):
          tokenized_sms.remove(word)
    for i in range(len(tokenized_sms)):
      tokenized_sms[i] = stemmer.stem(tokenized_sms[i])
    
    better_title.append(tokenized_sms)
    ONEd_title=[]
  for i in better_title:
    s=""
    for j in i:
      s+=j
      s+=" "
    ONEd_title.append(s)
  TF_transformer = TfidfTransformer().fit_transform(ONEd_title)
  X_titles = TF_transformer.fit_transform

  X = []

  for i in range(len(X_titles)):
    X.append(np.append(X_titles[i], new_df['history'][i]))
  print(len(X[0]))
  print(X[0])
  y = new_df.iloc[:, 2]  

  return X, y ;

#in between to avoid teleporting

import praw
import re
 
def getX(stockName, today):  
  reddit = praw.Reddit(client_id='78xDxjnFWtr-grWN6gSYJQ', client_secret='-ZpQ0YJ_oO0BWeyDqWVYa9DHSpI3CA', user_agent='Jay')
  posts = []

  ml_subreddit = reddit.subreddit(stockName)
  for post in ml_subreddit.hot(limit=None):
      posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.utcfromtimestamp(post.created).date()])
  posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'date'])
  posts 

  unique_date=[]
  for i in range(len(posts)):
    if(posts['date'][i] not in unique_date):
      unique_date.append(posts['date'][i])

  unique_date=sorted(unique_date)

  new_df_date=[]
  new_df_title=[]
  new_df_indicator=[]

  for i in unique_date:
    s=""
    index=0
    found=False
    for j in range(len(posts)):
      if(posts['date'][j]==i):
        s+=(posts['title'][j]+" ")
        for k in range(len(df)):
          if(df['date'][k]==i):
            index=k
            found=True
            break
    if(found):
      new_df_date.append(i)
      new_df_title.append(s)
      new_df_indicator.append(df['indicator'][index])
    else:
      new_df_date.append(i)
      new_df_title.append(s)
      new_df_indicator.append(0.5)

    
  new_df=pd.DataFrame({'date':new_df_date, 'title':new_df_title, 'indicator':new_df_indicator})
  new_df_history=[]
  LEN_HISTORY=5

  for i in range(LEN_HISTORY):
    new_df_history.append([0,0,0,0,0])
  for i in range(LEN_HISTORY, len(new_df)):
    temp=[]
    for j in range(i-LEN_HISTORY, i):
      temp.append(new_df['indicator'][j])
    new_df_history.append(temp)
  new_df['history']=new_df_history
  #new_df
  posts=posts.sort_values(by=['date'])
  #posts

  display(new_df)
  for i in range(len(new_df['date'])):
    if(new_df['date'][i]==today):
      new_df_today=pd.DataFrame({'date':[new_df['date'][i]], 'title':[new_df['title'][i]], 'indicator':[new_df['indicator'][i]]})
  
  better_title=[]
  nltk.download('punkt')
  nltk.download('stopwords')
  stemmer = PorterStemmer()

  for i in new_df_today['title']:
    sms=re.sub('[^A-Za-z]', ' ', i).lower()
    tokenized_sms = word_tokenize(sms)
    for word in tokenized_sms:
      if word in stopwords.words('english'):
          tokenized_sms.remove(word)
    for i in range(len(tokenized_sms)):
      tokenized_sms[i] = stemmer.stem(tokenized_sms[i])
    
    better_title.append(tokenized_sms)
    ONEd_title=[]
  for i in better_title:
    s=""
    for j in i:
      s+=j
      s+=" "
    ONEd_title.append(s)
  matrix = CountVectorizer(max_features=100)
  X_titles = matrix.fit_transform(ONEd_title).toarray()
  print(X_titles)

  X = []

  for i in range(len(X_titles)):
    X.append(np.append(X_titles[i], new_df['history'][i]))
  
  print(len(X[0]))
  print(X[0])

  return X;

def getDataFromList(listOfTickers): 
  listOfNames=[]
  listOfHistory=[]
  for i in listOfTickers:
    ticker=yf.Ticker(i)
    s=ticker.info['shortName'].split(' ')
    s=s[0].split(',')
    listOfNames.append(s[0])
    listOfHistory.append(ticker.history(start="2000-01-01"))
    #print(listOfNames)
    #print(listOfHistory)
  
  reddit = praw.Reddit(client_id='78xDxjnFWtr-grWN6gSYJQ', client_secret='-ZpQ0YJ_oO0BWeyDqWVYa9DHSpI3CA', user_agent='Jay')
  listOfPosts = []

  for i in listOfNames:
    ml_subreddit = reddit.subreddit(i)
    posts=[]
    for post in ml_subreddit.hot(limit=10):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.utcfromtimestamp(post.created).date()])
    listOfPosts.append(pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'date']))

    
  print(listOfPosts)

getDataFromList(["AAPL", "TSLA", "MSFT"])

from datetime import date

print(getData("apple"))
#print(getX("apple", date.today()))

def getManyData(stockList ):  
  X, y=getData(stockList[0])
  for i in stockList[1:]:
    Xtemp, Ytemp = getData(i)  
    X+=Xtemp
    y=y.append(Ytemp)  
    print(len(X), len(y))
  return X, y;

"""# MODEL TESTING"""

X, y=getManyData(["apple", "microsoft"]) 
print(X)
print(y)

print(len(X), len(y))

# split train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
print(len(X), len(y))
print(X_train)
print(X_test)

# Naive Bayes 
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predict Class
y_pred = classifier.predict(X_test)

# Accuracy 
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)

#linear regression
from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train)
predictions = logisticRegr.predict(X_test)
score = logisticRegr.score(X_test, y_test)

trainPredictions = logisticRegr.predict(X_train)
trainScore = logisticRegr.score(X_train, y_train)

print(score, trainScore)

#svm
from sklearn import model_selection, svm
svm = svm.SVC()
svm.fit(X_train, y_train)

predictions = svm.predict(X_test)
score = svm.score(X_test, y_test)

trainPredictions = svm.predict(X_train)
trainScore = svm.score(X_train, y_train)

print(score, trainScore)

#neural net sk learn
from sklearn.neural_network import MLPClassifier

bestScore=-1 
bestAlpha=-1

for i  in range(0, 15): 
  mlp= MLPClassifier(alpha=i,max_iter=5000)
  mlp.fit(X_train, y_train)

  predictions = mlp.predict(X_test)
  score = mlp.score(X_test, y_test)

  trainPredictions = mlp.predict(X_train)
  trainScore = mlp.score(X_train, y_train) 

  if(score>bestScore): 
    bestAlpha=i 
    bestScore=score 
mlp= MLPClassifier(alpha=bestAlpha,max_iter=5000)
mlp.fit(X_train, y_train)

predictions = mlp.predict(X_test)
score = mlp.score(X_test, y_test)

trainPredictions = mlp.predict(X_train)
trainScore = mlp.score(X_train, y_train)   
print(bestAlpha, score, trainScore)

print(X_train[0])
print(len(X_train[0]))

#random forest
from sklearn.ensemble import RandomForestClassifier 

from sklearn.model_selection import RandomizedSearchCV

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state = 42)
from pprint import pprint

def evaluate(model, test_features, test_labels):
    trainPredictions = model.predict(X_train)
    trainScore = model.score(X_train, y_train)

    print(score, trainScore)
    
    return score

# Look at parameters used by our current forest
print('Parameters currently in use:\n')
pprint(rf.get_params())

base_model = RandomForestRegressor(n_estimators = 10, random_state = 42)
base_model.fit(X_train, y_train)
base_accuracy = evaluate(base_model, X_train, y_train)
 
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
pprint(random_grid)
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
rf_random.fit(X_train, y_train)

best_random = rf_random.best_estimator_
random_accuracy = evaluate(best_random, X_train, y_train)

print('Improvement of {:0.2f}%.'.format( 100 * (random_accuracy - base_accuracy) / base_accuracy))

import pickle
from google.colab import files
with open('model.pkl', 'wb') as file:
  pickle.dump(best_random, file)
files.download('model.pkl')

if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':

        stockname = flask.request.form['stockname']
        print(stockname)
        X_input=getX(stockname, date.today())

        prediction=model.predict(X_input)[0] #this is our prediction

        return flask.render_template('main.html',
                                        original_input={'stockname':stockname},
                                        result=prediction,
                                        )

<!––
<!doctype html>
<html>
<style>
form {
    margin: auto;
    width: 35%;
}
.result {
    margin: auto;
    width: 35%;
    border: 1px solid #ccc;
}
</style>
<head>
    <title>Stock Prediction Model</title>
</head>
<form action="{{ url_for('main') }}" method="POST">
    <fieldset>
        <legend>Input values:</legend>
        Stock Name:
        <input name="stockname" type="string" required>
        <br>
        <input type="submit">
    </fieldset>
</form>
<br>
<div class="result" align="center">
    {% if result %}
        {% for variable, value in original_input.items() %}
            <b>{{ variable }}</b> : {{ value }}
        {% endfor %}
        <br>
        <br> {stockname} will go up in price:
           <p style="font-size:50px">{{ result }}</p>
    {% endif %}
</div>
</html>

––>