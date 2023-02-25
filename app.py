import flask
import pickle

import praw
import re

import yfinance as yf
import pandas as pd
from IPython.display import HTML
import numpy as np

from pandas_datareader import data as pdr
import requests, json
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer

from datetime import date, timedelta

#from sklearn.feature_extraction.text import CountVectorizer NOT SURE WHY THIS DOESN"T WORK AND GIVES ERROR

# Use pickle to load in the pre-trained model.
with open(f'model/model.pkl', 'rb') as f:
	model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])

def main():
	if flask.request.method == 'GET':
		return(flask.render_template('main.html'))
	if flask.request.method == 'POST':
		stockname = flask.request.form['stockname']
		print(stockname)
		ticker = flask.request.form['ticker']
		print(ticker)


		
		def getX(stockName, ticker, today):

			yf.pdr_override()
			data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")


			data['indicator']=((data['Open']-data['Close'])>0)*1

			#print(data)

			#aapl=yf.Ticker("AAPL")
			#tsla=yf.Ticker("TSLA")
			inputTicker=yf.Ticker(ticker)

			#aapl_history=aapl.history(start="2000-01-01")
			#tsla_history=tsla.history(start="2000-01-01")
			input_history=inputTicker.history(start="2000-01-01")

			DATA_SIZE=len(input_history)
			print(input_history)
			print(DATA_SIZE)

			indicator = [] #0 down 1 up
			date = [] #which date is it
			last=0
			def dump_Pandas_Timestamp (ts):
				return datetime(ts.year, ts.month,ts.day).date()

			for i in range(DATA_SIZE-1):
				indicator.append((int)(input_history['Open'][i+1]>input_history['Open'][i]))
			for i in input_history.index:
				date.append(dump_Pandas_Timestamp(i))

			date.pop() #get rid of last date because we dont know if it went up or down
			df=pd.DataFrame({'date':date, 'indicator':indicator})
			df=df.iloc[::-1]

			print("BOOP STOCKNAME: ", stockName)
			reddit = praw.Reddit(client_id='78xDxjnFWtr-grWN6gSYJQ', client_secret='-ZpQ0YJ_oO0BWeyDqWVYa9DHSpI3CA', user_agent='Jay')
			posts = []

			print("fetching latest articles")

			ml_subreddit = reddit.subreddit(stockName)
			for post in ml_subreddit.hot(limit=400):
				print("got an article!",post.title)
				posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.utcfromtimestamp(post.created).date()])
			posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'date']) 

			print("done getting the articles")
			print("we got ",len(posts)," posts. ")

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

			postsToday=0
			totalHours=24
			while(postsToday==0):
				for i in range(len(new_df['date'])):
					if(today-timedelta(hours=totalHours) <= new_df['date'][i] <= today+timedelta(hours=totalHours)):
						postsToday+=1
						new_df_today=pd.DataFrame({'date':[new_df['date'][i]], 'title':[new_df['title'][i]], 'indicator':[new_df['indicator'][i]]})
				totalHours+=12
			
			print("We got ", postsToday, " posts today.")

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
			print("length:", len(X_titles[0]))

			X = []

			for i in range(len(X_titles)):
				temp=[]
				for j in range(100-len(X_titles[i])):
					temp.append(0)
				temp.extend(new_df['history'][i])
				X.append(np.append(X_titles[i], temp ))
			


			print(len(X[0]))
			#print(X)
			
			return X, posts, input_history, True;
		
		status=False
		X_input=[]
		headlines=[]
		history=[]
		upOrDown=""
		prediction=-1

		try:
			X_input, headlines, history, status=getX(stockname, ticker, date.today())
			print(X_input)
			prediction = model.predict(X_input)[0]#this is our prediction
			print(prediction)
			upOrDown="down"
			if(prediction>0.5):
				upOrDown="up"
			print(status)
		except:
			print("program crashed")
			status=False
		
		
		return flask.render_template('main.html',
					original_input={'stockname':stockname, 'ticker':ticker, '% probability of going up':round(prediction, 4)*100, 'sentiment':upOrDown},
					status=status, 
					result=upOrDown,
					headlines=HTML(headlines.tail(10).to_html(classes='table table-stripped')),
					history=HTML(history.tail(10).to_html(classes='table table-stripped')),
					)

if __name__ == '__main__':
	app.run()

