from database import dataBase as db
from sentiment import sentiment as stm

class analyzes():
    def __init__(self, dados, fell):
        self.data = dados
        self.felling = fell

if __name__ == '__main__':
    deA = analyzes(db(), stm('I love you'))
    print(deA.data.extractDeliveryList())
    print(deA.felling.englishSentiment())
    deA.felling.set_text("Esse governo está no início, vamos ver o que vai dar")
    print(deA.felling.sentimentMultinomialNBModel())