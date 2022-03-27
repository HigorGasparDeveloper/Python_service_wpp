import threading

import selenium
from entity.Message import Message
from functions.functions import setInterval
from functions.functions import ExecuteSelenium
class service:
  interval_seconds = 60 * 15
  def run_service(self):
    selenium = ExecuteSelenium
    selenium.setUrl(selenium,"https://web.whatsapp.com/")
    selenium.executeGet(selenium)
    self.action(selenium)
    # interval = setInterval()
    # interval.setInterval(self.interval_seconds)
    # interval.setAction(self.action)
    #interval.setSelenium(selenium)
    # interval.setStopEvent(threading.Event())
    # interval.startThreading()
  def action(self, selenium):
    Message.getMessages(Message,selenium)
    
classe = service()
classe.run_service()