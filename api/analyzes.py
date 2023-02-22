from database import dataBase as db
from sentiment import sentiment as stm

class analyzes():
    def __init__(self, dados, fell):
        self.data = dados
        self.text = fell

if __name__ == '__main__':
    deA = analyzes(db(), stm('I love you'))
    print(deA.data.extractDeliveryList())
    print(deA.text.englishSentiment())