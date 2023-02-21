import mysql.connector

class dataBase:
  def __init__(self):
    mydb = mysql.connector.connect(host="localhost", user="root", password="1512", database="agilim")
    mycursor = mydb.cursor()
    self.mydb = mydb
    self.mycursor = mycursor

  def extractFellingList(self):
    self.mycursor.execute("SELECT felling FROM instances")
    myresult = self.mycursor.fetchall()
    axis = []
    for x in myresult:
      axis.append(x[0])
    return axis

  def extractDeliveryList(self):
    self.mycursor.execute("SELECT delivery FROM instances")
    myresult = self.mycursor.fetchall()
    axis = []
    for x in myresult:
      axis.append(int(x[0]))
    return axis

if __name__ == '__main__':
    dados = dataBase()
    print(dados.extractDeliveryList())