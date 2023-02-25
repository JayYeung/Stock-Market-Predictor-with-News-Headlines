# Stock-Market-Predictor-with-News-Headlines
Created a robot that consumes news headlines and historical performance data and predicts the stock market trend with 80% accuracy

![example image](/project1.png "Example Image")

A robot that predicts stock market outcomes using: 
Past performance
Logistic regression
News articles regarding the stock
Categorizing
Details about the company/stock
Logistic regression


Data
indicator: up or down (0 or 1)
headlines: all the news articles that were published the night before (lists of string)
Financials:
Size
Profit

Which model to use (7/16): 
Logistic regression (simple)
Neural net (can be found in sklearn, mlp classifier)
Random forest classifier 
Try and get more data, tickers other than apple

(8/13): 
Look at hyper parameters in the model
Combine multiple products
Add number of comments (reddit)
Add overall market history
Already have tesla, apple, can add amc,   

(9/23): 
Find a list of subreddits with news 
Download model onto pickle 
Create folder with html  (interface), pickle (ur model), and python (interactions to heroku) 
https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7  
https://dashboard.heroku.com/apps 

(11/18)
Output of array X should only include 1 row
Fix the getX function to only work with first date
Use Sublime to put into visual studio code in app.py (in webapp)
Import relevant libraries into app.py


(1/5/22)
Get the getX to wrok
Get it to work with AI BOT
Launch it to Heroku so everybody can use it

Distribution/showcase options: 
A website or discord bot?
A local hackathon (https://www.cupertino.org/our-city/departments/parks-recreation/recreation-classes-and-activities/teen/hack-cupertino)
A research paper?!?!??! 

Questions I have: 
How can I combine multiple pieces of information


GOOGLE COLAB: https://colab.research.google.com/drive/16B1JqUOd8ZUQrqnJOqQr-U8LkaADcR5D#scrollTo=w2mHzkBetdGj 
Links
https://monkeylearn.com/blog/filtering-startup-news-machine-learning/ 
https://github.com/ranaroussi/yfinance 
https://pypi.org/project/yfinance/ 
https://github.com/ronil068/Stock-Sentiment-Analysis 



~700 data points (AAPL)
Naive Bayes Accuracy: 54%
Linear Regression: 62%
SVM: 62.5%
Neural Net: 58%
Random Forest: 59%

~700 data points (TSLA)
Naive Bayes Accuracy: 50%
Linear Regression: 54%
SVM: 56%
Neural Net: 56%
Random Forest: 56%

~700 data points + additional history of trends (TSLA and AAPL) (trained on only training data)
Naive Bayes Accuracy: 40%
Linear Regression: 44%, 100%
SVM: 75%, 100%
Neural Net: 60%, 88%
Random Forest: 60%, 88%

Plan before the last meeting: 
Public website: stock-mlv1.herokuapp.com

Code: https://colab.research.google.com/drive/16B1JqUOd8ZUQrqnJOqQr-U8LkaADcR5D#scrollTo=00NgQFkWRz4g
Private website on flask: http://127.0.0.1:5000/

Finish designing the website and making sure it doesn’t crash by 3/30 (2 weekends until then) 
Send to mentor
Come up with a video or slides presentation to showcase it by the last meeting (sometime before meeting in april) 


