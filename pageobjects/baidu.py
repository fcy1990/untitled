
#-*- coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import threading
from threading import Lock
# help(threading)
n=100
def baidu(name):
    global n
    g.acquire()
    temp=n
    input_text = "//input[@id='kw']"
    query_button ="//input[@id='su']"
    url = 'https://www.baidu.com/'
    path = os.path.dirname(os.path.abspath('.'))
    print(path)
    driver = webdriver.Chrome(path + '/tools/chromedriver.exe')
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.XPATH,input_text).send_keys(name)
    # time.sleep(2)
    driver.find_element(By.XPATH,query_button).click()
    time.sleep(2)
    driver.quit()
    n=temp-1
    g.release()

def youdao(name):
    global n
    g.acquire()
    temp = n
    url = 'http://fanyi.youdao.com/'
    input_textarea = "//textarea[@id='inputOriginal']"
    interprate_button = "//a[@id='transMachine']"
    path = os.path.dirname(os.path.abspath('.'))
    print(path)
    driver = webdriver.Chrome(path + '/tools/chromedriver.exe')
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.XPATH, input_textarea).send_keys(name)
    # time.sleep(2)
    driver.find_element(By.XPATH, interprate_button).click()
    time.sleep(2)
    driver.quit()
    n = temp - 1
    g.release()

threads = []
t1 = threading.Thread(target=baidu,args=('python',))
threads.append(t1)
t2 = threading.Thread(target=youdao,args=(u'中国',))
threads.append(t2)

if __name__ == '__main__':
    g=Lock()
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    print('完美!')
    print(n)


