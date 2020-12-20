from ProxyRotation.proxies import Proxy

USER_AGENT = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
URL = "https://sslproxies.org/"
GPU = "--disable-gpu"
HEADLESS = "--headless"

my_proxies = Proxy(USER_AGENT, GPU, HEADLESS)

my_proxies.driver_start()
my_proxies.driver_url(URL)

arg = 'td'

my_proxies.addresses(arg)
my_proxies.ports(arg)
my_proxies.full_address()
my_proxies.get_choice(request_method='get', url=URL)

my_proxies.driver_quit()