import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import plotly.express as px

chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

start_url = "https://bestlifeonline.com/best-selling-novels/?nab=0&utm_referrer=https%3A%2F%2Fwww.google.com%2F"
driver.get(start_url)

titles = []
sales = []

content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')

book1 = soup.find_all('div', attrs={'class': 'title'})

count = 0
for row in book1:
    count += 1
    if len(book1) > count:
        titles.append(row.get_text().split("by")[0])

book2 = re.findall(r"(\d{2,3})\s(million)", " "+soup.get_text()+" ")

for row in book2:
    sales.append(row[0])

df = pd.DataFrame({'Book Titles': titles, 'Sold Copies (in millions)': sales})
df.to_csv('books.csv', index=False, encoding='utf-8')
driver.quit()

fig1 = px.bar(df, x='Book Titles', y='Sold Copies (in millions)', title='Top 30 Best-Seller Novels')
fig = px.pie(df, values='Sold Copies (in millions)',
             names='Book Titles', title='Top 30 Best-Seller Novels', hole=.3)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
fig1.show()
