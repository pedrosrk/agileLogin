from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class sentiment:
  def __init__(self, message=''):
    self.text = message
  
  def get_text(self):
    return self.text

  def set_text(self, msg):
    self.text = msg

  def show_message (self):
    if self.get_text():
      print("The message is: " + self.get_text())
    else:
      print("Please set you message!")
  
  def englishSentiment(self):       
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(self.text)
    return scores

  def sentimentMultinomialNBModel(self):
    dataset = pd.read_csv('api/Tweets_Mg.csv',encoding='utf-8') #production
    #dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8') #test
    tweets = dataset["Text"].values
    classes = dataset["Classificacao"].values
    vectorizer = CountVectorizer(analyzer = "word")
    freq_tweets = vectorizer.fit_transform(tweets)
    modelo = MultinomialNB()
    modelo.fit(freq_tweets, classes)    
    example = [self.text]
    freq_teste = vectorizer.transform(example)
    return modelo.predict(freq_teste)[0]

  def __del__(self):
        pass #print('Destructor called')

if __name__ == "__main__":
    data = sentiment("I love you!")
    print(data.englishSentiment())
    data.set_text("Esse governo está no início, vamos ver o que vai dar")
    print(data.sentimentMultinomialNBModel())

    