import sys
from selenium import webdriver
from getpass import getpass
import requests
import time
from tkinter.filedialog import askopenfile
from free2multi import Free
import random
import re,os
from free2multi import Free
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
if "win" in sys.platform:
  os.system("cls")
else:
  os.system("clear")
###########fuctions##################
def windows():
    path=os.path.dirname(__file__)
    return path
def Choosing_Items():
  items=[]
  path=windows()
  skins=path+"\\freefireskins.txt"
  with open(skins) as load:
    loaded = [items.rstrip().strip() for items in load]
    for lines in loaded:
          line_splits = lines.split(':')
          items.append(line_splits)
    for d,s in zip(items,range(len(items))):
            print(Fore.YELLOW+"[",s,']',Fore.WHITE+"Choose",d[0])
    print(Fore.WHITE+'''
  Choose What ITEM You wanna crack:''')
    try:
      choosing= int(input("  "))
      print(Fore.YELLOW+"[-]",Fore.WHITE+"You Chose", items[choosing][0])
      print(Fore.RED+'''  {-''',Fore.WHITE+"Please Wait While Processing",Fore.RED+"-}",)
    except KeyboardInterrupt:
      sys.exit()
    except:
      Choosing_Items()
    time.sleep(5)
    return choosing
print(Fore.WHITE+'''
    WELCOME TO MY FREE FIRE CRACKING PROGRAM
         PLEASE SUBSCRIBE TO MY CHANEL
''')
print(Fore.YELLOW+'''

 ______ _______ ______         _____  __   _ _______
  ____/ |______ |     \       |     | | \  | |______
 /_____ |______ |_____/ _____ |_____| |  \_| |______
                                                    

''')
class FacebookLogin():
    def __init__(self, email, password,cracking ,browser='Chrome'):
        # Store credentials for login
        self.cracking=cracking
        self.email = email
        self.password = password
        self.drive= drive
        self.browser=browser


    def login(self):
        if self.browser == 'Chrome':
            # Use chrome
            driver = webdriver.Chrome(self.drive)
        elif browser == 'Firefox':
            # Set it to Firefox
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
        email_element = driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input

        password_element = driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too

        login_button = driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
        time.sleep(6) # Wait for 2 seconds for the page to show up
        ACCESS_URL= driver.current_url
        driver.quit()
        print(Fore.YELLOW+'[-] ')
        print('the url is', end= '')
        print(Fore.YELLOW+": ")
        print(ACCESS_URL)
        s=0
        FacebookLogin.access(self.cracking)
    def access(cracking):
        print(Fore.YELLOW+"[-] ",Fore.WHITE+"follow the video to add the access token:")
        token=input("enter the token: ")
        print('''  1]- Use Proxy''',
          '''  2]- Don't Use Proxy ''' )
        print(Fore.RED+"NOTE:",Fore.WHITE+"EMPTY WILL TAKE SECOND OPTION")
        PROXY= input("[+]:")
        if PROXY=="1": 
          proxy=askopenfile(title="Choose Your ProxyList FileName:",filetypes =[('Text Files', '*.txt')])
          Free(drive=drive,token=token,proxy=proxy,skin=cracking,multi=multi).multiprocess()
        else:
          Free(drive=drive,token=token,proxy=0,skin=cracking,multi=multi).multiprocess()
    def access_(self):
        print(Fore.YELLOW+"[-] ",Fore.WHITE+"follow the video to add the access token:")
        token=input("enter the token: ")
        print('''  1]- Use Proxy''',
          '''  2]- Don't Use Proxy ''' )
        print(Fore.RED+"NOTE:",Fore.WHITE+"EMPTY ")
        PROXY= input("[+]:")
        if PROXY=="1": 
          proxy=askopenfile(title="Choose Your ProxyList FileName:",filetypes =[('Text Files', '*.txt')])
          Free(drive=self.drive,token=token,multi=multi,proxy=proxy,skin=self.cracking).multiprocess()
        else:
          Free(drive=self.drive,token=token,multi=multi,proxy=0,skin=self.cracking).multiprocess()

if __name__ == '__main__':
  try:
    cracking= Choosing_Items()
    print(Fore.WHITE+"")
    print("  Would you like to login or pass it for the access token?")
    print(Fore.RED+'''
    1)''',Fore.WHITE+'''- Inputing login data
    '''+Fore.RED+'''2)''',Fore.WHITE+'''- Pass Through directly to the access token
      ''')
    one= int(input("[-]: "))
    multi= input(Fore.RED+" how many bot you wanna use: "+Fore.WHITE)
    try:
       with open("chromedriver.txt",'r') as f:
          drive=(f.readlines())
    except:   
       drive=input("webdriver path: ")
       with open("chromedriver.txt",'w') as f:
           f.writelines(drive)
    if one==2:
      email="no need for"
      password="no need for too"
      FacebookLogin(email, password, cracking, browser='Chrome').access_()
      sys.exit()
    else:
      pass
    email= input("Input your email: ")
    password= getpass("Input your password: ")
    driver= webdriver.Chrome(drive)
    # Enter your login credentials here
    browser=driver.get("https://reward.ff.garena.com/")
    free_log=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="btn-item facebook"]')))
    free_log.click()
    LOGIN_URL = driver.current_url
    driver.quit()
    fb_login = FacebookLogin(email, password,cracking, multi=multi ,browser='Chrome')
    fb_login.login()
  except KeyboardInterrupt:
    print(Fore.WHITE)
    sys.exit()
