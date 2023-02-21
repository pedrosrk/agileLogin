from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

  def __del__(self):
        print('Destructor called')

if __name__ == "__main__":
    data = sentiment("I love you!")
    print(data.englishSentiment())