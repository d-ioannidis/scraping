from skroutz import Skroutz

USER_AGENT = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
URL = "https://www.skroutz.gr/c/25/laptop.html?from=families"

my_skroutz = Skroutz(USER_AGENT, "--disable-gpu", "--headless")

my_skroutz.driver_start()
my_skroutz.get_url(URL)

arg1 = 'a' # HTML tags to pass as arguments for data collection of the website's content
arg2 = 'class'
arg3 = 'js-sku-link'

my_skroutz.get_titles(arg1, arg2, arg3)

arg3 = 'js-sku-link sku-link'

my_skroutz.get_prices(arg1, arg2, arg3)

arg1 = 'div'
arg2 = 'class'
arg3 = 'rating-wrapper'

my_skroutz.get_ratings(arg1, arg2, arg3)
my_skroutz.get_df()
my_skroutz.get_plot()
my_skroutz.get_pdf()

my_skroutz.driver_quit()
