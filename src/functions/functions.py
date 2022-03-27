import time, threading

StartTime=time.time()

class setInterval :
  interval = 0
  action = ''
  stopEvent = ''
  selenium = ''
  def setInterval(self, interval):
    self.interval = interval

  def setSelenium (self, selenium):
    self.selenium = selenium

  def setAction(self, action):
    self.action = action

  def setStopEvent(self,stopEvent):
    self.stopEvent = stopEvent

  def startThreading(self):
    thread=threading.Thread(target=self.__setInterval)
    thread.start()

  def __setInterval(self) :
      nextTime=time.time()+self.interval
      while not self.stopEvent.wait(nextTime-time.time()) :
          nextTime+=self.interval
          self.action(self.selenium)

  def cancel(self) :
      self.stopEvent.set()

class ExecuteSelenium:
  #import webdriver
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service
  from webdriver_manager.chrome import ChromeDriverManager
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.select import Select
  import time
  import pyautogui
  import keyboard as k
  import urllib
  s=Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=s)
  urlGet = ''
  def setUrl(self,value):
    self.urlGet = value
  def executeGet(self):
    self.driver.get(self.urlGet)
  def sendMessage(self, msg,numero):
    #while len(self.driver.find_elements(self.By.ID,"side")) < 1:
      #self.time.sleep(1)
    texto = self.urllib.parse.quote(msg)
    #codificando a mensagem
    link = f"https://web.whatsapp.com/send/?phone={numero}&text={texto}" 
    #f significa que o que ta entre chaves é variavel
    self.driver.get(link)
    #se não achou nada, espera um sec
    while len(self.driver.find_elements(self.By.ID,"side")) < 1:
      self.time.sleep(1)
    #pressionar enter ao escrever a mensagem e esperar um tempo
    self.time.sleep(3)
    self.driver.find_element(self.By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').click()
    self.time.sleep(2)
    self.k.press_and_release('enter')