import mysql.connector
from mysql.connector import errorcode
class Connection: 
  conn = ''
  config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'',
    'database':'automacao_whatsapp',
    'port':'3308',
    'charset':"utf8"
  }
  def start_connection(self):
    try:
      self.conn = mysql.connector.connect(**self.config)
      return [True, "Conexão realizada"]
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return [False, "Erro de autenticação"]
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return [False, "Base de dados não encontrada"]
      else:
        return [False, err]