import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import plotly.express as px
import plotly.io as pio
import os
import pdfkit

class Skroutz:
    def __init__(self, user_agent, gpu, headless):
        self.driver = None

        self.titles = []
        self.prices = []
        self.ratings = []

        self.chrome_options = Options()
        self.chrome_options.add_argument(user_agent)
        self.chrome_options.add_argument(gpu)
        self.chrome_options.add_argument(headless)

    def driver_start(self):
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.chrome_options)

    def driver_quit(self):
        self.driver.quit()

    def get_url(self, url):
        self.driver.get(url)

    def get_titles(self, arg1, arg2, arg3):

        content = self.driver.page_source
        soup = BeautifulSoup(content, features='html.parser')

        laptops = soup.find_all(arg1, attrs={arg2: arg3})

        for row in laptops:
            if len(row.get_text()) > 0:
                string = re.split(r'[(].*[)]', row.get_text())
                self.titles.append(("".join(string[::2]).replace("  ", " ")))

        self.titles = self.titles[0::2]

        for i, title in enumerate(self.titles):
            self.titles[i] = self.titles[i] + " {" + str(i+1) + "}"

    def get_prices(self, arg1, arg2, arg3):

        content = self.driver.page_source
        soup = BeautifulSoup(content, features='html.parser')

        laptops = soup.find_all(arg1, attrs={arg2: arg3})

        for row in laptops:
            string = re.findall(r"([.\d]+.?\d*)", " " + row.get_text().replace(".", "").replace(",", ".") + " ")[0]
            self.prices.append(string)

    def get_ratings(self, arg1, arg2, arg3):

        content = self.driver.page_source
        soup = BeautifulSoup(content, features='html.parser')

        laptops = soup.find_all(arg1, attrs={arg2: arg3})

        for row in laptops:
            string = re.findall(r"([0-9]\W{1,2})", " " + row.get_text().replace(",", ".") + " ")
            self.ratings.append("".join(string))

    def get_df(self):
        df = pd.DataFrame({'Laptops': self.titles,
                                'Price': self.prices,
                                'Ratings': self.ratings})
        df.to_csv('laptops.csv', index=False, encoding='utf-8')
        df.to_html('tables.html')

    def get_plot(self):
        if not os.path.exists("plots"):
            os.mkdir("plots")

        pio.kaleido.scope.default_format = "png"

        df = pd.read_csv('laptops.csv')

        fig_a = px.bar(df, y='Price', x='Laptops', title='Comparing the cost of each laptop.', text='Price')
        fig_a.update_layout(
            height=800,
            width=800,
        )
        fig_a.update_traces(textposition='outside', texttemplate='%{text:.2s}')

        fig_b = px.scatter(df, y='Ratings', x='Laptops', title='Comparing average ratings of each laptop.', text='Ratings')
        fig_b.update_layout(
            height=800,
            width=800,
        )
        fig_b.update_traces(textposition='bottom center', texttemplate='%{text:.2s}')

        fig_c = px.line(df, y='Price', x='Laptops', title='Cost of laptops within a line chart.')
        fig_c.update_layout(
            height=800,
            width=800,
        )

        fig_a.write_image('plots/laptops1.png')
        fig_b.write_image('plots/laptops2.png')
        fig_c.write_image('plots/laptops3.png')

    def get_pdf(self):
        path_wkthmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

        options = {
            'page-size': 'A4',
            'margin-top': '0.12in',
            'margin-right': '0.12in',
            'margin-bottom': '0.12in',
            'margin-left': '0.12in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None,
            'enable-local-file-access': None
        }

        pdfkit.from_file('analysis.html', 'analysis.pdf', configuration=config, options=options)