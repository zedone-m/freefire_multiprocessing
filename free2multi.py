from colorama import Fore
import sys
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import selenium
import os
import selenium.common.exceptions
from multiprocessing.dummy import Pool
from multiprocessing import Lock
from tkinter.filedialog import askopenfile
try:
  import numpy as np
except ImportError:
  os.system("pip install numpy")
  import numpy as np
class Free:
 def __init__(self,drive,token,proxy,skin,multi,link="https://reward.ff.garena.com/?access_token="):
   link="https://reward.ff.garena.com/?access_token="
   self.drive=drive
   self.multi=multi
   self.skin=skin
   self.token=token
   link= link+token
   self.proxy= proxy
   self.link=link
   time.sleep(2)
   self.li_st=np.arange(20000)    
 def generate_proxy(self,proxy):
    self.proxy=proxy
    lines = open(self.proxy.name).read().splitlines()
    return random.choice(lines)
 def randome():
    myList=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    c=""
    d=0
    while d<4:
      d=d+1
      k=random.choice(myList)
      c=c+k
    return c
 def windows():
    path=os.path.dirname(__file__)
    return path
 def Choosing_Items():
  items=[]
  s=0
  path=Free.windows()
  skins=path+"\\freefireskins.txt"
  with open(skins) as load:
    loaded = [items.rstrip().strip() for items in load]
    for lines in loaded:
          line_splits = lines.split(':')
          items.append(line_splits)
    return items
 def exploiting(self,loost=0):
  try:
    s=0
    skins= Free.Choosing_Items()
    options= webdriver.ChromeOptions()
    if self.proxy != 0:
      PROXY= self.generate_proxy(self.proxy)
      options.add_argument('--proxy-server=%s' % PROXY)
    else:
      pass
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(self.drive, options=options)
    browser=driver.get(self.link)
    time.sleep(4.2)
    driver.refresh()
    while True:
     try:
      s=s+1
      b=Free.randome()
      c=Free.randome()
      WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="input_serial_1"]'))).send_keys(skins[self.skin][1])
      WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="input_serial_2"]'))).send_keys(b[0:2])
      WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="input_serial_3"]'))).send_keys(c)
      WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="confirm-btn"]'))).click()
      time.sleep(1.4)
      #Lock.acquire()
      pop=str(skins[self.skin][1])+str(b[0:2])+str(c)
      print("[REDEEM CODE THAT HAVE BEEN TRIED]["+Fore.YELLOW+pop+Fore.WHITE+"][TRY NUMBER]["+Fore.YELLOW+str(s)+Fore.WHITE+"]")
      #Lock.release()
      if self.proxy != 0:
        if s==100:
          Free(self.drive,self.token,skin=self.skin,proxy=self.proxy).exploiting()
          data_saving(s)
        else:
          data_saving(s=1)
      else:
        pass
      driver.refresh()
      time.sleep(1)
      #if selenium.common.exceptions.WebDriverException:
          #print(" proxy_error ")
          #driver.quit()
     #     #Free(self.drive,self.token,skin=self.skin,proxy=self.proxy).exploiting()
     except KeyboardInterrupt:
      print("thanks for using our program")
      data= data_saving()
      print(Fore.YELLOW+'[',Fore.WHITE+"YOU TRIDE ABOUT "+data+" CODE",Fore.YELLOW+"]"+Fore.WHITE)
      quit()
     except:
      driver.quit()
      Free(self.drive,self.token,skin=self.skin,multi=self.multi,proxy=self.proxy).exploiting()
      print("a problem had popped out :")
  except KeyboardInterrupt:
      with open("data.txt") as w:
        w.write("0")
      sys.exit()
  except:
      print("Stupid Proxy or access token not working re-enter it... You can exit the program only by pressing CTRL+C")
      data= data_saving()
      print(Fore.YELLOW+'[',Fore.WHITE+"YOU TRIDE ABOUT "+data+" CODE",Fore.YELLOW+"]"+Fore.WHITE)
      driver.quit()
      sleep(1)
      try:
        Free(self.drive,self.token,skin=self.skin,multi=self.multi,proxy=self.proxy).exploiting()
      except KeyboardInterrupt:
        sys.exit()
 def multiprocess(self):
  loost=[]
  for x in range(0,1000000):
    loost.append(x)
    
  pool = Pool(int(self.multi))
  try:
    pool.map(Free(self.drive,self.token,skin=self.skin,multi=self.multi,proxy=self.proxy).exploiting,loost)
  except KeyboardInterrupt:
    print(Fore.RED+"NOTE:"+Fore.YELLOW+"STOPING PROCESSING")
    sys.exit()
 def data_saving(s=0):
  with open("path+\\data.txt") as f:
    data= f.readlines()
    data= int(data)+int(s)
    f.write(data)
    return data
#      print("you tried",s, "times")
#     s=s+1
# exploiting(link,s)*