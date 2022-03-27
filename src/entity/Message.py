from db.Connection import Connection
class Message:
  def getMessages(self,selenium):
    connect = Connection.start_connection(Connection)
    if connect[0]:
      cursor = Connection.conn.cursor()
      cursor.execute("SELECT id_message, text_message,number_message FROM message WHERE status_message = 'N' AND was_deleted = 'N';")
      rows = cursor.fetchall()
      print("Lendo",cursor.rowcount,"linha(s) de dados.")
      for row in rows:
        id_message = row[0]
        text_message = row[1]
        number_message = row[2]
        # from functions.functions import ExecuteSelenium
        # ExecuteSelenium.setUrl(ExecuteSelenium,"https://web.whatsapp.com/")
        # ExecuteSelenium.executeGet(ExecuteSelenium)
        # ExecuteSelenium.sendMessage(ExecuteSelenium,text_message,number_message)
        selenium.executeGet(selenium)
        selenium.sendMessage(selenium,text_message,number_message)
        self.updateStateMessage(self,id_message)
    else:
      print(connect[1])
  def updateStateMessage(self,id_message):
    connect = Connection.start_connection(Connection)
    if connect[0]:
      cursor = Connection.conn.cursor()
      cursor.execute("UPDATE message set status_message = 'S' WHERE id_message ={}".format(id_message))
      Connection.conn.commit()
      cursor.close()
      Connection.conn.close()
    else: 
      print(connect[1])