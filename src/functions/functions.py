import time, threading

StartTime=time.time()

class setInterval :
  interval = 0
  action = ''
  stopEvent = ''
  def setInterval(self, interval):
    self.interval = interval

  def setAction(self, action):
    self.action = action

  def setStopEvent(self,stopEvent):
    self.stopEvent = stopEvent

  def startThreading(self):
    thread=threading.Thread(target=self.__setInterval)
    thread.start()

  # def __init__(self,interval,action) :
  #     self.interval=interval
  #     self.action=action
  #     self.stopEvent=threading.Event()
  #     thread=threading.Thread(target=self.__setInterval)
  #     thread.start()

  def __setInterval(self) :
      nextTime=time.time()+self.interval
      while not self.stopEvent.wait(nextTime-time.time()) :
          nextTime+=self.interval
          self.action()

  def cancel(self) :
      self.stopEvent.set()
  def test(self):
    print("test")
# inter=setInterval(2,action)
# print('just after setInterval -> time : {:.1f}s'.format(time.time()-StartTime))

# # will stop interval in 5s
# t=threading.Timer(5,inter.cancel)
# t.start()