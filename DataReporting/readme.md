A program that scrapes data from https://www.skroutz.gr/c/25/laptop.html?from=families, extracting its laptop names,
prices and average ratings that are saved into a csv file afterwards. Data is stored with its HTML tags inside the file
which is then cleaned and sliced to keep the wanted parts only, then three different charts are made and saved into 
separate PNG files stored into a folder 'plots'. At the same time, an HTML file 'tables.html' is created from the
DataFrame, which is then used to create a new HTML file 'analysis.html' which includes the clean data. The program lastly
converts 'analysis.html' into an PDF file, 'analysis.pdf' being the final Data Report. Used libraries are:
- Pandas
- BeautifulSoup
- Selenium
- ReGex
- Plotly
- PDFkit