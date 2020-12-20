import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import choice as rchoice
import requests

class Proxy:
    def __init__(self, user_agent, gpu, headless):
        self.driver = None

        self.address = []
        self.port = []
        self.new_address = []
        self.new_port = []

        self.chrome_options = Options()
        self.chrome_options.add_argument(gpu)
        self.chrome_options.add_argument(user_agent)
        self.chrome_options.add_argument(headless)

    def driver_start(self):
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.chrome_options)

    def driver_quit(self):
        self.driver.quit()

    def driver_url(self, url):
        self.driver.get(url)

    def addresses(self, arg):
        content = self.driver.page_source
        soup = BeautifulSoup(content, features='html.parser')

        ip = soup.find_all(arg)

        for row in ip:
            string = re.findall(r'[0-9].*[^</td>]', " " + row.get_text())
            self.address.append(string)

        self.address = self.address[::8]

        del self.address[20::1]

    def ports(self, arg):
        content = self.driver.page_source
        soup = BeautifulSoup(content, features='html.parser')

        ip = soup.find_all(arg)

        for row in ip:
            string = re.findall(r'[0-9].*[^</td>]', " " + row.get_text())
            self.port.append(string)

        self.port = self.port[1::8]

        del self.port[20::1]

    def full_address(self):

        for elem in self.address:
            self.new_address.extend(elem)

        for elem in self.port:
            self.new_port.extend(elem)

        for i, address in enumerate(self.new_address):
            self.new_address[i] = self.new_address[i] + ":" + self.new_port[i]

    def get_choice(self, request_method, url, **kwargs):
        cho = []

        while True:
            try:
                cho = rchoice(self.new_address)
                choice = {'https': cho}
                print('Proxy currently being tested: {}'.format(choice))
                response = requests.request(request_method, url, proxies=choice, timeout=10, **kwargs)
                if response.status_code == 200:
                    print('Current proxy is functional.')
                break
            except:
                print('Error: Could not connect, looking for another proxy.')
                self.new_address.remove(cho)
                pass