from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
import socket


def login(username='', password=''):
    # 打开firefox浏览器
    s = Service("./geckodriver")  # 驱动所在位置
    driver = webdriver.Firefox(service=s)
    # 打开DUT登陆页
    url = "http://auth.dlut.edu.cn/eportal/index.jsp?wlanuserip=36403c6fd4c73626cb1a0d515f08fce4&wlanacname" \
          "=df066d169c39d07305dcabb988054834&ssid=&nasip=b7b559c9e7b461d404d0b61516e928ce&snmpagentip=&mac" \
          "=9a026df06fb402147d03bb4b43d7154d&t=wireless-v2&url" \
          "=b4cd630f5638399d22d38b9b44701dddda81144d7cf8bcae9a500f4ca17a4e0f289f919ba2e3320e&apmac=&nasid" \
          "=df066d169c39d07305dcabb988054834&vid=164600d61b566457&port=32caf90bbb95de10&nasportid" \
          "=bb1dfb88cacc0f8bb54291d1da6e6ff9314ebecb540ab497d098f0f8188a1014b1efd732ecb883d9be39567b3cadf013 "
    driver.get(url)
    time.sleep(10)
    '''
    调用selenium库中的find_element()方法定位输入框，
    同时使用send_keys()方法在其中输入信息
    '''
    driver.find_element(value='username_tip').click()
    driver.find_element(value='username').send_keys(username)
    driver.find_element(value='pwd_tip').click()
    driver.find_element(value='pwd').send_keys(password)
    '''
    调用selenium库中的find_element()方法定位登录按钮，
    同时使用click()方法对按钮进行点击
    '''
    driver.find_element(value='loginLink_div').click()

    if not isConected(testserver=("www.baidu.com", 443)):
        raise ValueError('Network is not connected.')


def isConected(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False


if __name__ == "__main__":
    username = ''
    psd = ''
    while True:
        every = 300  # 多少秒检查一次
        if isConected(testserver=("www.baidu.com", 443)):
            print('Network connected!')
        else:
            try:
                login(username=username, password=psd)
            except:
                print('Login failed or network has been connected, try again in {:d} seconds'.format(every))
        time.sleep(every)
        continue
