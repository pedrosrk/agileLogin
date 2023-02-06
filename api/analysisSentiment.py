# First we import the relevant NLTK library modules
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class analysisSentiment():
    # the 'message_text' variable contains the text we are going to analyze.
    message_text = '''Like you, I am getting very frustrated with this process. 
                    I am genuinely trying to be as reasonable as possible. 
                    I am not trying to "hold up" the deal at the last minute. 
                    I'm afraid that I am being asked to take a fairly large leap of faith after this company 
                    (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''
    
    def __init__ (self, message = message_text):
        self.message = message

    def intensitySentiment(self):       
        # a seguir, inicializamos o VADER para que possamos usá-lo em nosso script Python
        sid = SentimentIntensityAnalyzer()

        # Utilizar método polarity_scores no sid e passar dentro dele o message_text produz um dicionário com pontuações negativas, neutras, positivas e compostas para o texto de entrada
        scores = sid.polarity_scores(self.message)

        # Aqui, percorremos as chaves contidas nas pontuações (pos, neu, neg e pontuações compostas) e imprimimos os pares de valores-chave na tela
        # for key in sorted(scores):
             #print('{0}: {1}, '.format(key, scores[key]), end='')
        
        return scores

'''if __name__ == "__main__":
    data = analysisSentiment("I love you!")
    print(str(data.intensitySentiment()))'''