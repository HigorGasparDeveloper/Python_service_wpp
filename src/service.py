import threading
from db.Connection import Connection
from functions.functions import setInterval
class service:
  interval_seconds = 10
  def run_service(self):
    interval = setInterval()
    interval.setInterval(self.interval_seconds)
    interval.setAction(self.action)
    interval.setStopEvent(threading.Event())
    interval.startThreading()
  def action(self):
    Connection.start_connection(Connection)
    print("Consultar banco as mensagens e enviar via selenium para o whatsapp")
    
classe = service()
classe.run_service()