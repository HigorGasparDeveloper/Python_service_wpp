import mysql.connector
class Connection: 
  con = ''
  def start_connection(self):
    self.con = mysql.connector.connect(host='localhost',database='db_MeusLivros',user='root',password='123**')
    # if self.con.is_connected():
    #     db_info = self.con.get_server_info()
    #     print("Conectado ao servidor MySQL versão ",db_info)
    #     cursor = self.con.cursor()
    #     cursor.execute("select database();")
    #     linha = cursor.fetchone()
    #     print("Conectado ao banco de dados ",linha)
    # if self.con.is_connected():
    #     cursor.close()
    #     self.con.close()
    #     print("Conexão ao MySQL foi encerrada")